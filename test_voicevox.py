from voicevox_adapter import VoicevoxAdapter
from play_sound import PlaySound

voicevox = VoicevoxAdapter()
play_sound = PlaySound('スピーカー')

data, sample_rate = voicevox.get_voice('こんにちは')
play_sound.play_sound(data, sample_rate)
