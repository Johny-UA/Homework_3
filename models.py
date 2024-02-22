from random import randint

class Player:
   items = {1:'paper', 2:'scissors', 3:'rock'}
   live_difficulty = {1:3,2:2,3:1}
   name: str
   score = 0
   lives: int

   def __init__(self, name, difficulty):
      self.name = name
      self.lives = self.live_difficulty[difficulty]

   def select_attack_item(self, item):
      return self.items[item]
   

   def degrees_lives(self):
      self.lives -= 1
      if self.lives ==0:
         print('Game over')
         pass

   def achieve_scores(self, enemy_lives, scores_per_difficulty):
      if enemy_lives == 0:
         self.scores += scores_per_difficulty



class Enemy:
   _lives: int
   active_lives: int
   level: int
   items = {1:'paper', 2:'scissors', 3:'rock'}

   def __init__(self,lives_and_level):
      self.active_lives = lives_and_level
      self._lives = lives_and_level
      self.level = lives_and_level

   def select_attack(self,item):
      return self.items[item]

   def degrees_lives(self):
      self.active_lives -= 1
      if self.active_lives == 0:
         print('You win')
         self.active_lives = self._lives + self.level
         self.level += 1





enemy = Enemy(1)
player = Player('Ivan',2)


item1 = int(input('Select an item (1-paper, 2-scissors, 3-rock):'))
item2 = randint(1,3)
print(f'{player.select_attack_item(item1)} vs. {enemy.select_attack(item2)}')

player.degrees_lives()
player.degrees_lives()

enemy.degrees_lives()
enemy.degrees_lives()
print(enemy.active_lives)