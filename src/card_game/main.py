from .cards import Card, Color
from .game import Game
from .humans import Human
from .rules import AbstractGameRules, Bataille


def main() -> None:
    me: Human = Human(last_name="METIVIER", first_name="Nicolas")
    bot: Human = Human(last_name="DOE", first_name="John")

    game: AbstractGameRules = Bataille()


# Définir le point d'entré du programme.
if __name__ == "__main__":
    main()
