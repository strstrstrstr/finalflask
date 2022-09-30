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
    pilldetail=pilldetail_filter("아네모정")
    pill_name = pilldetail.medicine_nm
    pill_ingredient = pilldetail.ingredient
    pill_additive = pilldetail.additive
    pill_doping_now = pilldetail.doping_now
    pill_doping_outside = pilldetail.doping_outside
    pill_safety = pilldetail.safety
    pill_save = pilldetail.save
    pill_efficacy = pilldetail.efficacy
    pill_usage = pilldetail.usage
    pill_Precautions = pilldetail.Precautions
    pill_eat = pilldetail.eat
    pill_shape = pilldetail.shape
    pill_same = pilldetail.same
    pill_food_Interaction = pilldetail.food_Interaction
    pill_medicine_Interaction = pilldetail.medicine_Interaction


    return render_template('pill/pill_result.html', pill_name = pill_name, pill_ingredient = pill_ingredient, pill_additive = pill_additive, pill_doping_now=pill_doping_now, pill_doping_outside=pill_doping_outside, pill_safety=pill_safety, pill_same=pill_same, pill_shape=pill_shape, pill_eat=pill_eat, pill_Precautions=pill_Precautions, pill_usage=pill_usage, pill_efficacy=pill_efficacy, pill_save=pill_save, pill_food_Interaction=pill_food_Interaction, pill_medicine_Interaction=pill_medicine_Interaction)

@bp.route('/pill_warning/', methods=('GET', 'POST'))
def warning():
    pilldetail = pilldetail_filter("아네모정")
    pill_name = pilldetail.medicine_nm
    pill_ingredient = pilldetail.ingredient
    pill_additive = pilldetail.additive
    pill_doping_now = pilldetail.doping_now
    pill_doping_outside = pilldetail.doping_outside
    pill_safety = pilldetail.safety
    pill_save = pilldetail.save
    pill_efficacy = pilldetail.efficacy
    pill_usage = pilldetail.usage
    pill_Precautions = pilldetail.Precautions
    pill_eat = pilldetail.eat
    pill_shape = pilldetail.shape
    pill_same = pilldetail.same
    pill_food_Interaction = pilldetail.food_Interaction
    pill_medicine_Interaction = pilldetail.medicine_Interaction
    return  render_template('pill/pill_warning.html', pill_Precautions=pill_Precautions, pill_eat=pill_eat, pill_medicine_Interaction=pill_medicine_Interaction, pill_same=pill_same)

@bp.route('/pill_not_result/', methods=('GET', 'POST'))
def not_result():
    queryset=Medicine.query.filter(Medicine.name.like('%아%')).all()
    return render_template('pill/pill_not_result.html', queryset=queryset)

@bp.route('/pill_name_search', methods=["POST"])
def pill_name_search():
    pillname = request.form["id"]
    pilldetail = pilldetail_filter(pillname)
    if not pilldetail == None:
        pill_name = pilldetail.medicine_nm
        pill_ingredient = pilldetail.ingredient
        pill_additive = pilldetail.additive
        pill_doping_now = pilldetail.doping_now
        pill_doping_outside = pilldetail.doping_outside
        pill_safety = pilldetail.safety
        pill_save = pilldetail.save
        pill_efficacy = pilldetail.efficacy
        pill_usage = pilldetail.usage
        pill_Precautions = pilldetail.Precautions
        pill_eat = pilldetail.eat
        pill_shape = pilldetail.shape
        pill_same = pilldetail.same
        pill_food_Interaction = pilldetail.food_Interaction
        pill_medicine_Interaction = pilldetail.medicine_Interaction


        return render_template('pill/pill_result.html', pill_name = pill_name, pill_ingredient = pill_ingredient, pill_additive = pill_additive, pill_doping_now=pill_doping_now, pill_doping_outside=pill_doping_outside, pill_safety=pill_safety, pill_same=pill_same, pill_shape=pill_shape, pill_eat=pill_eat, pill_Precautions=pill_Precautions, pill_usage=pill_usage, pill_efficacy=pill_efficacy, pill_save=pill_save, pill_food_Interaction=pill_food_Interaction, pill_medicine_Interaction=pill_medicine_Interaction)
    elif pilldetail == '':
        flash('검색결과가 없습니다.')
        return render_template('main.html')
    else:
        flash('검색결과가 없습니다.')
        return render_template('main.html')






