class Segment:
    def __init__(self, lyrics, mp3):
        self.lyrics = lyrics
        self.mp3 = mp3
        self.ai_prediction = ""
        self.humman_prediction = ""

    def get_mp3(self):
        return self.mp3 

    def get_ai_prediction(self):
        return self.ai_prediction

    def get_human_prediction(self):
        return self.human_prediction

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