from random import randint
from settings import *
from exceptions import GameOver,EnemyDown

class Player:
   difficulty: int
   name: str
   score: int = 0
   lives: int

   def __init__(self, name,mode):
      self.name = name
      self.mode = MODES[mode]
      self.lives = LIVES[self.mode]

   def select_attack_item(self) -> None:
      return SELECT_ATTACK[input("Select an item (1-paper, 2-scissors, 3-rock):")]
   

   def degrees_lives(self) -> None:
      self.lives -= 1
      if self.lives == 0:
         GameOver(self,'hello')

   def achieve_scores(self) -> None:
         self.score += self.mode





class Enemy:
   _lives: int
   active_lives: int
   level: int

   def __init__(self,lives):
      self._lives = lives
      self.active_lives = self._lives
      self.level = 1

   def select_attack(self) -> None:
      return SELECT_ATTACK[str(randint(1,3))]

   def degrees_lives(self) -> None:
      self.active_lives -= 1
      if self.active_lives == 0:
         EnemyDown(self)




# player = Player('Ivan', '3')
# enemy = Enemy(ENEMY_LIVES[MODES['1']])
# print(enemy.select_attack())
# print(player.select_attack_item())
# player.degrees_lives()
# print(enemy.active_lives)
# enemy.degrees_lives()
# enemy.degrees_lives()
# print(enemy.active_lives)