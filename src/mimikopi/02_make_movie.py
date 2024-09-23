import cv2
from path_setting import dir_fft_images, no_sound_video_path

# フォルダ内の画像ファイルを取得
img_paths = list(dir_fft_images.glob("*.png"))
img_paths.sort()  # ファイル名でソート


# 最初の画像を読み込んでビデオプロパティを設定
frame = cv2.imread(img_paths[0])
height, width, layers = frame.shape
fps = 20  # 1秒あたりのフレーム数

# VideoWriterオブジェクトを作成
fourcc = cv2.VideoWriter_fourcc(*"avc1")

video = cv2.VideoWriter(no_sound_video_path, fourcc, fps, (width, height))

# 各画像をビデオに追加
for img_path in img_paths:
    frame = cv2.imread(img_path)
    video.write(frame)

# ビデオを保存して終了
video.release()
print(f"{no_sound_video_path} が作成されました。")
