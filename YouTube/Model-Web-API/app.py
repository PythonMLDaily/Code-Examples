from flask import Flask, render_template, request, jsonify
from model.model import predict_salary
from waitress import serve

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Welcome to the Salary Prediction homepage"


@app.route('/api/calculate/salary', methods=['POST'])
def salary_calculation_api():
    return jsonify({
        "salary": "{:.2f}".format(predict_salary(request.json['experience'], request.json['level']))
    })


@app.route('/calculate/salary', methods=['GET'])
def salary_calculation_get():
    # Jinja2 template engine is used to render HTML page
    return render_template('form.html')


@app.route('/calculate/salary', methods=['POST'])
def salary_calculation():
    salary = "{:.2f}".format(predict_salary(request.form['experience'], request.form['level']))
    return render_template('form.html', salary=salary, experience=request.form['experience'],
                           level=request.form['level'])


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
