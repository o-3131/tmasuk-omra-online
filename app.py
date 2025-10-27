from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# صفحة الدخول
@app.route('/')
def login():
    return render_template('login.html')

# بعد الدخول
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# الصفحة الرئيسية
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
