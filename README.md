# Paper Bookshelf
https://github.com/yuta0821?tab=repositories を自分用にカスタマイズ

[毎日の論文サーベイを手軽に！ChatGPTを活用したSlackへの3行要約通知とNotionデータベース連携](https://qiita.com/yuta0821/items/2edf338a92b8a157af37)

# Usage
## Install

1. git clone後, grobidのinstallを実施
```bash
paper_bookshelf$ wget https://github.com/kermitt2/grobid/archive/0.7.2.zip
paper_bookshelf$ unzip 0.7.2.zip
paper_bookshelf$ cd grobid-0.7.2
paper_bookshelf/grobid-0.7.2$ ./gradlew clean install
```

2. Dockerの起動
```bash
#Dockerイメージ作成
$ docker build . -t paper_bookshelf:test

# Dockerを起動
$ docker run --name bookshelf_container -v /path/to/paper_bookshelf:/workspace/ -it paper_bookshelf /bin/bash
```

3. .env.exampleファイルを参考に.envファイルを作成してAPIのキーを設定してください

4. 最後に環境変数の設定をしてください(Dockerの起動毎に設定)
```bash
export $(cat .env| grep -v "#" | xargs)
```

以下でアプリが起動します
arxiv_id: https://arxiv.org/abs/{arxiv_id}
```bash
python main.py {arxiv_id}
```
