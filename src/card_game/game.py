from typing import List
from .cards import Card

class Game:
    def __init__(self, name: str, cards_in_game: List[Card]) -> None:
        self.name: str = name
        self.cards: List[Card] = cards_in_game
        self.players: List[Player] = []
    
    def add_player(self, player: Player):
        self.players.append(player)
    
    def distribute_card_to_player(self, card_to_distribute: Card, player: Player):
        # On vérifie que la carte existe bien dans le jeu de carte.
        # Si ca n'est pas le cas, on interrompt la distribution.
        if not card_to_distribute in self.cards:
            return
        
        # Même chose mais pour le joueur.
        if not player in self.players:
            return
        
        # On enleve la carte du jeu pour la donner au joueur.
        self.cards.remove(card_to_distribute)
        # On donne la carte au joueur.
        player.add_card(card_to_distribute)
        
    def distribute_cards_to_player(self, cards_to_distribute: List[Card], player: Player):
        # On vérifie que les cartes à distribuer sont bien dans le jeu de carte...
        for card in cards_to_distribute:
            # ... Si ca n'est pas le cas, on ne distribue rien.
            if not card in self.cards:
                return
        
        # On distribue chaque carte au joueur.
        for card in cards_to_distribute:
            self.distribute_card_to_player(card, player)