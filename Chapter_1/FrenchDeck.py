"""
220510
챕터 1
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


base_card = Card('7', 'diamonds')
print(base_card)

deck = FrenchDeck()
print(len(deck))

print(deck[0], deck[-1])


from random import choice

print(choice(deck), choice(deck))

print(deck[:3])
print(deck[12::13])
# a[시작:끝:간격] start through not past stop, by step. 12 시작, 13 간격으로
# https://docs.python.org/ko/3/library/stdtypes.html#common-sequence-operations

for card in deck:  # doctest: +ELLIPSIS
    print(card)

for card in reversed(deck):  # doctest: +ELLIPSIS
    print(card)
# https://docs.python.org/ko/3/library/doctest.html#doctest.ELLIPSIS

print(Card('Q', 'hearts') in deck)
print(Card('77', 'beasts') in deck)


suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
# https://docs.python.org/ko/3/library/stdtypes.html#dict
print(suits_values)


def spades_hight(card):
    # 카드 점수 계산. 0: 2 clubs, 51: ace spades. rank first, suit second
    rank_value = FrenchDeck.ranks.index(card.rank)  # 0 ~ 12
    return rank_value * len(suits_values) + suits_values[card.suit]


for card in sorted(deck, key=spades_hight):
    print(card)
