from flask import Blueprint, url_for, render_template, request
from werkzeug.utils import redirect
from werkzeug.utils import secure_filename
import csv

from flask import app

from pill_my_heart import db
from pill_my_heart.models import Medicine_Info,Medicine
# from pill_my_heart.models import Question

from sqlalchemy import and_,or_
import os


def pillname_filter(side1, side2): # 정보 없음 처리해줘야할 것들...
    # side1= {'PRINT':'BSS','DRUG_SHAPE':'원형','COLOR_CLASS':'분홍','LINE':'Default','SHAPE':'','MARK_CODE':'Default'}
    # side2= {'PRINT':'Default','DRUG_SHAPE':'원형','COLOR_CLASS':'분홍','LINE':'Default','SHAPE':'','MARK_CODE':'Default'}
    if len(side1['COLOR_CLASS'].split(','))==1: # 컬러 하나일 때
        queries = Medicine_Info.query.filter(and_(or_(and_(Medicine_Info.print_front==side1['PRINT'],Medicine_Info.print_back==side2['PRINT']),and_(Medicine_Info.print_front==side2['PRINT'],Medicine_Info.print_back==side1['PRINT'])),
                                    and_(Medicine_Info.DRUG_SHAPE==side1['DRUG_SHAPE'],Medicine_Info.DRUG_SHAPE==side2['DRUG_SHAPE']),
                                    or_(and_(Medicine_Info.color_class1==side1['COLOR_CLASS'],Medicine_Info.color_class2=='Default'),and_(Medicine_Info.color_class2==side1['COLOR_CLASS'],Medicine_Info.color_class1=='Default')),
                                    or_(and_(Medicine_Info.line_front==side1['LINE'],Medicine_Info.line_back==side2['LINE']),and_(Medicine_Info.line_front==side2['LINE'],Medicine_Info.line_back==side1['LINE'])),
                                    or_(and_(Medicine_Info.mark_front==side1['MARK_CODE'],Medicine_Info.mark_back==side2['MARK_CODE']),and_(Medicine_Info.mark_front==side2['MARK_CODE'],Medicine_Info.mark_back==side1['MARK_CODE'])),
                                    and_(Medicine_Info.shape == side1['SHAPE'], Medicine_Info.shape == side2['SHAPE']),
                                         )).all()
        if queries.len()==0:
            queries = Medicine_Info.query.filter(and_(
                or_(and_(Medicine_Info.print_front == side1['PRINT'], Medicine_Info.print_back == side2['PRINT']),
                    and_(Medicine_Info.print_front == side2['PRINT'], Medicine_Info.print_back == side1['PRINT'])),
                or_(Medicine_Info.DRUG_SHAPE == side1['DRUG_SHAPE'], Medicine_Info.DRUG_SHAPE == side2['DRUG_SHAPE']),
                or_(and_(Medicine_Info.color_class1 == side1['COLOR_CLASS'], Medicine_Info.color_class2 == 'Default'),
                    and_(Medicine_Info.color_class2 == side1['COLOR_CLASS'], Medicine_Info.color_class1 == 'Default')),
                or_(and_(Medicine_Info.line_front == side1['LINE'], Medicine_Info.line_back == side2['LINE']),
                    and_(Medicine_Info.line_front == side2['LINE'], Medicine_Info.line_back == side1['LINE'])),

                )).all() # 식별문자, 모양, 색, 분할선
            if queries.len()==0:
                queries = Medicine_Info.query.filter(and_(
                    or_(and_(Medicine_Info.print_front == side1['PRINT'], Medicine_Info.print_back == side2['PRINT']),
                        and_(Medicine_Info.print_front == side2['PRINT'], Medicine_Info.print_back == side1['PRINT'])),
                    or_(Medicine_Info.DRUG_SHAPE == side1['DRUG_SHAPE'], Medicine_Info.DRUG_SHAPE == side2['DRUG_SHAPE']),
                )).all() # 식별문자, 모양

        return queries

    if len(side1['COLOR_CLASS'].split(','))>=2: # 컬러 두 개일 때
        queries = Medicine_Info.query.filter(and_(or_(and_(Medicine_Info.print_front==side1['PRINT'],Medicine_Info.print_back==side2['PRINT']),and_(Medicine_Info.print_front==side2['PRINT'],Medicine_Info.print_back==side1['PRINT'])),
                                    and_(Medicine_Info.DRUG_SHAPE==side1['DRUG_SHAPE'],Medicine_Info.DRUG_SHAPE==side2['DRUG_SHAPE']),
                                    or_(and_(Medicine_Info.color_class1==side1['COLOR_CLASS'].split(',')[0],Medicine_Info.color_class2==side1['COLOR_CLASS'].split(',')[1]),and_(Medicine_Info.color_class2==side1['COLOR_CLASS'].split(',')[1],side1['COLOR_CLASS'].split(',')[0])),
                                    or_(and_(Medicine_Info.line_front==side1['LINE'],Medicine_Info.line_back==side2['LINE']),and_(Medicine_Info.line_front==side2['LINE'],Medicine_Info.line_back==side1['LINE'])),
                                    or_(and_(Medicine_Info.mark_front==side1['MARK_CODE'],Medicine_Info.mark_back==side2['MARK_CODE']),and_(Medicine_Info.mark_front==side2['MARK_CODE'],Medicine_Info.mark_back==side1['MARK_CODE'])),
                                    and_(Medicine_Info.shape == side1['SHAPE'], Medicine_Info.shape == side2['SHAPE']),
                                         )).all()
        if queries.len()==0:
            queries = Medicine_Info.query.filter(and_(
                or_(and_(Medicine_Info.print_front == side1['PRINT'], Medicine_Info.print_back == side2['PRINT']),
                    and_(Medicine_Info.print_front == side2['PRINT'], Medicine_Info.print_back == side1['PRINT'])),
                and_(Medicine_Info.DRUG_SHAPE == side1['DRUG_SHAPE'], Medicine_Info.DRUG_SHAPE == side2['DRUG_SHAPE']),
                or_(and_(Medicine_Info.color_class1 == side1['COLOR_CLASS'].split(',')[0],
                         Medicine_Info.color_class2 == side1['COLOR_CLASS'].split(',')[1]),
                    and_(Medicine_Info.color_class2 == side1['COLOR_CLASS'].split(',')[1], side1['COLOR_CLASS'].split(',')[0])),
                or_(and_(Medicine_Info.line_front == side1['LINE'], Medicine_Info.line_back == side2['LINE']),
                    and_(Medicine_Info.line_front == side2['LINE'], Medicine_Info.line_back == side1['LINE'])),

                )).all()

            if queries.len() == 0:
                queries = Medicine_Info.query.filter(and_(
                    or_(and_(Medicine_Info.print_front == side1['PRINT'], Medicine_Info.print_back == side2['PRINT']),
                        and_(Medicine_Info.print_front == side2['PRINT'], Medicine_Info.print_back == side1['PRINT'])),
                    and_(Medicine_Info.DRUG_SHAPE == side1['DRUG_SHAPE'], Medicine_Info.DRUG_SHAPE == side2['DRUG_SHAPE']),
                )).all()

        return queries


def pilldetail_filter(name):
    try:
        detail=Medicine.query.filter(Medicine.name==name)[0]
        return detail

    except:
        return None
