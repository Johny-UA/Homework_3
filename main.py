from folder.game import Game
from folder.models import Player
from folder.score import ScoreHandler
from folder.settings import SCORE_FILE, MENU, START_GAME, SHOW_SCORE, EXIT

def play_game ():
      player, mode = create_player()
      game = Game(player, mode)
      game.play()

def create_player():
      name = input('Input the name: ')
      while True:
            try:
               mode = input('Input the difficulty ( 1=ease, 2=medium, 3=hard): ')
               player = Player(name, mode)
               return player, mode
            except KeyError:
                 print('Bad choice')

def show_score():
      handler = ScoreHandler(SCORE_FILE)
      handler.display()


def main():
     while True:
         input_menu = input('Start Game = 1, Show Score = 2, Exit = 3:')
         try:
            menu = MENU[input_menu]
            if menu == START_GAME:
                  play_game()
            elif menu == SHOW_SCORE:
               show_score()
            elif menu == EXIT:
                  break
         except KeyError:
              print('Incorrect choose')



main()

