from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")

@app.route("/application-form")
def job_application():
    
    return render_template("application-form.html")

@app.route("/application-success")
def application_success():
    firstname = request.args.get("first name")
    lastname = request.args.get("last name")
    salary = request.args.get("salary")
    job = request.args.get("job type")
    return render_template("application-response.html",
        first_name=firstname,
        last_name=lastname,
        salary=salary,
        job=job)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
