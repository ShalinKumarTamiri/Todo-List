""" Todo list using flask"""

#Importing packages
from flask import Flask ,render_template , request , redirect , url_for

app = Flask(__name__)
#storing data 
db = []

@app.route("/" , methods = ["POST","GET"] )


def home():
	#request is post then adding task to db
	if request.method == "POST":
		newTask = request.form["newTask"]
		#checking if field is not empty and it is not in the db
		if len(newTask) > 0 and newTask not in db:
			db.append(newTask)
	return render_template("index.html",tasks = db)
	
	
#function to delete the tasks 
@app.route("/delete/<task>")
def delete(task):
 	db.remove(task)
 	return redirect(url_for("home"))
 	
 	
if __name__ == "__main__":
 	app.run()