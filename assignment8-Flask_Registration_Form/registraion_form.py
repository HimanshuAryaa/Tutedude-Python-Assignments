from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/confirmation', methods=['GET', 'POST'])

def confirmation():
    if request.method == 'POST':
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            return "Passwords do not match!", 400
        name = request.form.get('name')
        return render_template('confirmation.html', name=name)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)