from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors # views, errors: the whole modules
