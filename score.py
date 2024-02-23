class Score_finder:
   record_list: list


   def __init__(self,list):
      self.record_list = list.read()


   def write(self, other, list):
      self.record_list = self.record_list + other
      list.write(other)



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


   def prepare_score(self):
      return f' {self.name} , {self.score} , {self.mode}; '

