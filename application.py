from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def show_form():
    """Show a form for the applicant to fill out."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def get_applicant_details():
    """Get applicant's details."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary_requirements = request.form.get("salary")
    job_title = request.form.get("title")

    return render_template("application-response.html",
                            first=first_name,
                            last=last_name,
                            salary=salary_requirements,
                            title=job_title)


@app.route("/application-response", methods=["GET"])
def show_applicant_details():
    """Return a response to the applicant regarding their input."""

    return render_template("application-response.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
