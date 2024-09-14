from flask import Flask, render_template, request
from redaction import redact_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    redacted_text = ""
    if request.method == "POST":
        # Get the text from user input
        text = request.form.get("input_text")
        redaction_type = request.form.get("redaction_type")
        
        # Perform redaction
        redacted_text = redact_text(text, redaction_type)

    return render_template("index.html", redacted_text=redacted_text)

if __name__ == "__main__":
    app.run(debug=True)
