import os
from segment import Segment
from song_controller import SongController
os.environ['TK_SILENCE_DEPRECATION'] = '1'


def main():
    # segment1 = Segment("some test lyrics", "./audio/firework.mp3")
    # segment2 = Segment("heres more lyrics", "./audio/firework.mp3")
    # segment1.predict_ai("baby your a firework")
    # segment2.predict_ai("come on loser")
    # controller = SongController([segment1, segment2])
    # controller.run_song()

    # print(segment1.human_prediction)
    # print(segment2.human_prediction)
    print("done")




if __name__ == "__main__":
    main()