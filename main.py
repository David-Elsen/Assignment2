"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    semcost=annual_cost / SEMESTERS_PER_YEAR
    return semcost


def cost_per_month(annual_cost):
    monthcost=annual_cost / MONTHS_PER_YEAR
    return monthcost


def cost_per_day(annual_cost):
    daycost=annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return daycost


def cost_per_credit(annual_cost, credits):
    creditcost=(annual_cost /2)/ credits
    return creditcost


def cost_per_class(annual_cost, credits):
    classcost=(annual_cost/2) / (credits / CS1430_CREDITS * CS1430_MEETINGS_PER_SEMESTER)
    return classcost

def cost_per_meeting(annual_cost):
    meetingcost=(annual_cost/2) / (CS1430_MEETINGS_PER_SEMESTER)
    return meetingcost

# ---- PROGRAM ----

def main():
    YearCost= float(input("Enter the total cost for one year: "))
    Credits=int(input("Enter the number of credits this semester: "))
   
    while True:
        print("Menu:")
        print("1. cost per semester")
        print("2. cost per month")
        print("3. cost per day")
        print("4. cost per credit")
        print("5. cost per class")
        print("6. cost per CS1430 meeting")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            print("Cost per semester: ", f"{cost_per_semester(YearCost):.2f}")
        elif choice == "2":
            print("Cost per month: ", f"{cost_per_month(YearCost):.2f}")
        elif choice == "3":
            print("Cost per day: ", f"{cost_per_day(YearCost):.2f}")
        elif choice == "4":
            print("Cost per credit: ", f"{cost_per_credit(YearCost, Credits):.2f}")
        elif choice == "5":
            print("Cost per class: ", f"{cost_per_class(YearCost, Credits):.2f}")
        elif choice == "6":
            print("Cost per CS1430meeting: ", f"{cost_per_meeting(YearCost):.2f}")
        else:
            print("Invalid choice. Please try again.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
