# Python script for generating unique band name

def generate_name():
    print("Hello, I will generate a band name for you!")
    city = input("What is the name of the city you grew up?\n")
    pet = input("What is the name of your pet?\n")
    print("Your unique band name is:")
    print(city + " " + pet)


if __name__ == '__main__':
    generate_name()
