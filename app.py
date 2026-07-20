from flask import Flask, render_template, request, send_file
import os

from analyzer import analyze_data
from charts import generate_charts
from ai_assistant import ask_ai
from insights import generate_insights
from report_generator import generate_report

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {"csv", "xlsx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

current_summary = None
current_charts = None
current_insights = None
current_filepath = None
current_answer = None


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():

    global current_summary
    global current_charts
    global current_insights
    global current_filepath
    global current_answer

    file = request.files["dataset"]

    if file.filename == "":

        return "Please select a file."

    if not allowed_file(file.filename):

        return "Only CSV and Excel files are allowed."

    current_answer = None

    current_filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(current_filepath)

    try:

        current_summary = analyze_data(
            current_filepath
        )

        current_charts = generate_charts(
            current_filepath
        )

        current_insights = generate_insights(
            current_filepath
        )

    except Exception as e:

        return f"Error while reading the file: {str(e)}"

    return render_template(

        "result.html",

        summary=current_summary,

        charts=current_charts,

        insights=current_insights,

        answer=current_answer
    )


@app.route("/ask", methods=["POST"])
def ask():

    global current_summary
    global current_charts
    global current_insights
    global current_filepath
    global current_answer

    if current_summary is None:

        return "Please upload a dataset first."

    question = request.form["question"]

    current_answer = ask_ai(

        current_filepath,

        current_summary,

        question

    )

    return render_template(

        "result.html",

        summary=current_summary,

        charts=current_charts,

        insights=current_insights,

        answer=current_answer
    )


@app.route("/download-report")
def download_report():

    filename = generate_report(

        current_summary,

        current_insights,

        current_answer

    )

    return send_file(

        filename,

        as_attachment=True

    )


if __name__ == "__main__":

    app.run(debug=True)