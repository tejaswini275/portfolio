from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Portfolio Page


if __name__ == '__main__':
    app.run(debug=True)
