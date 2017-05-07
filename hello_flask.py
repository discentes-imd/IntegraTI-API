from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/hello/admin')
def hello_admin():
   return render_template('hello.html', name='admin')

@app.route('/hello/guest/<guest>')
def hello_guest(guest):
   return render_template('hello.html', name=guest)

@app.route('/hello/user/<name>')
def hello_user(name):
	if name =='admin':
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest',guest = name))

@app.route('/score/<int:score>')
def hello_name(score):
   return render_template('score.html', marks = score)

@app.route('/result')
def result():
   dicto = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dicto)
  
@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success',name = user))

if __name__ == "__main__":
	app.run(debug = True)