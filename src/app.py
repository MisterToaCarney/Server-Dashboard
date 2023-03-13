from flask import Flask, render_template
import subprocess

app = Flask(__name__)

def run_command(command):
    try: output = subprocess.check_output(["sh", "-c", command]).decode()
    except Exception as e: output = "Error: " + str(e)
    return(output)


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

    md_detail = run_command("mdadm --detail /dev/md0")
    sensors = run_command("sensors")
    hddtemp = run_command("hddtemp")
    smb_status = run_command("smbstatus")
    net_connections = run_command("netstat | grep ESTABLISHED")


    return render_template(
        "status.html",
        mdstat_output=mdstat_output,
        md_detail_output=md_detail,
        sensors=sensors,
        hddtemp=hddtemp,
        smb_status=smb_status,
        net_connections=net_connections,
    )