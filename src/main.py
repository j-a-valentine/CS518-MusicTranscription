import os
import sys
import json
from song_controller import SongController
from ml import AITranscriber
from dotenv import dotenv_values
from segment import Segment
os.environ['TK_SILENCE_DEPRECATION'] = '1'

def main():
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <song_name>")
        return
    for directory in ['./audio', './data', './temp']:
        if not os.path.exists(directory):
            os.makedirs(directory)
    song = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "pipeline":
        method = 1
    else:
        method = 0
    if os.path.exists(f"./data/{song}.json"):
        with open(f"./data/{song}.json", "r") as json_file:
            json_data = json.load(json_file)
        if method == 0:
            segments = []
            for json_segment in json_data[0]:
                segments.append(Segment(json_segment["prediction"], json_segment["mp3"]))
        else:
            segments = []
            for json_segment in json_data[len(json_data)-1]:
                segments.append(Segment(json_segment["transcription"], json_segment["mp3"]))
        
    else:
        json_data = []
        t = AITranscriber(dotenv_values()["OPENAI_API_KEY"])
        segments = t.transcribe_complex(f"./audio/{song}.mp3")
    controller = SongController(segments)
    controller.run_song()
    json_segments = [segment.serialize() for segment in segments]
    with open(f"./data/{song}.json", "w") as json_file:
        json_data.append(json_segments)
        json.dump(json_data, json_file, indent=4)


    
   



    print("done")




if __name__ == "__main__":
    main()
