# class Game:
#    player: player
#    enemy: enemy
#    mode: mode

#    def init(self, player, enemy, mode):

# class Game:

#    def __init__(self,player,enemy):
#       self.player = player
#       self.enemy = enemy

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