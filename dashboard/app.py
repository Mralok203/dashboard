from flask import Flask, render_template, request, redirect, session, url_for
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

DATA_FILE = 'users.xlsx'
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=['Name', 'Phone', 'Password', 'Email', 'Address', 'Item', 'Date'])
    df.to_excel(DATA_FILE, index=False)

def load_users():
    return pd.read_excel(DATA_FILE)

def save_users(df):
    df.to_excel(DATA_FILE, index=False)

@app.route('/')
def root():
    return redirect('/home')

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']
        item = request.form.get('item', '')
        date = datetime.now().strftime('%Y-%m-%d')

        df = load_users()
        if phone in df['Phone'].astype(str).values:
            return render_template('register.html', error="Phone number already exists.")

        new_user = {
            'Name': name,
            'Phone': phone,
            'Password': password,
            'Email': email,
            'Address': address,
            'Item': item,
            'Date': date
        }
        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
        save_users(df)
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']

        if phone == 'admin' and password == 'admin123':
            session['user'] = 'admin'
            return redirect('/dashboard')

        df = load_users()
        user = df[(df['Phone'].astype(str) == phone) & (df['Password'] == password)]
        if not user.empty:
            session['user'] = phone
            return redirect('/dashboard')
        else:
            error = "Invalid credentials."

    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    df = load_users()

    if session['user'] == 'admin':
        name_filter = request.args.get('name', '').strip().lower()
        date_filter = request.args.get('date', '').strip()

        if name_filter:
            df = df[df['Name'].str.lower().str.contains(name_filter)]
        if date_filter:
            df = df[df['Date'] == date_filter]

        return render_template('dashboard.html', user=df.to_dict(orient='records'), is_admin=True)

    user_data = df[df['Phone'].astype(str) == session['user']]
    return render_template('dashboard.html', user=user_data.to_dict(orient='records'), is_admin=False)

@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    if 'user' not in session or session['user'] == 'admin':
        return redirect('/login')

    df = load_users()
    user_data = df[df['Phone'].astype(str) == session['user']].iloc[0]

    if request.method == 'POST':
        item = request.form.get('item', '').strip()
        date = datetime.now().strftime('%Y-%m-%d')

        new_entry = user_data.to_dict()
        new_entry['Item'] = item
        new_entry['Date'] = date

        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        save_users(df)

        return redirect('/dashboard')

    return render_template('add_item.html', user=user_data)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/home')

if __name__ == '__main__':
    app.run(debug=True)