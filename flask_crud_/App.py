from flask import Flask, request, redirect, render_template
from models import db,studentModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_request
def create_table():
    db.create_all()

@app.route('/create', methods=['POST','GET'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        hobby = request.form.getlist('hobbies')
        hobbies = ' '.join(map(str, hobby))
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        country = request.form['country']
        gender = request.form['gender']
        hobbies = hobbies

        students = studentModel(first_name=first_name,last_name=last_name,email=email,
                                password=password, gender=gender, hobbies=hobbies, country=country)
        
        db.session.add(students)
        db.session.commit()
        # redirect('/')
        return redirect('/')

@app.route('/', methods=["GET"])
def displayList():
    students =  studentModel.query.all()
    return render_template('index.html', students=students)
    

@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    students = studentModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if students:
            db.session.delete(students)
            db.session.commit()
            return redirect('/')
        abort(404)
    return render_template('delete.html')


@app.route('/<int:id>/edit', methods=['GET','POST'])
def update(id):
    student = studentModel.query.filter_by(id=id).first()
    
    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()
       
        hobby = request.form.getlist('hobbies')
        hobbies = ",".join(map(str, hobby))
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        country = request.form['country']
        gender = request.form['gender']
        hobbies = hobbies

        students = studentModel(first_name=first_name,last_name=last_name,email=email,
                                password=password, gender=gender, hobbies=hobbies, country=country)
        
        db.session.add(students)
        db.session.commit()
        return redirect('/')
        return f"student id {id} Does not exist"
        
    return render_template('update.html', student=student)

if __name__ == ('__main__'):
    app.run(debug=True)