from pill_my_heart import db

# 유저 정보
class User(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)           # 유저 아이디
    password = db.Column(db.String(200), nullable=False)                        # 비밀번호
    email = db.Column(db.String(120), unique=True, nullable=False)              # 이메일
    birth_year = db.Column(db.Integer)                                          # 태어난 년도
    gender = db.Column(db.String(30))                                           # 성별
    re_dt = db.Column(db.String(500))                                           # 등록일


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# 병 정보
class Medical_Info(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    medical_cd = db.Column(db.String(25))
    medical_nm = db.Column(db.String(255))                # 병명
    re_dt = db.Column(db.String(500))                     # 등록일
    md_dt = db.Column(db.String(500))

#병력 정보
class Medical_History(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    user_seq =db.Column(db.Integer, primary_key=True)      # 유저 시퀸스
    medical_cd = db.Column(db.String(25))
    medical_nm = db.Column(db.String(255))                 # 유저가 적은 병명
    age = db.Column(db.Integer)                            # 나이
    gender = db.Column(db.String)                          # 성별
    re_dt = db.Column(db.String(500))                      # 등록일
    md_dt = db.Column(db.String(500))

# 약 정보
class Medicine_Info(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    medicine_cd = db.Column(db.String(25))
    medicine_nm = db.Column(db.String(255))                # 약품명
    print_front = db.Column(db.String(25))                 # 약 앞면에 있는 내용
    print_back = db.Column(db.String(25))                  # 약 앞면에 있는 내용
    shape = db.Column(db.String(25))                       # 약 제형
    DRUG_SHAPE = db.Column(db.String(25))                  # 약 모양
    color_class1 = db.Column(db.String(25))                # 약 색상(앞면)
    color_class2 = db.Column(db.String(25))                # 약 색상(앞면)
    line_front = db.Column(db.String(25))                  # 약 분할선(앞면)
    line_back = db.Column(db.String(25))                   # 약 분할선(뒷면)
    mark_front = db.Column(db.String(255))                 # 마크 모양(앞면)
    mark_back = db.Column(db.String(255))                  # 마크 모양(뒷면)
    re_dt = db.Column(db.String(500))                      # 등록일
    md_dt = db.Column(db.String(500))                      # 수정일


# 복용약정보
class Medicine_History(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    user_seq =db.Column(db.Integer, primary_key=True)      # 유저 시퀸스
    medicine_cd = db.Column(db.String(25))
    medicine_nm = db.Column(db.String(255))                # 복용약 이름
    age = db.Column(db.Integer)                            # 나이
    gender = db.Column(db.String)                          # 성별
    re_dt = db.Column(db.String(500))                      # 등록일일
    md_dt = db.Column(db.String(500))

# 약 상세정보
class Medicine(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))                        # 이름
    medicine_nm = db.Column(db.String(255))                 # 약품명
    ingredient = db.Column(db.String(255))                  # 성분
    additive = db.Column(db.String(255))                    # 첨가제
    doping_now = db.Column(db.String(255))                  # 경기기간 중 도핑
    doping_outside = db.Column(db.String(255))              # 경기기간 외 도핑
    safety = db.Column(db.String(255))                      # 제품의약안전성
    save = db.Column(db.String(255))                        # 저장방법
    efficacy = db.Column(db.String(255))                    # 효능
    usage = db.Column(db.String(255))                       # 용법
    Precautions = db.Column(db.String(65000))               # 주의사항
    eat = db.Column(db.String(6500))                        # 복약
    shape = db.Column(db.String(255))                       # 약 제형
    same = db.Column(db.String(255))                        # 동일성분
    food_Interaction = db.Column(db.String(255))            # 음식상호작용
    medicine_Interaction = db.Column(db.String(255))        # 약상호작용
    medicine_lmg = db.Column(db.String(300))                # 약 이미지










