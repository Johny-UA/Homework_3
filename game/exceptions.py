def GameOver (player,play):
   print(f"your score is {player.score} points")
   print(play)

def EnemyDown(enemy):
   enemy.active_lives = enemy._lives + enemy.level