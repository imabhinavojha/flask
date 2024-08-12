from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

JOBS = [
    {
        "id": 1,
        "Title": "SDE-1",
        "Location": "Noida",
        "Salary": "Rs. 10,00,000"
    },
    {
        "id": 2,
        "Title": "SDE-2",
        "Location": "Noida",
        "Salary": "Rs. 20,00,000"
    },
    {
        "id": 3,
        "Title": "SDE-3",
        "Location": "Noida",
    },
]


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/about')
def about():
  skills = [
      {
          'name': 'HTML/CSS',
          'level': 90
      },
      {
          'name': 'JavaScript',
          'level': 80
      },
      {
          'name': 'Python',
          'level': 70
      },
      {
          'name': 'Java',
          'level': 60
      },
  ]
  return render_template('about.html',skills=skills, email='abhinavojha59@hotmail.com', role='SDET', phone='9794757466', cv='<CV>')



@app.route('/skills')
def skills():
  return render_template('skills.html')


@app.route('/work')
def work():
  return render_template('work.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')


@app.route("/home1")
def about1():
  return render_template('home.html')


@app.route("/home2")
def about2():
  return render_template('homeUsingBootstrap.html',
                         jobs=JOBS,
                         company_name="NS")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
