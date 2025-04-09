Encryptor-Decryptor

This is a web application built using Python Flask that allows users to encrypt and decrypt messages using multiple cipher algorithms.

Features

Supports Caesar Cipher, Vigenère Cipher, Reverse Cipher, and Base64 Encode/Decode

Simple user interface with a form to input message, shift/key, and choose the cipher

Works for both encryption and decryption

Clean design with dynamic input fields based on selected algorithm


Technologies Used

Python

Flask

HTML

CSS

JavaScript


How to Run the Project

1. Clone the repository
git clone https://github.com/csm2310/Encryptor-Decryptor.git


2. Navigate to the project folder
cd Encryptor-Decryptor


3. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate (Windows: venv\Scripts\activate)


4. Install Flask
pip install Flask


5. Run the app
python app.py


6. Open your browser and go to
http://127.0.0.1:5000/



Cipher Examples

Caesar Cipher

Input: Hello

Shift: 3

Output: Khoor


Reverse Cipher

Input: Hello World

Output: dlroW olleH


Base64

Input: Hello World

Encoded: SGVsbG8gV29ybGQ=



Project Structure

app.py – Main Python Flask app

templates/index.html – HTML page

static/style.css – Styling

README.md – Project info


Author

Created by https://github.com/csm2310
Feel free to fork the repo, suggest improvements, or use it in your own projects!
