from flask import Blueprint, render_template

survey_page = Blueprint("survey_page", __name__, template_folder="templates")

@survey_page.route("/surveys", methods=['GET'])
def survey_index():
    return render_template("index.html")

@survey_page.route("/surveys/conduct", methods=['GET', 'POST'])
def conduct_survey():
    return render_template("conduct.html")
