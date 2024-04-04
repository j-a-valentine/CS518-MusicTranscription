from gui import GUI
from playsound import playsound

class GUIController:
    
    def __init__(self, segments):
        self.segments = segments
        self.segment_index = 0
        self.gui = GUI()

    def next_segment(self):
        ai_prediction = self.segments[self.segment_index].get_ai_prediction()
        self.gui.load_window(ai_prediction, self.submit_human_prediction, self.play_audio)
        self.gui.run()

    def submit_human_prediction(self, prediction):
        self.segments[self.segment_index].predict_human(prediction)
    
    def play_audio(self):
        playsound(self.segments[self.segment_index].get_mp3())