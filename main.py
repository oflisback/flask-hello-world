from flask import Flask
import subprocess
import sys

try:
    with open('./version.txt', 'r') as file:
        version = file.read().replace('\n', '')
except OSError:
    print("Could not open version.txt, did you run build.sh?")
    sys.exit()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return version

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
