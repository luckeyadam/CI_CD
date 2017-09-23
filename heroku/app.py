from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'The hamster has been integrated'

if __name__ == "__main__":
    app.run()
