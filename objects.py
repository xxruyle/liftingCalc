class liftCalc(): 
    def __init__(self, week):
        self.week = week 

    def calculate(self, trainingM): 
        if self.week == 1: 
            print(f" 5 Reps @ {trainingM * .65} (65%)")
            print(f" 5 Reps @ {trainingM * .75} (75%)")
            print(f" 5+ Reps @ {trainingM * .85} (85%)")
            print(f" 5x5 @ {trainingM * .65} (65%)")
        elif self.week == 2: 
            print(f" 3 Reps @ {trainingM * .70} (70%)")
            print(f" 3 Reps @ {trainingM * .80} (80%)")
            print(f" 3+ Reps @ {trainingM * .90} (90%)")
            print(f" 5x5 @ {trainingM * .70} (70%)")
        elif self.week == 3:
            print(f" 5 Reps @ {trainingM * .75} (75%)")
            print(f" 3 Reps @ {trainingM * .85} (85%)")
            print(f" 1+ Reps @ {trainingM * .95} (95%)")
            print(f" 5x5 @ {trainingM * .75} (75%)")