from flask import Flask, render_template, request
import base64

app = Flask(__name__)

def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def reverse_cipher(text):
    return text[::-1]

def base64_cipher(text, mode):
    if mode == "encrypt":
        return base64.b64encode(text.encode("utf-8")).decode("utf-8")
    elif mode == "decrypt":
        try:
            return base64.b64decode(text.encode("utf-8")).decode("utf-8")
        except Exception as e:
            return f"❌ Invalid Base64 string: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        message = request.form["message"]
        mode = request.form["mode"]
        algorithm = request.form["algorithm"]
        shift = int(request.form.get("shift", 0))  # shift is optional now

        if algorithm == "caesar":
            result = caesar_cipher(message, shift, mode)
        elif algorithm == "reverse":
            result = reverse_cipher(message)
        elif algorithm == "base64":
            result = base64_cipher(message, mode)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
