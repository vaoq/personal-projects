from random import shuffle
from random import randint

cards = [
    ['hA', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'hT', 'hJ', 'hQ', 'hK'],  # ♥
    ['dA', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'dT', 'dJ', 'dQ', 'dK'],  # ♦
    ['sA', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'sT', 'sJ', 'sQ', 'sK'],  # ♣
    ['cA', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'cT', 'cJ', 'cQ', 'cK']]  # ♠

def start_game(card_deck: list[str]) -> list[str]:
    deck = cards.copy()
    for i in deck:
        shuffle(i)


dealer_hand = []

player_hand = []