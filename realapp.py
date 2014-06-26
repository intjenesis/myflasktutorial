from flask import Flask, render_template, request, redirect
app = Flask(__name__)
#test
app.vars = {}

app.questions = {}
app.questions['How many eyes do you have?'] = ('1','2','3')
app.questions['Which fruit do you like best?'] = ('banana','mango','pineapple')
app.questions['Do you like cupcakes?'] = ('yes','no','maybe')

app.nquestions = len(app.questions)

@app.route('/index', methods=['GET','POST'])
def index():
	nquestions = app.nquestions
	if request.method == 'GET':
		return render_template('userinfo_lulu.html',num=nquestions)
		
	else:
		#request was a POST
		app.vars['name'] = request.form['name']
		app.vars['age'] = request.form['age']
		
		f = open('%s_%s.txt' % (app.vars['name'], app.vars['age']),'w')
		f.write('Name: %s\n' % (app.vars['name']))
		f.write('Age: %s\n\n' % (app.vars['age']))
		f.close()
		
		return redirect('/main')
	
@app.route('/main')
def main():
	if len(app.questions) == 0:
		return render_template('end_lulu.html')
	return redirect('/next')

@app.route('/next', methods=['GET'])
def next1():
	n = app.nquestions - len(app.questions) + 1
	q = app.questions.keys()[0]
	a1, a2, a3 = app.questions.values()[0]
	
	app.currentq = q
	
	return render_template('layout_lulu.html', num=n, question=q, ans1=a1, ans2=a2, ans3=a3)
	
@app.route('/next', methods=['POST'])
def next2():
	f = open('%s_%s.txt' % (app.vars['name'],app.vars['age']),'a')
	f.write('%s\n' % (app.currentq))
	f.write('%s\n\n' % (request.form['answerfromlayout']))
	f.close()
	
	#remove question
	del app.questions[app.currentq]
	
	return redirect('/main')

if __name__ == '__main__':
	app.run(debug=True)