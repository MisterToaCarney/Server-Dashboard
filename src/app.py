from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hello.html")

@app.route("/status")
def status():
    try:
        with open("/proc/mdstat", "r") as f:
            mdstat_output = f.read()
    except Exception as e:
        mdstat_output = "Error: Cannot open /proc/mdstat"
        mdstat_output += "\n" + str(e)
    return render_template("status.html", mdstat_output=mdstat_output)