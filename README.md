AI Email Replyer & Sender

This project is a web-based application that generates professional emails using an AI language model and allows users to send emails directly with optional attachments. The system helps automate email writing and improves productivity by reducing the time required to compose structured emails.

The application is built using Python and Streamlit, with an external AI model used to generate email content dynamically based on user input.

🚀 Features

Generate emails based on:

Email purpose or context

Selected tone

Additional instructions

Supports multiple email tones:

Professional

Formal

Friendly

Follow-up

Apology

Request

Edit generated email before sending

Send emails directly using Gmail SMTP

Optional file attachments (Resume or documents)

Clean and user-friendly interface

🛠 Technologies Used

Python

Streamlit

Requests library

SMTP (Gmail)

AI Language Model API

📂 Project Structure project-folder/ │ ├── app.py # Main application ├── ai_email_generator.py # AI email generation logic ├── email_sender.py # Email sending logic ├── requirements.txt # Dependencies └── README.md

⚙ How to Run the Project

Install required libraries:

pip install -r requirements.txt

Add your AI API key in:

ai_email_generator.py

Run the application:

streamlit run app.py

Open the browser at:

http://localhost:8501

🔐 Gmail Configuration

To send emails:

Enable 2-Step Verification in your Google account

Generate a Gmail App Password

Use the App Password instead of your Gmail password

🧠 How It Works

The user enters the email purpose and selects a tone. The system generates a structured email using an AI model. The user can review or edit the email and send it directly with optional attachments.

👨‍💻 Author

Hemant Jain B.Tech Computer Science Engineering
