# Rock Paper Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("\n✨ Play Rock Paper Scissors! ✨\n")
while True:
    user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
    if user not in ("0", "1", "2"):
        print("Invalid choice. Please try again.")
    else:
        break
print("\n")
computer = random.randint(0, 2)
if user == "0":
    if computer == 0:
        print(f"You: \n {rock} \n Computer: \n {rock} \n Draw!")
    elif computer == 1:
        print(f"You: \n {rock} \n Computer: \n {paper} \n You lose :(")
    else:
        print(f"You: \n {rock} \n Computer: \n {scissors} \n You win :)")
elif user == "1":
    if computer == 0:
        print(f"You: \n {paper} \n Computer: \n {rock} \n You win :)")
    elif computer == 1:
        print(f"You: \n {paper} \n Computer: \n {paper} \n Draw!")
    else:
        print(f"You: \n {paper} \n Computer: \n {scissors} \n You lose :(")
else:
    if computer == 0:
        print(f"You: \n {scissors} \n Computer: \n {rock} \n You lose :(")
    elif computer == 1:
        print(f"You: \n {scissors} \n Computer: \n {paper} \n You win :)")
    else:
        print(f"You: \n {scissors} \n Computer: \n {scissors} \n Draw!")

