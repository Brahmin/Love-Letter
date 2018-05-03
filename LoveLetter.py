import random
import copy
Guard, Priest, Baron, Handmaid, Prince, King, Countess, Princess = [1,5],[2,2],[3,2],[4,2],[5,2],[6,1],[7,1],[8,1]
cards = Guard, Priest, Baron, Handmaid, Prince, King, Countess, Princess
deck = []
for card in cards:
    for each in range(0,card[1]):
        deck.append(card[0])

default_deck = copy.deepcopy(deck)



#deal the cards out
random.shuffle(deck)
hands = [[],[]]
discards = [[],[]]
face_up = []
face_down = []

deck = [1,1,1,1,1,1,1,1,1,1,3]

hands[0].append(deck.pop())
hands[1].append(deck.pop())
face_down.append(deck.pop())
for each in range(3):
    face_up.append(deck.pop())

def print_player_game_state():
    print('')
    print('Player Hand:' + str(hands[0]))
    print('Player Discard:' + str(discards[0]))
    print('Computer Discard:' + str(discards[1]))
    print('Face up pile:' + str(face_up))
    print('Deck size:' + str(len(deck)))
    print('Current player: ' + str(current_player))

def print_computer_hand():
    print('Computer Hand:' + str(hands[1]))

def get_target(legal_targets):
    new_target = target
    legal_targets = copy.deepcopy(legal_targets)
    for each_player in legal_targets:
        if each_player in handmaided:
            legal_targets.remove(each_player)
    if legal_targets == []:
        new_target = None
    elif len(legal_targets) == 1:
        new_target = legal_targets[0]
    else:
        while new_target not in legal_targets:
            if human_player:
                new_target = int(input('Pick a player: ' + str(legal_targets)+ ' '))
            else:
                new_target = pick_computer_target()
    return new_target

def other_players():
    possible_players = copy.deepcopy(players)
    possible_players.remove(current_player)
    return possible_players

def evaluate_played_card():
    if played_card == 1:
        target = get_target(other_players())
        if target != None:
            if human_player:
                guessed_card = int(input('Guess a card: '))
            else:
                guessed_card = pick_computer_guess()
                print(guessed_card)
            if guessed_card == hands[target][0] and guessed_card != 1:
                print('Good guess')
                players.remove(target)
    if played_card == 2:
        target = get_target(other_players())
        if target!= None:
            print(hands[target])
    if played_card == 3:
        target = get_target(other_players())
        if target != None:
            print(hands[target])
            if hands[current_player] > hands[target]:
                players.remove(target)
            if hands[current_player] < hands[target]:
                players.remove(current_player)
    if played_card == 4:
        handmaided.append(current_player)
        print('Handmaid')
    if played_card == 5:
        target = get_target(players)
        discarded = hands[target].pop()
        discards[target].append(discarded)
        if discarded == 8:
            players.remove(target)
        else:
            if len(deck) != 0:
                hands[target].append(deck.pop())
            else:
                hands[target].append(face_down.pop())
    if played_card == 6:
        target = get_target(other_players())
        if target != None:
            hands[current_player], hands[target] = hands[target], hands[current_player]
    if played_card == 7:
        print('Suspicious')
    if played_card == 8:
        players.remove(current_player)

def discard_played_card():
    hands[current_player].remove(played_card)
    discards[current_player].append(played_card)

def pick_computer_card():
    lower_card, higher_card = hands[current_player][0], hands[current_player][1]
    if higher_card == 8:
        picked_card = lower_card
    if higher_card == 7:
        picked_card = higher_card
    if higher_card == 6:
        picked_card = lower_card
    if higher_card == 5:
        picked_card = higher_card
    if higher_card == 4:
        picked_card = higher_card
    if higher_card == 3:
        picked_card = lower_card
    if higher_card == 2:
        picked_card = higher_card
    if higher_card == 1:
        picked_card = higher_card
    return picked_card

def pick_computer_target():
    return 0
        
def pick_computer_guess():
    return 3#random.randrange(1, 8)+1
    

num_of_players = 2
players = []
for each in range(num_of_players):
    players.append(each)
print(players)
handmaided = []
turn = 1
while len(deck) >= 1 and len(players) > 1:
    #Reset everything
    played_card = None
    target = None
    #This is a hack \/
    current_player = (turn+1)%num_of_players
    if current_player in handmaided:
        handmaided.remove(current_player)
    #Draw for turn and get started
    hands[current_player].append(deck.pop())
    hands[current_player].sort()
    print_player_game_state()
    if current_player == 0:
        human_player = True
        while played_card not in hands[current_player]:
            played_card = int(input('Pick a card: ' + str(hands[current_player])))
        discard_played_card()
        evaluate_played_card()
        turn += 1
    if current_player == 1:
        human_player = False
        played_card = pick_computer_card()
        if played_card in hands[1]:
            discard_played_card()
            print(discards[1])
            evaluate_played_card()
            turn += 1


print_player_game_state()
print_computer_hand()
print('Face down pile:' + str(face_down))
print(deck)
print('Winner is: ' + str(players))

#Never play 8
#Always play 7
#Almost never play 6
#Target them with 5
#Almost always 4
#If I have a 5+, 3
#Almost always 2
#Guess highest likely








