from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <body style="font-family:Arial; text-align:center; margin-top:500px;">
            <h1>bro abhi click on this </h1>

            <button onclick="alert('Hello abhi')">
                Click Me
            </button>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
