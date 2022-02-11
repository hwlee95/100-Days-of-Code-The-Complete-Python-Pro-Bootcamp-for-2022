# Python script for blind auction

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.\n")
name = input("What is your name?: ")
bid = input("what is your bid?: ")
other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

bidders = {}
bidders[name] = {"bid": bid}

while other_bidders == 'yes':
    name = input("What is your name?: ")
    bid = input("what is your bid?: ")
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    bidders[name] = {"bid": bid}

current_winner = ""
current_winning_bid = 0

for name in bidders:
    bid = int(bidders[name]["bid"])
    if bid > current_winning_bid:
        current_winning_bid = bid
        current_winner = name

print(f"\nThe winner is {current_winner} with a bid of {current_winning_bid}! 🎉\n")