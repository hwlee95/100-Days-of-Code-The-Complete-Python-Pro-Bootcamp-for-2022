print('''
*******************************************************************************
                      _..._
                            \_.._ `'-.,--,
                             '-._'-.  `\ a|
                                 '. `_.' (|
                                   `7    ||
                                   /   .' |
                                  /_.-'  ,J
                                 /         |
                                ||   /      ;
                     _..        ||  |       |  /`\.-.
                   .' _ `\      `\  \       |  \_/__/
                  /  /e)-,\       '. \      /.-` .'|
                 /  |  ,_ |        /\ `;_.-'_.-'`\_/
                /   '-(-.)/        \_;(((_.-;
              .'--.   \  `       .(((_,;`'.  |
             /    `\   |   _.--'`__.'  `\  '-;|
           /`       |  /.-'  .--'        '._.'||
         .'        ;  /__.-'`             |  \ |
       .'`-'_     /_.')))                  \_\,_/
      / -'_.'---;`'-)))
     (__.'/   /` .'`
      (_.'/ /` /`
        _|.' /`
  jgs.-` __.'|
      .-'||  |
         \_`/
           `
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

#Write your code below this line 👇
first = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ').lower()
if first == "left":
    second = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if second == "wait":
        third = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if third == "red":
            print("It's a room full of fire. Game Over.")
        elif third == "yellow":
            print("You get attacked by an angry trout. Game Over.")
        elif third == "blue":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    elif second == "swim":
        third = input("You arrive at the island with cuts and bruises. You are bleeding and you see a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if third == "red":
            print("It's a room full of fire. Game Over.")
        elif third == "yellow":
            print("You get attacked by an angry trout. Game Over.")
        elif third == "blue":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You chose a method that doesn't exist. You get attacked by a poisonous spider. Game Over.")
elif first == "right":
    second = input('You\'ve come to a forest. There is a cave in the middle of the forest. Type "path" to walk on the path. Type "forest" to go through the forest. ').lower()
    if second == "path":
        third = input("You arrive at the cave unharmed. There are 2 treasure box with different colours. One red, and one yellow. Which colour do you choose? ").lower()
        if third == "red":
            print("You found a treasure box full with rocks. Game Over.")
        elif third == "yellow":
            print("You found the treasure! You Win!")
    elif second == "forest":
        print("You get attacked by an angry bear. Game Over.")
    else:
        print("You get attacked by a gigantic bird while deciding. Game Over.")
else:
    print("You chose to stay at the crossroad. You get attacked by a venomous snake. Game Over.")

