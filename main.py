from flask import Flask
import subprocess

app = Flask(__name__)

version = subprocess.check_output(["git", "reflog", "--date=iso"]).strip().decode().split('\n')[0]

@app.route('/')
def hello_world():
    return version
