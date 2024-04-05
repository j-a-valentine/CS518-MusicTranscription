from gui import GUI
import os
import pygame

class SongController:
    
    def __init__(self, segments):
        self.segments = segments
        self.segment_index = -1
        self.gui = GUI()
        pygame.mixer.init()

    def run_song(self):
        self.next_segment()
        self.gui.run()

    def next_segment(self):
        self.stop_audio()
        self.segment_index += 1
        if self.segment_index < len(self.segments):
            ai_prediction = self.segments[self.segment_index].get_ai_prediction()
            self.gui.load_window(ai_prediction, self.submit_human_prediction, self.play_audio)
        else:
            self.gui.stop()

    def submit_human_prediction(self, prediction):
        self.segments[self.segment_index].predict_human(prediction)
        self.next_segment()
    
    def play_audio(self):
        pygame.mixer.music.load(self.segments[self.segment_index].get_mp3())
        pygame.mixer.music.play()

    def stop_audio(self):
        pygame.mixer.music.stop()
    