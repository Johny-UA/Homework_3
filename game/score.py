from settings import *

class PlayerRecord:
    def __init__(self, name, mode, score):
        self.name = name
        self.mode = mode
        self.score = score

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f"{self.name}, {self.mode}, {self.score}"


class GameRecord:
    def __init__(self):
        self.records = []

    def add_record(self, record) -> None:
        existing_record = next((r for r in self.records if r.name == record.name and r.mode == record.mode), None)
        if existing_record:
            if record > existing_record:
                self.records.remove(existing_record)
                self.records.append(record)
        else:
            self.records.append(record)

    def prepare_records(self, max_records):
        self.records.sort(reverse=True)
        self.records = self.records[:max_records]


class ScoreHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.game_record = GameRecord()
        self.read()

    def read(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                name, mode, score = line.strip().split(',')
                player_record = PlayerRecord(name, mode, int(score))
                self.game_record.add_record(player_record)

    def save(self):
        with open(self.file_name, 'w') as file:
            for record in self.game_record.records:
                file.write(f"{record.name},{record.mode},{record.score}\n")

    def display(self):
         records_length = len(self.game_record.records)
         repeating = REPEATING_PRINT
         while repeating != records_length:
            print(self.game_record.records[repeating])
            repeating += 1


# handler = ScoreHandler(SCORE_FILE)

# new_record = PlayerRecord("McDonalds", "medium", 225)
# handler.game_record.add_record(new_record)

# handler.save()
# handler.display()
