#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

def calculate_tip():
    # Welcome message
    print("Welcome to the tip calculator.\n")
    # Get user inputs
    total_bill = float(input("What was the total bill? $"))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    total_people = int(input("How many people to split the bill? "))
    # Calculate per person
    each_person = (total_bill / total_people) * (1 + (0.01 * tip_percentage))
    # rounding can be done using "{:.2f}".format(each_person)
    print(f"Each person should pay: ${round(each_person, 2)}")


if __name__ == '__main__':
    calculate_tip()