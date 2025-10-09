#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return (
        "This is a sample Flask application.<br>"
        "I am Albert — thank you for visiting!<br><br>"
        "This app is part of a simple CI/CD pipeline demo "
        "to show how a web service can be built, tested, and deployed automatically."
    )

def main():
    print("=== Welcome to Albert Jerald’s Flask App ===\n")
    paragraph = (
        "This is a simple Python + Flask application used for CI/CD pipeline testing. "
        "It demonstrates how code can be automatically built and deployed using DevOps tools. "
        "Flask is a lightweight web framework that helps create web applications quickly. "
        "By integrating Flask into a CI/CD pipeline, you can automate deployments "
        "and continuously deliver updates efficiently."
    )
    print(paragraph)

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=5000)

