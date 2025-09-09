from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test():
    return {"message": "Server is running"}

# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5002)