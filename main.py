import argparse

from objects import liftCalc 

def main(week):
    l1 = liftCalc(week)

    l1.calculate(args.trainingmax)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Calculate 5/3/1 lifts")
    parser.add_argument("-w", "--week", metavar="week", type=int, help = "Enter current week")
    parser.add_argument("-tm", "--trainingmax", metavar="training max", type=int, help = "Enter current Training Max")
    parser.set_defaults(feature=False)
    args = parser.parse_args()
    main(args.week)