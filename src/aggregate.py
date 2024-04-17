import random
import utils


class Aggregator:

    def __init__(self, json_data):
        self.json_data = json_data
        self.num_transcriptions = len(json_data)
        self.num_segments = len(json_data[0])

    def aggregate_majority(self):
        lyrics = []
        for i in range(self.num_segments):
            best_transcription = ""
            best_similarity_score = -1
            for j in range(self.num_transcriptions):
                total_similarity_score = 0
                current = self.json_data[j][i]["transcription"]
                for k in range(self.num_transcriptions):
                    compare = self.json_data[k][i]["transcription"]
                    total_similarity_score += utils.get_similarity_score(current, compare)
                if total_similarity_score > best_similarity_score:
                    best_similarity_score = total_similarity_score
                    best_transcription = current
                elif total_similarity_score == best_similarity_score:
                    if random.random() < 0.5:
                        best_similarity_score = total_similarity_score
                        best_transcription = current
            lyrics.append(best_transcription)
        return lyrics
    
    def aggregate_pipeline(self):
        segment_data = self.json_data[len(self.json_data) - 1]
        lyrics = []
        for segment in segment_data:
            lyrics.append(segment["transcription"])
        return lyrics