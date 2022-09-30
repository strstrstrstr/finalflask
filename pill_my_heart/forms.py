from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    gender = StringField('성별', validators=[DataRequired()])
    birth_year = StringField('나이', validators=[DataRequired()])
    re_dt = StringField('등록일자', validators=[DataRequired()])
    medical_cd = StringField('의학코드')
    medical_nm = StringField('병명', validators=[DataRequired()])
    medicine_nm = StringField('약품명', validators=[DataRequired()])
    medicine_cd = StringField('약품 코드')
    user_seq = StringField('유저시퀸스')



class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])



