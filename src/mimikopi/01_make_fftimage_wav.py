import os

import japanize_matplotlib  # noqa
import matplotlib.pyplot as plt
import numpy as np
import yaml
from path_setting import (
    dir_fft_images,
    dir_input_music,
    target_audio_path,
    tmp_wav_path,
)
from pydub import AudioSegment
from scipy.fft import fft
from scipy.io import wavfile
from sound import SOUND_LIST

with open("setting.yaml", "r") as yml:
    config = yaml.safe_load(yml)

# mp3ファイルの読み込みと指定時間区間の抽出
filepath = dir_input_music / config["filename"]
audio = AudioSegment.from_mp3(filepath)
start_sec = config["start_sec"]
end_sec = config["end_sec"]
duration_ms = config["duration_ms"]

start_time = int(start_sec * 1000)
end_time = int(end_sec * 1000)


def main():
    # 過去に作成したfft_imagesを削除
    delete_prev_fft_images()

    time = start_time
    sound_list = []
    while time <= end_time:
        audio_segment = audio[time : time + duration_ms]
        fft_image(audio_segment, time, time + duration_ms)
        sound_list.append(audio_segment)
        time += duration_ms

    # 音声の保存
    combined_audio = sum(sound_list)
    combined_audio.export(target_audio_path, format="wav")


def delete_prev_fft_images():
    # Delete all .png files in the fft_images directory
    filepaths = dir_fft_images.glob("*.png")
    for filepath in filepaths:
        os.remove(filepath)


def fft_image(audio_segment, start: int, end: int):
    # wavファイルに変換して保存
    audio_segment.export(tmp_wav_path, format="wav")
    # wavファイルを読み込み
    sample_rate, audio_data = wavfile.read(tmp_wav_path)

    # フーリエ変換
    fft_result = fft(audio_data)
    frequencies = np.fft.fftfreq(len(fft_result), 1 / sample_rate)

    # 結果の可視化
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(
        frequencies[: len(frequencies) // 2], np.abs(fft_result)[: len(fft_result) // 2]
    )
    max_amp = np.max(np.abs(fft_result))
    y_pos1 = ax.get_ylim()[1]
    y_pos2 = ax.get_ylim()[1] - ax.get_ylim()[1] // 20
    for i, sound in enumerate(SOUND_LIST):
        y_pos = y_pos2 if i % 2 == 0 else y_pos1
        ax.axvline(x=sound.freq, ymin=0, ymax=max_amp, color="#F26649", linestyle="--")
        ax.text(
            sound.freq,
            y_pos,
            sound.note,
            rotation=0,
            verticalalignment="bottom",
        )
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude")
    ax.set_xlim(0, 1000)
    filename = config["filename"]
    fig.suptitle(f"{filename} ({start_sec} - {end_sec} sec)")
    fig.savefig(dir_fft_images / f"{start}-{end}.png")
    plt.close()


if __name__ == "__main__":
    main()
    main()


if __name__ == "__main__":
    main()
    main()
