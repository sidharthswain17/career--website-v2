from sqlalchemy import create_engine,text
db_connection_string="mysql+pymysql://root:KSnLiPhywtGxOfUXVONoHrpDbYuacite@gondola.proxy.rlwy.net:21062/jobportal?charset=utf8mb4"
engine = create_engine(db_connection_string)


# # Test the connection
# try:
#     with engine.connect() as connection:
#         print("Connected to the database successfully!")
# except Exception as e:
#     print(f"Error: {e}")
# with engine.connect() as conn:
#     result=conn.execute(text("SELECT * FROM jobs"))

#     result_dicts=[]
#     for row in result.all():
#         result_dicts.append(dict(row))
    


# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs")).mappings().all()  # Convert rows to dictionaries

#     result_dicts = list(result)  # Already a list of dictionaries
#     print(result_dicts)  # Print the results
def laod_jobs_from_db():
    with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM jobs")).mappings().all()  # Convert rows to dictionaries

      jobs = list(result)  # Already a list of dictionaries
        # Print the results
    return jobs  
    
    
    
    