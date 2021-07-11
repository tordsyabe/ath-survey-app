from flask import Blueprint, render_template, request, redirect
from flask.helpers import url_for
from athsurveyapp.models.models import Branch, db

branch_page = Blueprint('branch_page', __name__, template_folder='templates')


@branch_page.route('/', methods=['GET'])
def branch_index():
    return render_template('branches.html')


@branch_page.route('/create', methods=['GET', 'POST'])
def create_branch():

    if request.method == 'POST':
        branch_name = request.form['name']
        branch_address = request.form['address']

        new_branch = Branch(branch_name, branch_address)
        db.session.add(new_branch)
        db.session.commit()

        return redirect(url_for('branch_page.branch_index'))

    return render_template('create_branch.html')
