from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import Sources

# views
@main.route('/')
def index():
    '''
    view root page function that returns the index of the page and its data
    '''
    highlights_sources = get_sources('highlights')
    title = "KNN"

    return render_template('index.html', title=title, highlights_sources=highlights_sources)


@main.route('/sources/<id>')
def articles(id):
    '''
    view articles page
    '''
    articles = get_articles(id)
    title = {id}
    return render_template('articles.html', title=title, articles=articles)
