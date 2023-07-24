from flask import Flask, render_template
from routes.user import user
from routes.task import task
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv('.env')


app.register_blueprint(user)
app.register_blueprint(task)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)