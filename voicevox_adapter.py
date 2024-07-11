import json
import requests
import io
import soundfile

class VoicevoxAdapter:
    URL = 'http://localhost:50021/'

    def __init__(self) -> None:
        pass

    def __create_audio_query(self, text: str, speaker: int) -> json:
        item_data = {
            'text': text,
            'speaker': speaker
        }
        
        response = requests.post(self.URL + 'audio_query', params=item_data)
        return response.json()

    def __create_request_audio(self, query_data, speaker: int) -> bytes:
        a_params = {
            'speaker': speaker
        }
        headers = {
            'accept': 'audio/wav',
            'Content-Type': 'application/json'
        }
        response = requests.post(self.URL + 'synthesis', params=a_params, headers=headers, data=json.dumps(query_data))
        return response.content


    def get_voice(self, text: str):
        speaker = 3
        query_data = self.__create_audio_query(text, speaker)
        audio_bytes = self.__create_request_audio(query_data, speaker)
        
        audio_stream = io.BytesIO(audio_bytes)
        data, sample_rate = soundfile.read(audio_stream)
        return data, sample_rate

if __name__ == '__main__':
    voicevox = VoicevoxAdapter()
    data, sample_rate = voicevox.get_voice('こんにちは')
    print(sample_rate)
