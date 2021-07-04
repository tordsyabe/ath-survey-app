from flask import Blueprint, render_template

survery_page = Blueprint("survery_page", __name__, template_folder="templates")

@survery_page.route("/surveys")
def survery_index():
    return render_template("index.html")
