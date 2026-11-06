from random import randint

from .cards import Card, Color, Sign


class Human:
    def __init__(self, first_name: str, last_name: str):
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.cards = []

    def add_card(self, card: Card):
        # On vérifie que le joueur n'a pas déja la carte dans sa main.
        if card in self.cards:
            # Si il l'a déja, on ne la lui donne pas.
            return

        # Si'il ne l'a pas, on la rajoute à sa main.
        self.cards.append(card)

    def get_first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    def distribute(
        self, all_cards: list[Card], total_cards_per_player: int
    ) -> list[Card]:
        """Distributes the cards to players."""
        cards_to_distribute: list[Card] = []

        ...

        return cards_to_distribute
