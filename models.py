from random import randint

class Player:
   items = {1:'paper', 2:'scissors', 3:'rock'}
   live_difficulty = {1:3,2:2,3:1}
   difficulty: int
   name: str
   score = 0
   lives: int

   def __init__(self, name, difficulty):
      self.name = name
      self.lives = self.live_difficulty[difficulty]
      self.difficulty = difficulty

   def select_attack_item(self):
      return self.items[int(input("Select an item (1-paper, 2-scissors, 3-rock):"))]
   

   def degrees_lives(self):
      self.lives -= 1
      if self.lives ==0:
         print('Game over')
         print(self.score)


   def achieve_scores(self):
         self.score += level_difficulty


class Enemy:
   _lives: int
   active_lives: int
   level: int
   items = {1:'paper', 2:'scissors', 3:'rock'}

   def __init__(self,lives_and_level):
      self.active_lives = lives_and_level
      self._lives = lives_and_level
      self.level = lives_and_level

   def select_attack(self):
      return self.items[randint(1,3)]

   def degrees_lives(self,add_score):
      self.active_lives -= 1
      if self.active_lives == 0:
         add_score
         print('You win')
         self.active_lives = self._lives + self.level
         self.level += 1





player_name = input('Enter the name:')
level_difficulty = int(input('Input the difficulty (1 = ease, 2 = medium, 3 = hard):'))
enemy = Enemy(level_difficulty)
player = Player(player_name,level_difficulty)


# print(f'{player.select_attack_item(int(input("Select an item (1-paper, 2-scissors, 3-rock):")))} vs. {enemy.select_attack(randint(1,3))}')

# player.degrees_lives()
# player.degrees_lives()
