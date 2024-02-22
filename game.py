from models import player
from models import enemy

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




game = Game(player, enemy)


def play():
   while game.player.lives != 0:
      game.fight()


play()