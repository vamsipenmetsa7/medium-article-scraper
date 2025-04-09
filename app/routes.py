from flask import render_template, request
from app import app
from app.scraper import scrape_medium_headers_with_titles

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        article_url = request.form.get("article_url")
        headers_data = scrape_medium_headers_with_titles(article_url)
        return render_template("index.html", headers_data=headers_data, article_url=article_url)
    return render_template("index.html", headers_data=None)