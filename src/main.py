import os
from segment import Segment
from song_controller import SongController
from ml import AITranscriber
from dotenv import dotenv_values
os.environ['TK_SILENCE_DEPRECATION'] = '1'


def main():
    t = AITranscriber(dotenv_values()["OPENAI_API_KEY"])
    segments = t.transcribe("./audio/adele.mp3")
    controller = SongController(segments)
    controller.run_song()


    print("done")




if __name__ == "__main__":
    main()
