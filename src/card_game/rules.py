from abc import ABC, abstractmethod
from typing import override
from .cards import Card
from .game import Game
from .humans import Human
from src.card_game import cards


class AbstractGameRules(Game, ABC):
    def __init__(self, game_name: str, cards_in_game: list[Card]):
        super().__init__(game_name, cards_in_game)

    # @abstractmethod
    def setup_game(self):
        """
        Prépare e jeu avant le début de la partie (ex: distrubtion de cartes, mises initiales, choix du donneur, etc)
        """
        pass

    @abstractmethod
    def play_turn(self) -> str:
        """
        Exécute la logique d'un tour de jeu complet et route le résumé de l'action.
        """
        pass

    @abstractmethod
    def check__winner(self) -> Human | None:
        """
        Vérifie les conditions de victoire spécifique eu jeu.
        Reoute le joueur gagnant ou None si la partie continue.
        """
        pass


class Bataille(AbstractGameRules):
    def __init__(self, cards_in_game: list[Card]):
        super().__init__("Bataille", cards_in_game)

    @override
    def setup_game(self):
        if len(self.players) == 2:
            middle = len(self.cards) // 2
            player_1 = self.players[0]
            player_2 = self.players[1]

            cards_for_player_1 = self.cards[:middle]
            cards_for_player_2 = self.cards[middle:]

            self.distribute_cards_to_player(cards_for_player_1, player_1)
            self.distribute_cards_to_player(cards_for_player_2, player_2)

    @override
    def play_turn(self) -> str:
        if len(self.players) < 2:
            return "Il faut 2 joueurs pour jouer à la bataille."

        player_1, player_2 = self.players[0], self.players[1]

        if not player_1.cards or not player_2.cards:
            return "La partie est terminée."

        card_player_1 = player_1.cards.pop(0)
        card_player_2 = player_2.cards.pop(0)

        if card_player_1.value > card_player_2.value:
            player_1.cards.extend([card_player_1, card_player_2])
        elif card_player_2.value > card_player_1.value:
            player_2.cards.extend([card_player_1, card_player_2])
        else:
            player_1.cards.append(card_player_1)
            player_2.cards.append(card_player_2)
            return "Egalité ! Chacun reprend sa carte."

    @override
    def check__winner(self) -> Human | None:
        if len(self.players) < 2:
            return None
        player_1, player_2 = self.players[0], self.players[1]

        if not player_2.cards:
            return player_1
        if not player_1.cards:
            return player_2
        return None
