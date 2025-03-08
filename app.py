from flask import Flask,render_template,jsonify
from database import laod_jobs_from_db


app=Flask(__name__)
# jobs = [
#     {
#         'id': 1,
#         'title': 'Data Analyst',
#         'location': 'Bangalore',
#         'salary': 'Rs 12,00,000'
#     },
#     {
#         'id': 2,
#         'title': 'Data Scientist',
#         'location': 'Delhi',
#         'salary': 'Rs 22,00,000'
#     },
#     {
#         'id': 3,
#         'title': 'Frontend Engineer',
#         'location': 'Bangalore',
#         'salary': 'Rs 2,00,000'
#     },
#     {
#         'id': 4,
#         'title': 'Backend Engineer',
#         'location': 'Bangalore',
#         'salary': 'Rs 15,00,000'
#     }
# ]

    
 

@app.route("/")
def hello_world():
    jobs=laod_jobs_from_db()
    return render_template('home.html',jobs=jobs)

@app.route("/jobs")
def jobs_info():
    return jsonify(jobs)

if __name__=="__main__":
    app.run(debug=True)

    # wddw