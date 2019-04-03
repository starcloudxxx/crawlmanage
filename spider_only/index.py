# -*- coding=utf-8 -*-
import re

from flask import Blueprint, render_template, flash, request
from flask import current_app as app

from .vars import INFO, WARN,TEMPLATE_INDEX, NAVI_NAME
from .utils import make_request

bp = Blueprint('index', __name__, url_prefix='/')
check_latest_version = True

@bp.route('/')
@bp.route('/index/')
def index():
    """
        params:
        node: navi显示的主要类型序号 
    """
    TEMPLATE = TEMPLATE_INDEX
    title = "欢迎"

    navis = NAVI_NAME

    return render_template(TEMPLATE, title=title, navis=navis)

 