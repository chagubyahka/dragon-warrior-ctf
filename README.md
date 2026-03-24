# 🐉 Dragon Warrior CTF — Web Pentest Write-up

## 📌 Overview
Goal: build a vulnerable web application where a player must:
- find hidden credentials  
- extract a key from an image  
- decrypt a stored password  
- log in to access the flag  

---

## ⚙️ Tech Stack
- Python (Flask)
- HTML / CSS / JavaScript
- `.env` for secrets
- Docker (optional)
- Nginx (optional)

---

## 📁 Project Structure

```
project/
│
├── app.py
├── index.html
├── logins.html
├── success.html
├── static/
│   └── image.png
├── .env
├── requirements.txt
```

---

## 🔐 Environment Variables (.env)

```
SECRET_KEY=supersecretkey
DRAGON_USERNAME=admin
DRAGON_PASSWORD=ThereIsNoSecretIngredient01
```

⚠️ Important:
- Never commit `.env` to Git
- Add `.env` to `.gitignore`

---

## 🐍 Flask Backend

```python
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, session

load_dotenv()

app = Flask(__name__, template_folder='.')

app.secret_key = os.getenv("SECRET_KEY")

USERNAME = os.getenv("DRAGON_USERNAME", "").lower()
PASSWORD = os.getenv("DRAGON_PASSWORD", "")


@app.route("/")
def home():
    error = request.args.get("error")
    return render_template("index.html", error=error)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").lower()
    password = request.form.get("password", "")

    if username == USERNAME and password == PASSWORD:
        session["logged_in"] = True
        return redirect("/success")

    return redirect("/?error=Access denied")


@app.route("/success")
def success():
    if not session.get("logged_in"):
        return redirect("/")
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🖼️ Hidden Key in Image (Metadata)

### Embed a key:
```
exiftool -Comment="dragon_key_123" image.png
```

### Extract the key:
```
exiftool image.png
```

---

## 🔑 Encrypted Password (Client-Side)

```javascript
localStorage.setItem("ciphertext", "U2FsdGVkX1...");
```

---

## 🔎 Attack Walkthrough (Solution Path)

1. Open the website  
2. Download the image from `/static`  
3. Extract metadata → obtain the key  
4. Inspect browser localStorage  
5. Find the ciphertext  
6. Decrypt it using the key  
7. Log in  
8. Access `/success`  

---

## 🏁 success.html

```html
<h1>Congratulations!</h1>
<p>FLAG{dragon_warrior_ctf}</p>
```

---