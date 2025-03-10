from sqlalchemy import create_engine,text
db_connection_string="mysql+pymysql://root:KSnLiPhywtGxOfUXVONoHrpDbYuacite@gondola.proxy.rlwy.net:21062/jobportal?charset=utf8mb4"
engine = create_engine(db_connection_string)

def laod_jobs_from_db():
    with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM jobs")).mappings().all()  # Convert rows to dictionaries

      jobs = list(result)  # Already a list of dictionaries
        # Print the results
    return jobs  

def load_job_from_db(id):
  with engine.connect() as conn:
   result =conn.execute(text("SELECT * FROM jobs WHERE id= :val"),{"val":id}).mappings().first()
   if result is None:
     return None
   else:
    return dict(result)
   
def insert_to_db(data,job_id):
  with engine.connect() as conn:
    with conn.begin():
      query = text(" INSERT INTO applications (job_id, full_name, email, linkedin, education, experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin, :education, :experience, :resume_url)")

      conn.execute(query,{"job_id":job_id,
                          "full_name":data["full_name"],
                          "email":data["email"],
                          "linkedin":data["linkedin"],
                          "education":data["education"],
                          "experience":data["experience"],
                          "resume_url":data["resume_url"]})
      conn.commit()
   
    