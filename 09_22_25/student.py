class Student:
    def __init__(self,name, number_of_scores):
        self.name = name
        self.scores = []
        for count in range(number_of_scores):
            self.scores.append(0)

    def get_name(self):
        return self.name
    
    def set_score(self, i, score):
        if i <= len(self.scores) and i > 0:
            if score >= 0 and score <= 100:
                self.scores[i-1] = score

    def __str__(self):
        return f"Name: {self.name}\nScores: {self.scores}"