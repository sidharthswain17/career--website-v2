from flask import Flask,render_template,jsonify,url_for,request
from database import laod_jobs_from_db,load_job_from_db,insert_to_db


app=Flask(__name__)

@app.route("/")
def hello_world():
    jobs=laod_jobs_from_db()
    return render_template('home.html',jobs=jobs)

@app.route("/job/<int:id>")
def show_job(id):
    job =load_job_from_db(id)
    if not job:
        return "Job not found",404
    return render_template('job_page.html',job=job)

@app.route("/job/<int:id>/apply",methods=["POST"])
def apply_to_job(id):
    data=request.form
    job=load_job_from_db(id)
    # return jsonify(data)
    insert_to_db(data, id)
    return render_template("application.html",application=data,job=job)



if __name__=="__main__":
    app.run(debug=True)

  