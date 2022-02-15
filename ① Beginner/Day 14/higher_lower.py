import data
import art
import random

def higher_lower():
    print(art.logo)
    continue_game = True
    score = 0
    game_data = data.data
    random_data = random.randint(0, len(game_data) - 1)
    side_a = game_data[random_data]
    del game_data[random_data]
    random_data = random.randint(0, len(game_data) - 1)
    side_b = game_data[random_data]
    del game_data[random_data]
    while continue_game == True and len(game_data) > 0:
        print(f"Compare A: {side_a['name']}, {side_a['description']} from {side_a['country']}")
        print("    vs")
        print(f"Compare B: {side_b['name']}, {side_b['description']} from {side_b['country']}")
        guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
        if side_a['follower_count'] > side_b['follower_count'] and guess == 'A':
            score += 1
            print(f"You're right! Current score: {score}\n")
            random_data = random.randint(0, len(game_data) - 1)
            side_b = game_data[random_data]
            del game_data[random_data]
        elif side_a['follower_count'] < side_b['follower_count'] and guess == 'B':
            score += 1
            print(f"You're right! Current score: {score}\n")
            side_a = side_b
            random_data = random.randint(0, len(game_data) - 1)
            side_b = game_data[random_data]
            del game_data[random_data]
        elif side_a['follower_count'] == side_b['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}\n")
            if guess == 'A':
                random_data = random.randint(0, len(game_data) - 1)
                side_b = game_data[random_data]
                del game_data[random_data]
            else:
                side_a = side_b
                random_data = random.randint(0, len(game_data) - 1)
                side_b = game_data[random_data]
                del game_data[random_data]
        else:
            print(f"You're wrong! Your score: {score}\n")
            continue_game = False

if __name__ == '__main__':
    higher_lower()