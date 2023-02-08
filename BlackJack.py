import random
Cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

def PlayerStart(X):
    players_score = X
    current_value = random.choice(Cards)
    current_suit = random.choice(Suits)
    print("You got " + str(current_value) + " of " + current_suit)
    players_score = players_score + current_value
    current_value = random.choice(Cards)
    current_suit = random.choice(Suits)
    print("You got " + str(current_value) + " of " + current_suit)
    players_score = players_score + current_value
    return players_score

def dealerStart(X):
    dealer_score = X
    current_value = random.choice(Cards)
    dealer_score = dealer_score + current_value
    current_value = random.choice(Cards)
    dealer_score = dealer_score + current_value
    return dealer_score

def dealer_deal(x):
    score = x
    current_value = random.choice(Cards)
    score = score + current_value
    return score

def player_deal(x):
    score = x
    current_value = random.choice(Cards)
    current_suit = random.choice(Suits)
    print("You got " + str(current_value) + " of " + current_suit)
    score = score + current_value
    return score

players_score = 0
dealers_score = 0
loop = 0

while loop <= 1:
    decision = input()
    if decision == "start":
        dealers_score = dealerStart(dealers_score)
        players_score = PlayerStart(players_score)
    elif decision == "deal":
        players_score = player_deal(players_score)
        if dealers_score < 17:
            dealers_score = dealer_deal(dealers_score)
    elif decision == "stand":
        print("You dont take a card")
        if dealers_score < 17:
            dealer_deal(dealers_score)
    loop = loop + 1

if dealers_score > 21:
    print("Dealer is bust")
elif dealers_score == 21:
    print("Dealer wins")

if players_score > 21:
    print("You are bust")
elif players_score == 21:
    print("You win")

if players_score <= 21 and dealers_score <= 21:
    if players_score > dealers_score:
        print("You win")
    elif dealers_score > players_score:
        print("Dealer wins")
    elif dealers_score == players_score:
        print("Draw")