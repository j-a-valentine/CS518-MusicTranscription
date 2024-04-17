import os
import sys
import json
from aggregate import Aggregator

def main():
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <song_name>")
        return
    for directory in ['./audio', './data', './temp', './output']:
        if not os.path.exists(directory):
            os.makedirs(directory)
    song = sys.argv[1]
    if not os.path.exists(f"./data/{song}.json"):
        print(f"{song}.json could not be found in ./data")
        return
    if len(sys.argv) > 2 and sys.argv[2] == "pipeline":
        method = 1
    else:
        method = 0
    with open(f"./data/{song}.json", "r") as json_file:
        json_data = json.load(json_file)
    a = Aggregator(json_data)
    if method == 0:
        lyrics = a.aggregate_majority()
    else:
        lyrics = a.aggregate_pipeline()
    with open(f"./output/{song}.txt", "w") as output_file:
        for line in lyrics:
            output_file.write(line + "\n") 
        
if __name__ == "__main__":
    main()