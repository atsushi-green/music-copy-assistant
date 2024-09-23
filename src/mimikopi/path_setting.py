from pathlib import Path

dir_home = Path(__file__).resolve().parent.parent.parent
dir_input_music = dir_home / "music"
dir_fft_images = dir_home / "fft_images"
dir_tmp = dir_home / "tmp"
tmp_wav_path = dir_tmp / "tmp.wav"
target_audio_path = dir_tmp / "target_audio.mp3"
no_sound_video_path = dir_tmp / "output_no_sound.mp4"
