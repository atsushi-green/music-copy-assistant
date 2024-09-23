from pathlib import Path

import yaml
from moviepy.editor import AudioFileClip, VideoFileClip
from path_setting import no_sound_video_path, target_audio_path

with open("setting.yaml", "r") as yml:
    config = yaml.safe_load(yml)

# 音声なしのビデオファイルを読み込む
# VideoFileClipはstrしか読み込めないので、strに変換
video_clip = VideoFileClip(str(no_sound_video_path))
# 音声ファイルを読み込む
audio_clip = AudioFileClip(str(target_audio_path))

# FFT画像の動画と音声の長さが一致しているか確認
assert video_clip.duration == audio_clip.duration

# ビデオクリップに音声をセット
video_clip = video_clip.set_audio(audio_clip)

# 音声付きのビデオファイルとして保存
filename = Path(config["filename"]).stem  # 拡張子を除いたファイル名
start_sec = config["start_sec"]
end_sec = config["end_sec"]
save_path = f"{filename}_fft_{start_sec}-{end_sec}.mp4"
video_clip.write_videofile(save_path, audio_codec="aac")
