from tkinter import Y
from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
from helper import get_db_connection, default
from graph_set import Graph_set
import json
from MyEncoder import myEncoder
from ExerciseCollection import ExerciseCollection

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("base.html")

@app.route('/bar')
def bar():
    db = get_db_connection()
    cur = db.cursor()
    userID = [1]
    query = """SELECT users.firstName, workouts.dateandtime AS w_datetime, workouts.id as w_id, sets.id AS s_id, sets.interval AS s_interval, sets.resistance AS s_res,
      sets.setNumber AS s_setNum, sets.workoutID AS s_workID, sets.exerciseID AS s_exeID, exercises.name AS e_name FROM users
      JOIN workouts ON users.id = workouts.userID JOIN sets ON workouts.id = sets.workoutID JOIN exercises ON
      sets.exerciseID = exercises.id WHERE users.id = ? ORDER BY w_id DESC LIMIT 6"""
    exercises = cur.execute(query, userID).fetchall()
    
    graph_exercises = []
    for i in exercises:
        graph_exercises.append(Graph_set(i['s_id'], i['s_interval'], i['s_res'], i['s_setNum'], i['w_id'], i['w_datetime'], i['s_exeID'], i['e_name']))
        
    # find the first exercise of the exercises
    exercise_id = graph_exercises[0].exercise_id
    # start a small list
    big_lst = []
    small_lst = []
    for i in graph_exercises:
        # add to small list til exercise changes
        if i.exercise_id == exercise_id:
            small_lst.append(i)
        else:
            # add small list to big list
            big_lst.append(small_lst)
            # start a new small list
            small_lst = []
            exercise_id = i.exercise_id
            small_lst.append(i)

    # for i in big_lst:
    #     print(i)
    # y = json.dumps(big_lst[0][0])
    # print(big_lst[0][0])
    # print(json.dumps(big_lst[0][0], cls=myEncoder, indent=1))
    # print(myEncoder().encode(big_lst[0][0]))
    ex_1 = big_lst[0][0]
    ex_2 = big_lst[0][1]
    ex_3 = big_lst[1][0]

    print(type(big_lst))
    exer = {"second":[[ex_1], [ex_2, ex_3]]}

    exer_col = ExerciseCollection(exer)
    print(exer_col)
    print(json.dumps(exer_col, cls=myEncoder, indent=2))
    # Need to learn how to make the large JSON text to pass to the page
    # print(json.dumps(big_lst[0][0].__dict__, indent=2, sort_keys= True))
    return render_template("bar.html")

@app.route('/line')
def line():
    return render_template("line.html")

@app.route('/pie')
def pie():
    return render_template("bar.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)