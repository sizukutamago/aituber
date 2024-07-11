import sounddevice as sd
from typing import TypedDict


class PlaySound:
    def __init__(self, output_device_name="MacBook Proのスピーカー") -> None:
        # 指定されたデバイス名に基づいてデバイスIDを取得
        output_device_id = self._search_output_device_id(output_device_name)

        input_device_id = 0

        sd.default.device = [input_device_id, output_device_id]

    def _search_output_device_id(self, output_device_name: str, output_device_host_api = 0) -> int:
        # 利用可能なデバイスの情報を取得
        devices = sd.query_devices()
        output_device_id = None

        # 指定された出力デバイス名とホストAPIに合致するデバイスIDを検索
        for device in devices:
            is_output_device_name = output_device_name in device['name']
            is_output_device_host_api = device['hostapi'] == output_device_host_api
            if is_output_device_name and is_output_device_host_api:
                output_device_id = device['index']
                break

        # 合致するデバイスが見つからなかった場合
        if output_device_id is None:
            print("Device not found: {output_device_name}")
            exit()

        return output_device_id

    def play_sound(self, data, rate) -> bool:
        # 指定されたデータを再生
        sd.play(data, rate)
        sd.wait()
        return True

