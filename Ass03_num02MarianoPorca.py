import random

def deckCard(your_cards):
    opponent_cards = [random.randint(0, 9) for _ in range(5)]

    your_cards.sort()
    your_max_number = your_cards[-2] * 10 + your_cards[-1]
    
    opponent_cards.sort()
    opponent_max_number = opponent_cards[-2] * 10 + opponent_cards[-1]
    
    print(f"Opponent's cards: {opponent_cards}")
    
    if your_max_number > opponent_max_number:
        return True
    else:
        return False

your_cards = []
for i in range(5):
    card = int(input(f"Enter your 5 cards {i + 1} (0-9): "))
    your_cards.append(card)

result = deckCard(your_cards)

if result:
    print("True!")
else:
    print("False")