# python-ffmpeg-svtav1-compressor

## Overview 概要

- This python file compresses video files all at once by using FFmpeg.

  FFmpegを用いて動画ファイルを一括で圧縮する事が出来るPythonファイルです。

- It uses an SVT-AV1 encoder for compression.

  圧縮にはSVT-AV1エンコーダが用いられます。

## Usage 使い方

- Install FFmpeg (version should be over 5.0).

  FFmpegをインストール (5.0以上)

- Install Python.

  Pythonをインストール

- Execute command below.

  以下のコマンドを実行

```sh
python ffmpeg-svtav1.py [path/to/file or directory]
```

## Note 注意点

- The code will generate the svtav1 directory to the video file path to save compressed files.

  このコードを実行すると、動画ファイルと同じパスへ新たに保存用ディレクトリ(svtav1)が追加されます。

- If the compressed file with the same name already exists, it doesn't overwrite. Please remove files from the svtav1 directory before you compress the file again.

  既に同名の圧縮済みファイルが存在する場合、上書きすることはありません。再度圧縮対象にする場合はsvtav1ディレクトリから当該ファイルを取り除いてから、実行し直してください。
