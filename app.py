from flask import Flask, render_template

# 웹 서버 역할 Flask App
app = Flask(__name__)

# 라우팅
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/page/')
def go_page():
    return render_template("page.html")

# App 가동
if __name__ == "__main__":
    app.run(debug=True, port=5001)