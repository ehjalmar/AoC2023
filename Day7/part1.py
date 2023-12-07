from collections import defaultdict
import functools

file = open('Day7/input.txt', 'r')
lines = file.read().splitlines()

class HandBet:
    def __init__(self, line: str) -> None:
       splitted_line = line.split(' ')
       self.hand = splitted_line[0]
       self.bet = int(splitted_line[1])

def check_five_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [5]:
        return True
    return False

def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False

def check_two_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False

def check_one_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return True
    else:
        return False

def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

def check_hand(hand):
    if check_five_of_a_kind(hand):
        return 8
    if check_four_of_a_kind(hand):
        return 7
    if check_full_house(hand):
        return 6
    if check_three_of_a_kind(hand):
        return 5
    if check_two_pair(hand):
        return 3
    if check_one_pair(hand):
        return 2
    return 1

card_order = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}

def compare_hand(x: HandBet, y: HandBet):
    if(check_hand(x.hand) > check_hand(y.hand)):
        return 1
    if(check_hand(x.hand) == check_hand(y.hand)):
        for i in range(0, len(x.hand)):
            if(card_order[x.hand[i]] > card_order[y.hand[i]]):
                return 1
            elif(card_order[y.hand[i]] > card_order[x.hand[i]]):
                return -1
    else:
        return -1

hands = []

for line in lines:
    hands.append(HandBet(line))

sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hand))

rank = 1
total_winnings = 0

for current_hand in sorted_hands:
    total_winnings += current_hand.bet * rank
    rank +=1

print(total_winnings)