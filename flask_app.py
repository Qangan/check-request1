from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    print(request.headers)
    return '123123'
if __name__ == '__main__':
    app.run(debug=True)
