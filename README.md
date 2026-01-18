Phishing Simulator

A safe, educational phishing‑awareness training tool

This project is a lightweight Flask‑based phishing‑simulation platform designed for security awareness training, SOC analytics, and demonstrations of phishing techniques in a controlled environment. It helps organizations teach users how phishing works without collecting or storing real credentials.

Features

• Realistic phishing landing page for awareness training

• 	Click‑tracking and visit logging (IP, timestamp, user agent)

• 	Safe form‑submission logging without storing real credentials

• 	CSV‑based reporting for SOC analysts and training teams

• 	Customizable templates for different phishing scenarios

• 	Simple Flask backend that’s easy to extend

Important Safety Notice

This tool is intended only for authorized training and educational use.

It is not designed to capture or store real usernames or passwords. I coded for only user results to test if a user will sign in. During the POST phase the user will get the page: "Submission Received. This was part of a security test." Only and the results only have a GET Thank you page. 

Test will not get capture results of the compromised account, instead its a base report if the user did input their information of a time stamp, Enagement Summary, IP source, User-Agent breakdown, Mitre Attack, Assesment, and Recommendations. 

If used in a corporate environment:

• 	Inform users that this is part of a sanctioned security‑awareness program

• 	Never collect real credentials

• 	Replace password fields with dummy placeholders

• 	Use the reporting features only for behavioral analytics of submission

Project Structure

```
Phishing-Simulator/
│
├── app.py               # Flask backend
├── templates/
│   └── index.html       # Landing page template
├── credentials.csv      # Training telemetry (no real credentials)
└── README.md            # Project documentation
```

 How It Works

1. 	A user receives a simulated phishing email (created by your training team).

2. 	The link directs them to this Flask‑hosted landing page.

3. 	The simulator logs:

• 	Visit timestamp

• 	IP address

• 	User agent

• 	Whether they attempted to submit the form

4. 	No real credentials are stored — only behavioral metrics.

5. 	SOC analysts or training staff review the CSV report to measure awareness

Installation:

On kali or linux: 
```
git clone https://github.com/HackingHusky/Phishing-Simulator-/tree/main
cd Phising Simulator
chmod +x app.py
chmod +x app1.py
chomd +x results.py
pip install flask

or in kali

python3 -m venv venv

source venv/bin/activate

pin install flask
```

How it works;

Simple:
```
python3 app1.py

```
 
Then go to the landing page, then users will submit their login info. 

It's defaulted http://127.0.0.1:5000 

Or if you like:

```
python3 app.py --host <your ip> --port <port you want>
```

Then Ctrl+C to end the script, it will give an cvs report, next run this:
```
pyhton3 results.py
```

Then that will give you the resultes of the test. 

Each entry includes:

• 	Timestamp

• 	IP address

• 	User agent

• 	Whether a form was submitted

Customization

You can modify:

• 	 for custom phishing themes

• 	CSS and images in 

• 	Logging behavior in 

This makes it easy to simulate:

• 	Fake login portals

• 	Fake document downloads

• 	MFA‑themed phishing

• 	HR‑themed phishing

All while keeping the simulation safe.

Contributing

Pull requests are welcome.
If you have ideas for new training modules or reporting features, feel free to open an issue.

License
MIT License — free to use for training, research, and awareness programs.
