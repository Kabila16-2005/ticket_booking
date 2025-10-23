from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

EXCEL_FILE = "ticket.xlsx"

# Create Excel file if not exist
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=["Name", "Date", "Gender", "Seats", "SeatType", "From", "To", "TicketType"])
    df.to_excel(EXCEL_FILE, index=False)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username and password:
        return redirect(url_for('options'))
    return redirect(url_for('home'))

@app.route('/options')
def options():
    return render_template('home.html')

@app.route('/book/<ticket_type>')
def book(ticket_type):
    if ticket_type not in ['bus', 'train']:
        return redirect(url_for('options'))
    return render_template('book.html', ticket_type=ticket_type)

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "Name": request.form['name'],
        "Date": request.form['date'],
        "Gender": request.form['gender'],
        "Seats": request.form['seats'],
        "SeatType": request.form['seat_type'],
        "From": request.form['from_place'],
        "To": request.form['to_place'],
        "TicketType": request.form['ticket_type']
    }

    df = pd.read_excel(EXCEL_FILE)
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)

    return render_template('success.html', name=data['Name'], ticket=data['TicketType'])

if __name__ == "__main__":
    app.run(debug=True)
