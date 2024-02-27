MODE_HARD = 'hard'
MODE_MEDIUM = 'medium'
MODE_EASE = 'ease'

MODES = {
   '1': MODE_EASE,
   '2': MODE_MEDIUM,
   '3':MODE_HARD,
}

LIVES = {
   'hard': 1,
   'medium' : 3,
   'ease' : 5,
}

ENEMY_LIVES = {
   'hard' : 4,
   'medium': 3,
   'ease' : 2
}

POINTS_FOR_FIGHT = 2
POINTS_FOR_KILL = 4

SCORE_FILE ='score_list.txt'

PAPER = 'paper'
SCISSORS = 'scissors'
STONE = 'stone'

SELECT_ATTACK = {
   '1': PAPER,
   '2': SCISSORS,
   '3': STONE,
}

WIN = 1
DRAW = 0
LOSE = -1

ATTACK_PAIRS = {
       (PAPER, PAPER): DRAW,
    (PAPER, STONE): WIN,
    (PAPER, SCISSORS): LOSE,
    (STONE, PAPER): LOSE,
    (STONE, STONE): DRAW,
    (STONE, SCISSORS): WIN,
    (SCISSORS, PAPER): WIN,
    (SCISSORS, STONE): LOSE,
    (SCISSORS, SCISSORS): DRAW
}

MAX_RECORDS_NUMBER = 5

REPEATING_PRINT = 0