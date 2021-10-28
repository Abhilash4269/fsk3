pip install:
    - flask 
    - Flask-MysqlAlchemy
    - pymysql

# Download bootstrap CSS and JS , import both files under Static.
  - NOTE - HTML files have to be under Templates.

Created basic form for student details using bootstrap. Performed CRUD operations on the table.:
        - Soft Delete was implemented , all records store in db. ( cannot be deleted from db )

creating table using flask-mysql:
>>>     from App import db
>>>     db.create_all()


