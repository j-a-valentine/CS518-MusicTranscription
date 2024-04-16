import utils

class Segment:
    def __init__(self, prediction, mp3):
        self.mp3 = mp3
        self.prediction = utils.remove_punctuation(prediction).lower()
        self.transcription = utils.remove_punctuation(prediction).lower()

    def get_mp3(self):
        return self.mp3 

    def get_prediction(self):
        return self.prediction

    def get_transcription(self):
        return self.transcription

    def set_transcription(self, prediction):
        self.transcription = utils.remove_punctuation(prediction).lower()

    def serialize(self):
        return {
            "mp3": self.mp3,
            "prediction": self.prediction,
            "transcription": self.transcription
        }
