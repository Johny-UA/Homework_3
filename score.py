class Score_finder:
   record_list: list


   def __init__(self):
      self.record_list = []


   def write(self, other):
      self.record_list.append(other)


   def read_score(self):
      print(self.record_list)



class Player_Record:
   name: str
   score: int
   mode: str


   def __init__(self, name, score, mode):
      self.name = name
      self.score = score
      self.mode = mode


class Game_Record(Player_Record):


   def prepare_score(self):
      return [self.name,self.score,self.mode]



record = Game_Record('Ivan', 10, 'hard')
record1 = Game_Record('Ivan', 25, 'medium')
record2 = Game_Record('Anton', 50, 'ease')

score_list = Score_finder()

score_list.write(record.prepare_score())
score_list.write(record1.prepare_score())
score_list.write(record2.prepare_score())

score_list.read_score()