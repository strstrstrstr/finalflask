from flask import Blueprint, render_template, url_for
from pill_my_heart.models import Question
from werkzeug.utils import redirect
import folium

bp = Blueprint('address', __name__, url_prefix='/')


@bp.route('/address/', methods=('GET', 'POST'))
def index():

    return render_template('address/address.html', latitude=37.5285568, longitude=126.8885657 )