from models import Player
from models import Enemy
from score import Player_Record
from score import Score_finder

class Game:

   def __init__(self,player,enemy):
      self.player = player
      self.enemy = enemy

   def fight(self):
      print( f'{self.player.name} -> {self.player.lives} : {self.enemy.active_lives} <- Enemy')
      answer = self.player.select_attack_item()
      enemy_answer = self.enemy.select_attack()
      print(f'{answer} vs. {enemy_answer}')
      if answer == 'paper' and enemy_answer == 'scissors':
         self.player.degrees_lives()
      elif answer == 'paper' and enemy_answer == 'rock':
         self.enemy.degrees_lives(self.player.achieve_scores())
      elif answer == 'scissors' and enemy_answer == 'paper':
         self.enemy.degrees_lives(self.player.achieve_scores())
      elif answer == 'scissors' and enemy_answer == 'rock':
         self.player.degrees_lives()
      elif answer == 'rock' and enemy_answer == 'scissors':
         self.enemy.degrees_lives(self.player.achieve_scores())
      elif answer == 'rock' and enemy_answer == 'paper':
         self.player.degrees_lives()
      else: print('Draw')



def play(menu):


   list = []
   score = Score_finder(list)


   if menu == 1:

      player_name = input('Enter the name:')
      level_difficulty = int(input('Input the difficulty (1 = ease, 2 = medium, 3 = hard):'))

      enemy = Enemy(level_difficulty)
      player = Player(player_name,level_difficulty)
      game = Game(player, enemy)
      record = Player_Record(game.player.name, game.player.score, game.player.difficulty)
      while game.player.lives != 0:
         game.fight()
      if game.player.lives == 0:
         score.write(record)
         play(int(input('1 - play game, 2 - scores: ')))
   elif menu == 2:
      pass


play(int(input('1 - play game, 2 - scores: ')))