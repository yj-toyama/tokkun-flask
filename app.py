from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    text = None
    if request.method == 'POST':
        text = request.form['text']
    return render_template('home.html', text=text)

@app.route('/api/helloworld', methods=['GET'])
def hello_world():
    return {"message": "hello world"}


if __name__ == '__main__':
    app.run(debug=True)
