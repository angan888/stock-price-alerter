def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    
    card_value_map = {"K":10, "J":10, "Q":10, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10}

    for ndx,card in enumerate(hand_1):
        if card == 'A': 
            hand_1[ndx] = 'X'

    hand_1 = sorted(hand_1)
    hand1_total = 0
    for card in hand_1:
        if not(card == "X"):
            hand1_total += card_value_map[card]
        elif card == "X":
            if hand1_total+11 <= 21:
                hand1_total += 11
            else:
                hand1_total += 1
    
    for ndx,card in enumerate(hand_2):
        if card == 'A': 
            hand_2[ndx] = 'X'

    hand_2 = sorted(hand_2)
    hand2_total = 0
    for card in hand_2:
        if not(card == "X"):
            hand2_total += card_value_map[card]
        elif card == "X":
            if hand2_total+11 <= 21:
                hand2_total += 11
            else:
                hand2_total += 1

    print(hand1_total)
    print(hand2_total)


    if (hand1_total <= 21) and (hand1_total > hand2_total or hand2_total > 21):
        return True
    else:
        return False


               



hand_1 = ['2', '10', '5', 'A', '9', '9']
hand_2 = ['5', '7', '5', 'Q', '5']

print( blackjack_hand_greater_than(hand_1,hand_2) )

