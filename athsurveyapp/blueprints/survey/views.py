from flask import Blueprint, render_template, jsonify
# from athsurveyapp.services.branch_service import get_branches, get_employees

survey_page = Blueprint("survey_page", __name__, template_folder="templates")


@survey_page.route("/", methods=['GET'])
def survey_index():
    return render_template("surverys.html")


@survey_page.route("/create", methods=['GET', 'POST'])
def create_survey():

    return render_template("create_survey.html")

# @survey_page.route("/conduct", methods=['GET', 'POST'])
# def conduct_survey():

#     branches = get_branches()

#     return render_template("conduct_survey.html", branches=branches)


# @survey_page.route("/employees/<id>")
# def get_employees_by_company(id):

#     employees = get_employees(id)

#     return jsonify(employees)
