from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
import csv
from datetime import datetime
import sqlite3
from pill_my_heart import db
from pill_my_heart.models import Medicine

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def index():

    return render_template('main.html')

@bp.route('/test')
def dbtest():
    reader = csv.reader(open(r'C:\Users\itcam\Downloads\약상세정보1000.csv', 'r', encoding="utf-8"))
    # 엑셀 불러오기
    for row in reader:  # for 반복문을 통하여 DB에 작성
        if row[0] == '':
            print(row)
            continue
        to_db = [(row[1]), (row[2]), (row[3]), (row[4]), (row[5]), (row[6]), (row[7]), (row[8]),(row[9]),(row[10]), (row[11]), (row[12]),
                 (row[13]),(row[14]),(row[15]),(row[16])]
        pill = Medicine(name=to_db[0],
                        medicine_nm=to_db[1],
                        ingredient=to_db[2],
                        additive=to_db[3],
                        doping_now=to_db[4],
                        doping_outside=to_db[5],
                        safety=to_db[6],
                        save=to_db[7],
                        efficacy=to_db[8],
                        usage=to_db[9],
                        Precautions=to_db[10],
                        eat=to_db[11],
                        shape=to_db[12],
                        same=to_db[13],
                        food_Interaction=to_db[14],
                        medicine_Interaction=to_db[15])
        db.session.add(pill)

    db.session.commit()

    return '성공'

@bp.route('/', methods=['GET', 'POST'])
def search_result():
    if request.method == "POST":
        name = request.form.get("id", type=str)
        print(name)
        if name == "":
            flash("검색할 내용을 입력하세요")
            return render_template("main.html")
        elif name == pilldetail_filter(name):
            print("-"*50)
            return render_template('pill/pill_result.html', pill_name=pill_name, pill_ingredient=pill_ingredient,
                                   pill_additive=pill_additive, pill_doping_now=pill_doping_now,
                                   pill_doping_outside=pill_doping_outside, pill_safety=pill_safety,
                                   pill_same=pill_same,
                                   pill_shape=pill_shape, pill_eat=pill_eat, pill_Precautions=pill_Precautions,
                                   pill_usage=pill_usage, pill_efficacy=pill_efficacy, pill_save=pill_save,
                                   pill_food_Interaction=pill_food_Interaction,
                                   pill_medicine_Interaction=pill_medicine_Interaction)
        else:
            flash("검색 결과가 없습니다.")
            return render_template("main.html")

