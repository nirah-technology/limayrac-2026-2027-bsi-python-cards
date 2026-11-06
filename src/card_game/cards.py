from enum import Enum as Enumeration


class Color(Enumeration):
    RED = 0
    BLACK = 1


class Sign(Enumeration):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2
    SPADES = 3


class Card:
    def __init__(self, value: int, color: Color, sign: Sign):
        self.__value: int = value
        self.__color: Color = color
        self.__sign: Sign = sign

    @property
    def value(self) -> int:
        return self.__value

    @property
    def color(self) -> Color:
        return self.__color

    @property
    def sign(self) -> Sign:
        return self.__sign


class PackCards:
    def __init__(self, total_cards_in_game: int = 52):
        self.cards: list[Card] = self.__create_all_cards(total_cards_in_game)

    def __create_all_cards(self, total_cards_in_game: int = 52):
        all_cards: list[Card] = []

        for counter in range(
            total_cards_in_game
        ):  # on créé un compter qui commence automatiquement à 0 et va à 52
            value: int = (
                (counter % 13) + 1
            )  # On fait une division avec RESTE et on rajoute 1. Ex: 0%13 = 0 et 0+1 = 1
            color: Color = (
                Color.RED if counter < 26 else Color.BLACK
            )  # 26 premières cartes seront rouge, les autre seront noir
            sign: Sign = None
            if counter < 13:
                sign = Sign.HEARTS  # 13 premières cartes seront de coeur
            elif counter < 26:
                sign = Sign.DIAMONDS  # 13 suivantes seront de carreaux
            elif counter < 39:
                sign = Sign.CLUBS  # 13 suivantes seront de trèfles
            else:
                sign = Sign.SPADES  # et les autres seront de pique

            card: Card = Card(value=value, color=color, sign=sign)
            all_cards.append(card)

        return all_cards
