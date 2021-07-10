from flask import Blueprint, render_template, jsonify
from athsurveyapp.services.branch_service import get_branches, get_employees

survey_page = Blueprint("survey_page", __name__, template_folder="templates")

@survey_page.route("/surveys", methods=['GET'])
def survey_index():
    return render_template("index.html")

@survey_page.route("/surveys/conduct", methods=['GET', 'POST'])
def conduct_survey():
    
    branches = get_branches()

    return render_template("conduct.html", branches=branches)

@survey_page.route("/surveys/create", methods=['GET', 'POST'])
def create_survey():

    return render_template("createsurvey.html")

@survey_page.route("/employees/<id>")
def get_employees_by_company(id):

    employees = get_employees(id)

    return jsonify(employees)
