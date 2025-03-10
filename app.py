from flask import Flask,render_template,jsonify
from database import laod_jobs_from_db


app=Flask(__name__)

@app.route("/")
def hello_world():
    jobs=laod_jobs_from_db()
    return render_template('home.html',jobs=jobs)

if __name__=="__main__":
    app.run(debug=True)

  