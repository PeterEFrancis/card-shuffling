def rtr(deck:list):
    n = len(deck)
    card = r.choice(deck)
    new_deck = deck.copy()
    new_deck.remove(card)
    new_loc = r.randint(0, n - 1)
    new_deck.insert(b, card)
    return new_deck, card

def m_rtr(deck:list):
    n = len(deck)
    a = r.randint(0, n - 1)
    card = deck[a]
    new_deck = deck.copy()
    new_deck.remove(card)
    b = r.choice([pos % n for pos in range(a + 2, a + n + 1)])
    new_deck.insert(b, card)
    return new_deck, card
    
    
    
def T_trial(shuffle, n):
    deck = get_deck(n)
    marked = set()
    t = 0
    while len(marked) < n:
        deck, card = shuffle(deck)
        marked.add(card)
        t += 1
    return t
    
    

    
if __name__ == "__main__":
    print("don't be silly: don't execute this file!")