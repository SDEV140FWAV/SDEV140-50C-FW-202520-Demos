class Student:
    def __init__(self,name, number_of_scores):
        self.name = name
        self.scores = []
        for count in range(number_of_scores):
            self.scores.append(0)

    def get_name(self):
        return self.name