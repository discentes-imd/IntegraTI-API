from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def hello_world():
   return "Hello World"

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
	if name =='admin':
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest',guest = name))
  
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