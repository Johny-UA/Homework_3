from settings import *
from models import Player, Enemy

class Game:
   player:  Player
   enemy: Enemy
   mode: str

   def __init__(self,player, mode):
      self.player = player
      self.mode = MODES[mode]
      self.enemy = self.create_enemy()


   def create_enemy(self):
      return Enemy(ENEMY_LIVES[self.mode])
   

   def fight (self):

      player_select_attack = self.player.select_attack_item()
      enemy_select_attack = self.enemy.select_attack()

      print(f'{player_select_attack} vs. {enemy_select_attack}')
      checking_attack_pairs = (ATTACK_PAIRS[(player_select_attack, enemy_select_attack)])
      
      self.handle_fight_result(checking_attack_pairs)





   def handle_fight_result (self, checking_attack_pairs):
      if checking_attack_pairs == WIN:
         self.WIN()
      elif checking_attack_pairs == DRAW:
         self.DRAW()
      elif checking_attack_pairs == LOSE:
         self.LOSE()


   def DRAW (self):
      print('Draw')

   def LOSE (self):
      print('Lose')
      self.player.degrees_lives()

   def WIN (self):
      print('Win')
      self.enemy.degrees_lives()
      self.player.achieve_scores()



   def play (self):
      while True:
         print(f'{self.player.name}: {self.player.lives} |-| {self.enemy.active_lives} :Enemy (level {self.enemy.level})')
         self.fight()



mode = input('Input the difficulty ( 1=ease, 2=medium, 3=hard): ')
name = input('Input the name: ')
player = Player(name, mode)
play = Game(player, mode)
play.play()




#    def fight(self):
#       try:
#          print( f'{self.player.name} -> {self.player.lives} : {self.enemy.active_lives} <- Enemy')

#          answer = self.player.select_attack_item()
#          enemy_answer = self.enemy.select_attack()

#          print(f'{answer} vs. {enemy_answer}')
#          if answer == 'paper' and enemy_answer == 'scissors':
#             self.player.degrees_lives()

#          elif answer == 'paper' and enemy_answer == 'rock':
#             self.enemy.degrees_lives(self.player.achieve_scores())

#          elif answer == 'scissors' and enemy_answer == 'paper':
#             self.enemy.degrees_lives(self.player.achieve_scores())

#          elif answer == 'scissors' and enemy_answer == 'rock':
#             self.player.degrees_lives()

#          elif answer == 'rock' and enemy_answer == 'scissors':
#             self.enemy.degrees_lives(self.player.achieve_scores())

#          elif answer == 'rock' and enemy_answer == 'paper':
#             self.player.degrees_lives()

#          else: print('Draw')
#       except KeyError:
#          print('Incorrect choose!')
#       except ValueError:
#          print("incorrect choose!")


# def play(menu):
#    try:
#       list = open('score_list.txt', 'r')
#       score = Score_finder(list)
#       list.close()

#       if menu == 1:

#          player_name = input('Enter the name:')
#          level_difficulty = int(input('Input the difficulty (1 = ease, 2 = medium, 3 = hard):'))

#          difficulty_name = {1:'ease', 2:'medium', 3: 'hard'}

#          enemy = Enemy(level_difficulty)
#          player = Player(player_name,level_difficulty)
#          game = Game(player, enemy)

#          while game.player.lives != 0:
#             game.fight()

#          record = Player_Record(game.player.name, game.player.score, difficulty_name[game.player.difficulty])

#          if game.player.lives == 0:


#             list1 = open('score_list.txt', 'a')
#             score.write(record.prepare_score(), list1)
#             list1.close()
#             play(int(input('1 - play game, 2 - scores: ')))

#       elif menu == 2:
#          score.read_score()
#          play(int(input('1 - play game, 2 - scores: ')))

#       else:
#          print('What is it?')
#          play(int(input('1 - play game, 2 - scores: ')))

#    except KeyError:
#       print('Incorrect choose')
#       play(int(input('1 - play game, 2 - scores: ')))

#    except ValueError:
#       print('Error')
#       play(int(input('1 - play game, 2 - scores: ')))


# try:
#    play(int(input('1 - play game, 2 - scores: ')))
# except ValueError:
#    print('Error')
#    play(int(input('1 - play game, 2 - scores: ')))
