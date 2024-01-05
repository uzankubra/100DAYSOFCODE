from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number=random.randint(1,10)
    current_year=datetime.datetime.now().year
    return render_template("index.html")

@app.route("/guess/<username>")
def guess(username):
    gender_url=f"https://api.genderize.io?name={username}"
    gender_response=requests.get(gender_url)
    gender=gender_response.json()["gender"]

    age_url=f"https://api.agify.io?name={username}"
    age_response=requests.get(age_url)
    age=age_response.json()["age"]

    return render_template("guess.html", name=username, gender=gender, age=age)

@app.route("/blog")
def get_blog():
    blog_url="https://api.npoint.io/5abcca6f4e39b4955965"
    repsonse=requests.get(blog_url)
    all_posts=repsonse.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)