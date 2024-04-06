import os
from song_controller import SongController
from ml import AITranscriber
from dotenv import dotenv_values
os.environ['TK_SILENCE_DEPRECATION'] = '1'


def main():
    t = AITranscriber(dotenv_values()["OPENAI_API_KEY"])
    segments = t.transcribe_complex("./audio/blindinglights.mp3")
    controller = SongController(segments)
    controller.run_song()



    print("done")




if __name__ == "__main__":
    main()
