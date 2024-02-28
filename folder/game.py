from .settings import MODES, ENEMY_LIVES, ATTACK_PAIRS, WIN, DRAW, LOSE, SCORE_FILE, ADDING_LEVEL
from .models import Player, Enemy
from .score import PlayerRecord,  ScoreHandler
from .exceptions import GameOver, EnemyDown


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
         try:
            self.fight()
         except GameOver:
            handler = ScoreHandler(SCORE_FILE)
            new_record = PlayerRecord(self.player.name, self.mode,self.player.score)
            handler.game_record.add_record(new_record)
            handler.save()
            print('You lose!')
            print(f"{self.player.name}'s score is {self.player.score} points")
            break
         except EnemyDown:
            self.enemy.active_lives = self.enemy._lives + self.enemy.level
            self.enemy.level += ADDING_LEVEL
            print('You dit it! The enemy is defeated.')
         except KeyError:
            print('Bad choice')


# ! handler.display()
