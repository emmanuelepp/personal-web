from flask import Flask, render_template
import datetime

app = Flask(__name__)

date = datetime.datetime.now().strftime('%Y')


@app.route('/')
def index():
    return render_template('index.html', date=date)


def initializer(config):
    app.config.from_object(config)
    return app
