from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:CHEESEballs*69@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    phone = db.Column(db.Integer) # able to give 9 digit input only
    Created_on = db.Column(db.Date)
    Updated_on = db.Column(db.Date)
    Is_Active = db.Column(db.Integer)
    


    def __init__(self, name, location, phone, Created_on, Updated_on, Is_Active):

        self.name = name
        self.location = location
        self.phone = phone
        self.Created_on = Created_on
        self.Updated_on = Updated_on
        self.Is_Active = Is_Active


        
#This is the index route where we are going to
#query on all our student data
# READ

@app.route('/')
def Index():
    all_data1=[]
    all_data = Data.query.all()
    print(all_data)
    for data1 in all_data:
        if data1.Is_Active == 1:
            all_data1.append(data1)

    print(all_data1)
    return render_template("index.html", students = all_data1)


#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        location = request.form['location']
        phone = request.form['phone']
        Created_on = request.form['dateC']
        Updated_on = request.form['dateU']
        Is_Active = 1


        my_data = Data(name, location, phone, Created_on, Updated_on, Is_Active)
        db.session.add(my_data)
        db.session.commit()

        flash("Student Inserted Successfully")

        return redirect(url_for('Index'))


#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.location = request.form['location']
        my_data.phone = request.form['phone']
        my_data.dateC = request.form['dateC']
        my_data.dateU = request.form['dateU']

        db.session.commit()
        flash("Student Updated Successfully")

        return redirect(url_for('Index'))


#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data1 =[]
    my_data1 = Data.query.get(id)
    print(my_data1.Is_Active)
    my_data1.Is_Active = 0
    print(my_data1.Is_Active)

    # my_data = Data(name, location, phone, Created_on, Updated_on, Is_Active)
    db.session.add(my_data1)
    db.session.commit()

    flash("Student Deleted Successfully")

    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)