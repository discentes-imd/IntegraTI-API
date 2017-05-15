# Import flask dependencies
from flask import Blueprint, flash, g, session, url_for

# Import password / encryption helper tools

# Import the database object from the main app module
from app import db

# Import module forms
# from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


# Set the route and accepted methods
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():

    # If sign in form is submitted
    # form = LoginForm(request.form)

    # Verify the sign in form
    # if form.validate_on_submit():

    #     user = User.query.filter_by(email=form.email.data).first()

    #     if user and check_password_hash(user.password, form.password.data):

    #         session['user_id'] = user.id

    #         flash('Welcome %s' % user.name)

    #         return redirect(url_for('auth.home'))

    #     flash('Wrong email or password', 'error-message')

    # return render_template("auth/signin.html", form=form)
    return True
