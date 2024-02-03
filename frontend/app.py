from flask import Flask, render_template

app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logReport')
def logAReport():
    return render_template('logRubbishReport.html')

@app.route('/viewReport')
def viewReports():
    return render_template('viewReport.html')

@app.route('/history')
def history():
    return render_template('history.html')