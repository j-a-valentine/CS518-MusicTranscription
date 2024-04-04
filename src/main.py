import os
from segment import Segment
from gui_controller import GUIController
os.environ['TK_SILENCE_DEPRECATION'] = '1'


def main():
    segment1 = Segment("some test lyrics", "./audio/firework.mp3")
    segment1.predict_ai("baby your a firework")
    controller = GUIController([segment1])
    controller.next_segment()




if __name__ == "__main__":
    main()