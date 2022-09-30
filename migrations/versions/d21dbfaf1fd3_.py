"""empty message

Revision ID: d21dbfaf1fd3
Revises: 
Create Date: 2022-09-29 11:46:00.754963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd21dbfaf1fd3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medical__history',
    sa.Column('seq', sa.Integer(), nullable=False),
    sa.Column('user_seq', sa.Integer(), nullable=False),
    sa.Column('medical_cd', sa.String(length=25), nullable=True),
    sa.Column('medical_nm', sa.String(length=255), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('re_dt', sa.String(length=500), nullable=True),
    sa.Column('md_dt', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('seq', 'user_seq')
    )
    op.create_table('medical__info',
    sa.Column('seq', sa.Integer(), nullable=False),
    sa.Column('medical_cd', sa.String(length=25), nullable=True),
    sa.Column('medical_nm', sa.String(length=255), nullable=True),
    sa.Column('re_dt', sa.String(length=500), nullable=True),
    sa.Column('md_dt', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('seq')
    )
    op.create_table('medicine',
    sa.Column('seq', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('medicine_nm', sa.String(length=255), nullable=True),
    sa.Column('ingredient', sa.String(length=255), nullable=True),
    sa.Column('additive', sa.String(length=255), nullable=True),
    sa.Column('doping_now', sa.String(length=255), nullable=True),
    sa.Column('doping_outside', sa.String(length=255), nullable=True),
    sa.Column('safety', sa.String(length=255), nullable=True),
    sa.Column('save', sa.String(length=255), nullable=True),
    sa.Column('efficacy', sa.String(length=255), nullable=True),
    sa.Column('usage', sa.String(length=255), nullable=True),
    sa.Column('Precautions', sa.String(length=65000), nullable=True),
    sa.Column('eat', sa.String(length=6500), nullable=True),
    sa.Column('shape', sa.String(length=255), nullable=True),
    sa.Column('same', sa.String(length=255), nullable=True),
    sa.Column('food_Interaction', sa.String(length=255), nullable=True),
    sa.Column('medicine_Interaction', sa.String(length=255), nullable=True),
    sa.Column('medicine_lmg', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('seq')
    )
    op.create_table('medicine__history',
    sa.Column('seq', sa.Integer(), nullable=False),
    sa.Column('user_seq', sa.Integer(), nullable=False),
    sa.Column('medicine_cd', sa.String(length=25), nullable=True),
    sa.Column('medicine_nm', sa.String(length=255), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('re_dt', sa.String(length=500), nullable=True),
    sa.Column('md_dt', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('seq', 'user_seq')
    )
    op.create_table('medicine__info',
    sa.Column('seq', sa.Integer(), nullable=False),
    sa.Column('medicine_cd', sa.String(length=25), nullable=True),
    sa.Column('medicine_nm', sa.String(length=255), nullable=True),
    sa.Column('print_front', sa.String(length=25), nullable=True),
    sa.Column('print_back', sa.String(length=25), nullable=True),
    sa.Column('shape', sa.String(length=25), nullable=True),
    sa.Column('DRUG_SHAPE', sa.String(length=25), nullable=True),
    sa.Column('color_class1', sa.String(length=25), nullable=True),
    sa.Column('color_class2', sa.String(length=25), nullable=True),
    sa.Column('line_front', sa.String(length=25), nullable=True),
    sa.Column('line_back', sa.String(length=25), nullable=True),
    sa.Column('mark_front', sa.String(length=255), nullable=True),
    sa.Column('mark_back', sa.String(length=255), nullable=True),
    sa.Column('re_dt', sa.String(length=500), nullable=True),
    sa.Column('md_dt', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('seq')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('seq', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=30), nullable=True),
    sa.Column('re_dt', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('seq'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    op.drop_table('user')
    op.drop_table('question')
    op.drop_table('medicine__info')
    op.drop_table('medicine__history')
    op.drop_table('medicine')
    op.drop_table('medical__info')
    op.drop_table('medical__history')
    # ### end Alembic commands ###