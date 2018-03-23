from flask import Flask, render_template, request 
app = Flask(__name__)
@app.route('/')
def student():
	return render_template('render_template_2.html') 

@app.route('/result',methods=['POST', 'GET']) 
def result():
    if request.method=='POST':
        result = request.form
        return render_template("render_template_2_result.html",result = result)


