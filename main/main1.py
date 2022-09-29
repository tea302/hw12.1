import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import search_posts_by_word

home_blueprint = Blueprint('home_blueprint', __name__, template_folder='templates')


@home_blueprint.route('/')
def home_page():
    return render_template("index.html")


@home_blueprint.route('/search/')
def search_page():
    search_query = request.args.get("s", '')
    logging.info('Выполняю поиск')
    try:
        posts = search_posts_by_word(search_query)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template("post_list.html", query=search_query, posts=posts)
