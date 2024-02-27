def GameOver (player):
   print(f"your score is {player.score} points")

def EnemyDown(enemy):
   enemy.active_lives = enemy._lives + enemy.level