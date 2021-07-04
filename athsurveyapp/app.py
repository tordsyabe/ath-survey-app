from flask import Flask

from athsurveyapp.blueprints.survey import survey_page


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    app.register_blueprint(survey_page)

    return app
