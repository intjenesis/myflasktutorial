from flask import Flask, render_template, request, redirect
app = Flask(__name__)

app.varss = {}

@app.route('/index', methods=['GET','POST'])
def index():
	nquestions = 5
	if request.method == 'GET':
		return render_template('userinfo_lulu.html', num=nquestions)
	else:
		#request was a POST
		app.varss['name'] = request.form['name']
		app.varss['age'] = request.form['age']
		
		f = open('%s_%s.txt' % (app.varss['name'], app.varss['age']),'w')
		f.write('Name: %s\n' % (app.varss['name']))
		f.write('Age: %s\n\n' % (app.varss['age']))
		f.close()
		
		return render_template('layout_lulu.html', num=1, question='How many eyes do you have?', ans1=1, ans2=2, ans3=3)

@app.route('/next', methods=['POST'])
def next():
	return redirect('/usefulfunction')

@app.route('/usefulfunction', methods=['GET'])
def usefulfunction():
	return render_template('end_lulu.html')

if __name__ == '__main__':
	app.run(debug=True)