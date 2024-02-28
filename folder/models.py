from .settings import MODES, LIVES, SELECT_ATTACK, MODE_EASE, MODE_MEDIUM, MODE_HARD, POINTS_FOR_FIGHT_EASE, POINTS_FOR_FIGHT_MEDIUM, POINTS_FOR_FIGHT_HARD,ENEMY_ATTACK
from .exceptions import GameOver,EnemyDown

class Player:
   mode: str
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
         raise GameOver()

   def achieve_scores(self) -> None:
         if self.mode == MODE_EASE:
            self.score += POINTS_FOR_FIGHT_EASE
         elif self.mode == MODE_MEDIUM:
            self.score += POINTS_FOR_FIGHT_MEDIUM
         else:
            self.score += POINTS_FOR_FIGHT_HARD






class Enemy:
   _lives: int
   active_lives: int
   level: int

   def __init__(self,lives):
      self._lives = lives
      self.active_lives = self._lives
      self.level = 1

   def select_attack(self) -> None:
      return SELECT_ATTACK[str(ENEMY_ATTACK)]

   def degrees_lives(self) -> None:
      self.active_lives -= 1
      if self.active_lives == 0:
         raise EnemyDown()