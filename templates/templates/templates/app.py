from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# صفحة تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # التحقق البسيط
        if username == 'admin' and password == '1234':
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="بيانات الدخول غير صحيحة")

    return render_template('login.html')

# لوحة التحكم بعد الدخول
@app.route('/dashboard')
def dashboard():
    return "<h2>مرحبًا بك في نظام وكالة تماسك للسياحة والسفر 🌍</h2>"

if __name__ == '__main__':
    app.run(debug=True)
