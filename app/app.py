#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return (
        "This is a sample Flask application.<br>"
        "I am Albert Jerald — thank you for visiting!<br><br>"
        "This app is part of a simple CI/CD pipeline demo "
    )

def main():
    print("=== Welcome to Albert Jerald’s Flask App ===\n")
    paragraph = (
        "I'm Albert Jerald "
        "I'm open for new opportunities. I'm practicing AWS and Devops tools "
        "I have hands-on experience on AWS, Linux, Git, Jenkins, Docker and practical knowledge on Ansible and Terraform. "
        "Contact my Email: albertjerald19@gmail.com  "
        "Contact my Mobile Number : 8939263846/ 8072545136"
    )
    print(paragraph)

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=5000)

