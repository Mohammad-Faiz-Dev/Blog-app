from http.client import responses

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.npoint.io/971c9cfc653c1062838f"
    response = requests.get(url)
    data = response.json()
    blog_1 = next((post["title"] for post in data if post["id"] == 1), None)
    blog_1_sub = next((post["subtitle"] for post in data if post["id"] == 1), None)
    blog_2 = next((post["title"] for post in data if post["id"] == 2), None)
    blog_2_sub = next((post["subtitle"] for post in data if post["id"] == 2), None)
    blog_3 = next((post["title"] for post in data if post["id"] == 3), None)
    blog_3_sub = next((post["subtitle"] for post in data if post["id"] == 3), None)
    return render_template('home.html', blog_1=blog_1, blog_1_sub=blog_1_sub, blog_2=blog_2, blog_2_sub=blog_2_sub, blog_3=blog_3, blog_3_sub=blog_3_sub)

@app.route('/blog/1')
def blog1():
    url = "https://api.npoint.io/971c9cfc653c1062838f"
    response = requests.get(url)
    data = response.json()
    blog_1_title = next((post["title"] for post in data if post["id"] == 1), None)
    blog_1 = next((post["body"] for post in data if post["id"] == 1), None)
    blog_1_subtitle = next((post["subtitle"] for post in data if post["id"] == 1), None)
    return render_template('blog_1.html', blog_1=blog_1, blog_1_subtitle=blog_1_subtitle, blog_1_title=blog_1_title)

@app.route('/blog/2')
def blog2():
    url = "https://api.npoint.io/971c9cfc653c1062838f"
    response = requests.get(url)
    data = response.json()
    blog_2_title = next((post["title"] for post in data if post["id"] == 2), None)
    blog_2_subtitle = next((post["subtitle"] for post in data if post["id"] == 2), None)
    blog_2 = next((post["body"] for post in data if post["id"] == 2), None)
    return render_template('blog_2.html', blog_2=blog_2, blog_2_subtitle=blog_2_subtitle, blog_2_title=blog_2_title)

@app.route('/blog/3')
def blog3():
    url = "https://api.npoint.io/971c9cfc653c1062838f"
    response = requests.get(url)
    data = response.json()  # ✅ correct usage
    blog_3_title = next((post["title"] for post in data if post["id"] == 3), None)
    blog_3_subtitle = next((post["subtitle"] for post in data if post["id"] == 3), None)
    blog_3 = next((post["body"] for post in data if post["id"] == 3), None)
    return render_template('blog_3.html', blog_3=blog_3, blog_3_subtitle=blog_3_subtitle, blog_3_title=blog_3_title)


if __name__ == "__main__":
    app.run(debug=True)