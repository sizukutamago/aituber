import requests
import json

url = 'http://localhost:50021/'
text = 'こんにちは'
speaker = 1
item_data = {
    'text': text,
    'speaker': speaker
}

res = requests.post(url + 'audio_query', params=item_data)

res_json = res.json()
print(res_json)

query_data = res_json

a_params = {
    'speaker': speaker,
}

res = requests.post(url + 'synthesis', params=a_params,
                    data=json.dumps(query_data))

print(res.content)
