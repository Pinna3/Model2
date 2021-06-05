from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data1 = request.form.get('select1')
        data2 = request.form.get('select2')
        data3 = request.form.get('select3')
        data = [data1, data2, data3]
        with open('submit.json', 'w') as outfile:
            json.dump(data, outfile)
        return 'Added to wishlist!'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
