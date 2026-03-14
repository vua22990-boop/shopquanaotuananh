from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Shop Quan Ao Tuan Anh"

if __name__ == "__main__":
    app.run()
