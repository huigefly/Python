from flask import Flask
import os

#from flask import render_template

app = Flask (__name__)

@app.route("/")
def hello():    
	return "helloworld" 

@app.route("/btn")
def test():
	return app.send_static_file("index.html")

@app.route("/btn2")
def btn2():
    rtn=os.popen('ls -l').read()
    return rtn
if __name__ == "__main__":
    app.run(host='0.0.0.0')
