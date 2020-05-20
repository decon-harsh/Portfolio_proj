#imports
from Profile import app,db,bcrypt
from flask import redirect,render_template,url_for,flash,request
from flask import render_template,url_for,flash,redirect,request
from Profile.forms import Registration,Login,Login_via_email,suggestion,Contact_Form
from Profile.models import User
from flask_login import login_user,current_user,logout_user,login_required


#Routes
@app.route('/',methods=['GET','POST'])
def Main():
    return render_template('Welcome_Page.html',title="Welcome to my profile")

@app.route('/basic_details',methods=['GET','POST'])
def Basic_Details():
    if current_user.is_authenticated:
        return render_template('Basic_Details.html',title="Basic_Details")
    else:
        flash(f"You need to login first",'warning')
        return redirect(url_for("login"))


@app.route('/education',methods=['GET','POST'])
def Education():
    if current_user.is_authenticated:
        return render_template('Education.html',title="Educational Details")
    else:
        flash(f"You need to login first",'warning')
        return redirect(url_for("login"))

@app.route('/hobbies',methods=['GET','POST'])
def Hobbies():
    if current_user.is_authenticated:
        return render_template('Hobbies.html',title="Hobbies")
    else:
        flash(f"You need to login first",'warning')
        return redirect(url_for("login"))

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("Main"))
    form=Login()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=form.password.data)
                # flash(f"Welcome {form.username.data}",'info')
                return redirect(url_for('Main'))
            else:
                flash(f"Login Unsuccessful. Please check Username and Password",'danger')
        else:
            flash(f"You don't have an account!",'warning')
    return render_template('login.html',title="Login",form=form) 

@app.route('/login_via_email',methods=['GET','POST'])
def login_via_email():
    if current_user.is_authenticated:
        return redirect(url_for("Hobbies"))
    form=Login_via_email()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=form.password.data)
                flash(f"Welcome {form.email.data}",'info')
                return redirect(url_for('Main'))
            else:
                flash(f"Login Unsuccessful. Please check email and Password",'danger')
        else:
            flash(f"You don't have an account!",'warning')
    return render_template('login_via_email.html',title="Login_via_Email",form=form) 

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("Main"))
    form=Registration()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}! \n You can now log in!",'success')
        # flash(f"You can now log in!",'success')
        return redirect(url_for('login'))        
    return render_template("register.html",form=form,title="Registration")  


@app.route('/contact',methods=['GET','POST'])
def Contact():
    form=Contact_Form()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('Contact.html',title='Contact Me',form=form)

@app.route('/projects',methods=['GET','POST'])
def Project():
    return render_template('Projects.html',title='Projects')


@app.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('Main'))

@app.route('/test',methods=['GET','POST'])
def Test():
    return render_template('test.html',title='test')