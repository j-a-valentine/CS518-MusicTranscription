class Segment:

    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.ai_prediction = ""
        self.humman_prediction = ""

    def predict_ai(self, prediction):
        self.ai_prediction = prediction

    def predict_human(self, prediction):
        self.human_prediction = prediction

    def score_human(self):
        return self.score(self.lyrics, self.human_prediction)

    def score_ai(self):
        return self.score(self.lyrics, self.ai_prediction)

    def score(self, truth, prediction):
        score = 0
        truth = truth.split(" ")
        prediction = prediction.split(" ")
        for i in range(len(truth)):
            for j in range(len(prediction)):
                if truth[i] == prediction[j]:
                    score += 1
                    break
        score = score / len(truth)
        return score