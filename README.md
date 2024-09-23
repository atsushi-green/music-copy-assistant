# Music Copy Assistant
耳コピの補助をするためのツールです。MP3ファイルを読み込んで、指定した区間をフーリエ変換することで、周波数成分を動画で可視化します。MacOSでの動作のみ確認しています。例えば、ピアノの「ソ」の音声ファイルを入力すると、以下のような動画が生成されます。

https://github.com/user-attachments/assets/7b185410-3ecd-4d91-b7ce-b44e7f29a88e

# Install
```bash
sudo apt install ffmpeg
rye sync
```

# Preparation
1. 解析したいmp3ファイルを`music`ディレクトリ直下に置く。
2. `setting.yaml`を適宜編集する（`filename`は1.で置いたmp3ファイルの名前）。

# Usage
```bash
sh run.sh
```

# Sample Music
魔王魂 様より [ソ.mp3](https://maou.audio/se_inst_piano2_5so/)

