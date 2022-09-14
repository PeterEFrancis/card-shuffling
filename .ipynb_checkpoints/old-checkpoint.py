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
    
    
    
    
#                     # forward (card moving up)
#                     new_deck_1 = self.deck.copy()
#                     new_marked_1 = self.marked.copy()
#                     print(initial + length - 1)
#                     card_1 = new_deck_1[initial + length - 1]
#                     new_marked_1.add(card_1)
#                     new_deck_1.remove(card_1)
#                     new_deck_1.insert(initial, card_1)
#                     self.children.append(Node(new_deck_1, new_marked_1, self.depth + 1, 1 / size_of_S))
                    
#                     # backwards (card moving down)
#                     new_deck_2 = self.deck.copy()
#                     new_marked_2 = self.marked.copy()
#                     card_2 = new_deck_2[initial]
#                     new_marked_2.add(card_2)
#                     new_deck_2.remove(card_2)
#                     new_deck_2.insert(initial + length - 1, card_2)
#                     self.children.append(Node(new_deck_2, new_marked_2, self.depth + 1, 1 / size_of_S))
                    
    

    
if __name__ == "__main__":
    print("don't be silly: don't execute this file!")