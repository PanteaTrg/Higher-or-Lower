import random

total_round = 8
initial_score = 50

suit_tuple = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
rank_tuple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')


#  Build the deck
deck_list = []
for suit in suit_tuple:
    for count, rank in enumerate(rank_tuple):
        deck_list.append({'rank': rank, 'suit': suit, 'value': count + 1})


print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()


while True:
    random.shuffle(deck_list)
    first_deck = deck_list.pop()

    current_rank = first_deck['rank']
    current_suit = first_deck['suit']
    current_value = first_deck['value']

    for i in range(0, total_round):
        print('This is your ', i + 1, 'st round')
        print('Your starting card is: ', current_rank, ' ', current_suit, ' ', current_value)
        print()
        answer = input('Is the next card Higher or Lower than the current card? [h, l]: ')

        # Pick the next card
        random.shuffle(deck_list)
        next_card = deck_list.pop()
        next_rank, next_suit, next_value = next_card['rank'], next_card['suit'], next_card['value']

        print('Next Card is: ', next_rank, ' ', next_suit, ' ', next_value)
        print()

        if answer.lower() == 'h':
            if next_value > current_value:
                print('You won :)')
                initial_score += 10
            else:
                print('Sorry you lost :(')
                initial_score -= 20

        elif answer.lower() == 'l':
            if next_value < current_value:
                print('You won :)')
                initial_score += 10
            else:
                print('Sorry you lost :(')
                initial_score -= 20

        print('Your score is: ', initial_score)
        current_rank = next_rank
        current_value = next_value
        current_suit = next_suit

    goAgain = input('Do you still want to play honey? :)--> [y / n]')
    if goAgain.lower() == 'n':
        break
print('ok Bye!')
