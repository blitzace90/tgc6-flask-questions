from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# your code here!
@app.route('/')
def home():
    return render_template('index.template.html')

@app.route('/products')
def product():
    return render_template('product.template.html')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)