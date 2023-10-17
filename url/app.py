import string
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
url_database = {}


def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = generate_short_url()
        url_database[short_url] = long_url
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')


@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_database.get(short_url)
    if long_url:
        return redirect(long_url)
    return "Short URL not found."


if __name__ == '__main__':
    app.run(debug=True)
