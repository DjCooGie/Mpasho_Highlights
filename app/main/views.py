from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_topnews, get_categories, get_newsupdates

 #Views
@main.route('/') 
def index():
     '''
    View root page function that returns the index page and its data
    '''
     #Getting top news and categorically arranged news
     top_articles = get_topnews('google-news')
     print(top_articles)
     biz_articles = get_categories('business')
     tech_articles = get_categories('technology')
     ent_articles = get_categories('entertainment')
     sprt_articles = get_categories('sports')
     title = 'MPasho News'
     return render_template('index.html', title = title, google_news = top_articles, biz = biz_articles, tech = tech_articles, ent = ent_articles, sprt = sprt_articles)


@main.route('/update/<id>')
def article(id):
    detz_articles = get_newsupdates(id)
    print(detz_articles)
    return render_template('news.html',detz = detz_articles)