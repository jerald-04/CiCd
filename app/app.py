#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return (
        "This is a sample Flask application.<br>"
        "I am Albert Jerald — thank you for visiting!<br><br>"
        "This app is part of a simple CI/CD pipeline demo <br><br><br>"
        "Hi, I'm Albert Jerald <br><br>"
        "I'm practicing AWS and Devops tools <br>"
        "I have used AWS EC2, Linux, Git, Jenkins, Docker for this demo.<br> "
	"I'm planning to use Ansible, Terraform and Kubernetes in upcoming project.<br>"
        "Contact my Email: albertjerald19@gmail.com  <br>"
        "Contact my Mobile Number : 8939263846/ 8072545136"
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

