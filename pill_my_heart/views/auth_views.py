from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from datetime import datetime
import sqlite3
from pill_my_heart import db
from pill_my_heart.forms import UserCreateForm, UserLoginForm
from pill_my_heart.models import User, Medical_History, Medicine_History

bp = Blueprint('auth', __name__, url_prefix='/auth')

conn=sqlite3.connect("pybo.db",check_same_thread=False)
cur=conn.cursor()

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data,
                        birth_year=form.birth_year.data,
                        gender=form.gender.data,
                        re_dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        )
            db.session.add(user)
            db.session.commit()

            medical_history = Medical_History(age=form.birth_year.data,
                                                gender=form.gender.data,
                                                re_dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                medical_nm=form.medical_nm.data)
            medicine_history = Medicine_History(age=form.birth_year.data,
                                                gender=form.gender.data,
                                                re_dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                medicine_nm=form.medicine_nm.data)
            db.session.add(medical_history)
            db.session.add(medicine_history)
            db.session.commit()

            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.username
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/address.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(username=user_id).first()
        # g.user = User.query.get(user_id)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))