from filter_fun import pilldetail_filter, pillname_filter
from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect,secure_filename
from datetime import datetime
import os
from pill_my_heart import db
from pill_my_heart.forms import UserCreateForm, UserLoginForm
from pill_my_heart.models import User, Medicine

bp = Blueprint('pill_search', __name__, url_prefix='/')


@bp.route('/pill_search')
def pill_search():
    return render_template('pill/pill_search.html' )

@bp.route('/pill_result/', methods=["POST"])
def result():
    uploaded_file1 = request.files['file1']
    uploaded_file2 = request.files['file2']


    # print(uploaded_file1)
    # uploaded_file1.save(
    #     os.path.join(r'C:\testproject\pill_my_heart\uploadimg\\'+secure_filename(uploaded_file1.filename)))
    # uploaded_file2.save(
    #     os.path.join(r'C:\testproject\pill_my_heart\uploadimg\\' + secure_filename(uploaded_file2.filename)))
    #
    #
    # img1=cv2.imread(os.path.join(r'C:\testproject\pill_my_heart\uploadimg\\'+secure_filename(uploaded_file1.filename)))
    # img2 = cv2.imread(os.path.join(r'C:\testproject\pill_my_heart\uploadimg\\' + secure_filename(uploaded_file2.filename)))
    # img_pa1=RESHAPE_PADDING(img1)
    # img_pa2=RESHAPE_PADDING(img2)
    # cv2.imwrite('01.jpg', img_pa1)
    # cv2.imwrite('02.jpg', img_pa2)
    # result_front=CNN_FUN(img_pa1)
    # result_back=CNN_FUN(img_pa2)
    # print(result_front)
    # side1= {'PRINT':'BSS','DRUG_SHAPE':result_front['DRUG_SHAPE'],'COLOR_CLASS':result_front['COLOR_CLASS'],'LINE':result_front['LINE'],'SHAPE':result_front['SHAPE_CODE'],'MARK_CODE':'Default'}
    # side2= {'PRINT':'Default','DRUG_SHAPE':result_front['DRUG_SHAPE'],'COLOR_CLASS':result_front['COLOR_CLASS'],'LINE':result_front['LINE'],'SHAPE':result_front['SHAPE_CODE'],'MARK_CODE':'Default'}
    # pillname=pillname_filter(side1, side2)[0].medicine_nm
    queryset = Medicine.query.filter(Medicine.name.like('%아네모정%'))

    return render_template('pill/pill_not_result.html', queryset=queryset)

@bp.route('/pill_warning/', methods=('GET', 'POST'))
def warning():

    queryset = Medicine.query.filter(Medicine.name.like('%아네모정%')).all()[0]
    return  render_template('pill/pill_warning.html', queryset=queryset)

@bp.route('/pill_not_result/', methods=('GET', 'POST'))
def not_result():
    queryset=Medicine.query.filter(Medicine.name.like('%아%')).all()
    return render_template('pill/pill_not_result.html', queryset=queryset)

@bp.route('/pill_name_search', methods=["POST"])
def pill_name_search():
    pillname = request.form["id"]
    queryset=Medicine.query.filter(Medicine.name.like('%'+pillname+'%')).all()
    for query in queryset:
        if not query == None:
            return render_template('pill/pill_not_result.html', queryset=queryset)
        elif pilldetail == '':
            flash('검색결과가 없습니다.')
            return render_template('main.html')
        else:
            flash('검색결과가 없습니다.')
            return render_template('main.html')

@bp.route('/detail/<int:query_id>/')
def pill_id_search(query_id):
    query=Medicine.query.filter(Medicine.seq==query_id).all()[0]
    return render_template('pill/pill_result.html', query=query)






