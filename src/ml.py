from openai import OpenAI
from pydub import AudioSegment
import tempfile
from segment import Segment

class AITranscriber:

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def transcribe(self, mp3):
        audio_file = open(mp3, "rb")
        response = self.client.audio.transcriptions.create(model="whisper-1", file=audio_file, response_format="verbose_json", timestamp_granularities=["segment"])
        audio_file.close()
        print(response)
        audio = AudioSegment.from_mp3(mp3)
        segments = []
        for seg in response.segments:
            segment_audio = audio[float(seg["start"]) * 1000 : float(seg["end"]) * 1000]
            temp_file = tempfile.NamedTemporaryFile(suffix='.mp3', dir="./temp", delete=False)
            temp_file_path = temp_file.name
            segment_audio.export(temp_file_path, format='mp3')
            temp_file.close()
            segments.append(Segment(seg["text"], temp_file_path))
        return segments
