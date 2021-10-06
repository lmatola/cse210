import random

Score_list = []
print()
print("Welcome to the Hilo game!")
print()

new_scores = ""


def computer_guess():
    low = 1
    high = 13
    keep_playing = ""

    while keep_playing != "n":

        print()  

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        guess = random.randint(1, 13)
        guess2 = random.randint(1, 13)
        card = input(f"The card is: {guess}")
        feedback = input("Higher or lower? [h/l] ").lower()
            
        if feedback == "h":
            high = guess - 1
            Next_card = input(f"Next card was: {guess2}")

            if guess2 >= guess:
                score = 100
                Score_list.append(score)
            else:
                score = -75
                Score_list.append(score)
                  
        elif feedback =="l":
            low = guess + 1
            Next_card = input(f"Next card was: {guess2}")

            if guess2 <= guess:
                score = 100
                Score_list.append(score)
            else:
                score = -75
                Score_list.append(score)
        
        sum = 300
        for score in Score_list:
            sum += score     
        print(f"Your score is: {sum}")

        print()

        if sum <= 0:
            print("Game Over")
        else:
            keep_playing = input("Keep playing? [y/n] ")
            if keep_playing == "n":
                print("Game Over")

computer_guess()
print()

