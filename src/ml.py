from openai import OpenAI
from pydub import AudioSegment
import tempfile
from segment import Segment

class AITranscriber:

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def transcribe_simple(self, mp3):
        audio_file = open(mp3, "rb")
        response = self.client.audio.transcriptions.create(model="whisper-1", file=audio_file, response_format="verbose_json", timestamp_granularities=["segment"])
        audio_file.close()
        audio = AudioSegment.from_mp3(mp3)
        segments = []
        for seg in response.segments:
            segment_audio = audio[round(float(seg["start"]) * 1000) : round(float(seg["end"]) * 1000)]
            temp_file = tempfile.NamedTemporaryFile(suffix='.mp3', dir="./temp", delete=False)
            temp_file_path = temp_file.name
            segment_audio.export(temp_file_path, format='mp3')
            temp_file.close()
            segments.append(Segment(seg["text"], temp_file_path))
        return segments

    def debug(self, response):
        word_count = []
        for word in response.words:
            word_count.append(word["word"])
        segments_words_count = []
        for seg in response.segments:
            for word in seg["text"].strip().split(" "):
                segments_words_count.append(word)
        print("Words")
        print(word_count)
        print("Segments")
        print(segments_words_count)
        print(f"{len(word_count)} {len(segments_words_count)}")

    def transcribe_complex(self, mp3):
        audio_file = open(mp3, "rb")
        response = self.client.audio.transcriptions.create(model="whisper-1", file=audio_file, response_format="verbose_json", timestamp_granularities=["segment", "word"])
        audio_file.close()
        audio = AudioSegment.from_mp3(mp3)
        current_word_index = 0
        response_segments = response.segments
        response_words = response.words
        segments = []
        for seg in response_segments:
            words = seg["text"].strip().split(" ")
            words = [word for word in words if word != ""]
            start = response_words[current_word_index]["start"]
            current_word_index += len(words)
            end = response_words[current_word_index-1]["end"]
            segment_audio = audio[round(float(start) * 1000) : round(float(end) * 1000)]
            temp_file = tempfile.NamedTemporaryFile(suffix='.mp3', dir="./temp", delete=False)
            temp_file_path = temp_file.name
            segment_audio.export(temp_file_path, format='mp3')
            temp_file.close()
            segments.append(Segment(words, temp_file_path))
        return segments



       
