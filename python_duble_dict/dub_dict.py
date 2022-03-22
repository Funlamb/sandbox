from datetime import date


class workout:
    '''
    Users that input workouts will have created a workout
    
    Dater is used to avoid keyword useage of date
    
    It's poo poo
    '''
    def __init__(self, dater, name, interval, resistance) -> None:
        self.dater = dater
        self.name = name
        self.interval = interval
        self.resistance = resistance
    pass

w_1 = workout("2022", "Bench", 7, 125)
w_2 = workout("2022", "Bench", 7, 125)
w_3 = workout("2022", "Press", 9, 95)
w_4 = workout("2022", "Tricep", 7, 125)
w_5 = workout("2023", "Bench", 8, 125)
w_6 = workout("2023", "Press", 8, 95)
w_7 = workout("2023", "Press", 8, 90)
w_8 = workout("2023", "Press", 12, 95)

workouts = [w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8]

workouts_dates = [wk.dater for wk in workouts] # gets the list of the workout names
print("workouts")
print(workouts_dates)

single_dict = {d:{} for d in workouts_dates} # Makes a dict of the workouts
print(single_dict)

# for i in zip(workouts, workouts_dates):
#     print(i[0].dater + " " + i[0].name + " " + str(i[0].interval) + " " + str(i[0].resistance) + " " + i[1])

for wos in (workouts):
    dater = wos.dater
    name = wos.name
    interval = wos.interval
    res = wos.resistance
    if name in single_dict[dater]:
        single_dict[dater][name] += [interval, res]
    else:
        single_dict[dater][name] = [interval, res]

for wos_dates in single_dict:
    print(wos_dates)
    for ex, pat in single_dict[wos_dates].items():
        print(ex,*pat,sep="    ")