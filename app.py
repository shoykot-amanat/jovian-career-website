from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[
    {
        'id': 1,
        'title': 'Data Analyst',
        'Location': 'Dhaka, Bangladesh',
        'Salary': 'BDT 60,000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'Location': 'Chittagong, Bangladesh',
        'Salary': 'BDT 1,00,000',
    },
    {
        'id': 3,
        'title': 'Software Engineer',
        'Location': 'Cumilla, Bangladesh',
        'Salary': 'BDT 80,000',
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'Location': 'Mymensing, Bangladesh'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)