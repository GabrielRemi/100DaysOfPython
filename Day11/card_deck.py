import emoji
from dataclasses import dataclass
import random


@dataclass
class Card:
    """This class represents a playing card. It has a suit, rank, and a value."""
    suit: str
    name: str
    value: int

    def __str__(self):
        return f"{self.name}{self.suit}"

    def __eq__(self, other):
        return self.suit == other.suit and self.name == other.name


class CardDeck:
    """This class represents a standard card deck of 52. You can generate a new deck and
    take a card from the top. You can shuffle the deck and so on."""

    __colors: list[str] = [emoji.emojize(f":{i}_suit:") for i in ["club", "diamond", "heart", "spade"]]
    __card_names: list[str] = [str(i) for i in range(2, 11)]
    __card_names.extend(["Jack", "Queen", "King", "Ace"])
    __deck_sorted: list[Card] = []
    for color in __colors:
        for name in __card_names:
            value: int = 10
            try:
                value = int(name)
            except:
                pass

            if name == "Ace":
                value = 11

            __deck_sorted.append(Card(color, name, value))

    @property
    def colors(self):
        return CardDeck.__colors

    @property
    def card_names(self):
        return CardDeck.__card_names

    @property
    def deck(self):
        return self.__deck

    @property
    def deck_sorted(self):
        return self.__deck_sorted

    def __init__(self):
        self.__nums = [1, 2, 3]
        self.__deck = CardDeck.__deck_sorted.copy()

    def deck_str(self):
        return [str(i) for i in self.__deck]

    def is_sorted(self):
        return CardDeck.__deck_sorted == self.__deck

    def shuffle(self):
        random.shuffle(self.__deck)

    def take_from_top(self):
        return self.__deck.pop()

    def insert_card_on_top(self, card: Card):
        self.__deck.append(card)

    def take_from_bottom(self):
        return self.__deck.pop(0)

    def insert_card_on_bottom(self, card: Card):
        self.__deck.insert(0, card)

    def cards_left(self):
        return len(self.__deck)


if __name__ == "__main__":
    deck = CardDeck()
    print(deck.is_sorted())
    print(deck.deck_str())

    deck.shuffle()
    print(deck.deck_str())
    card = deck.take_from_top()
    deck.insert_card_on_bottom(card)
    print(deck.deck_str())
