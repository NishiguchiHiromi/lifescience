# インストール
- Docker
  - https://qiita.com/zaki-lknr/items/db99909ba1eb27803456
- git
  - https://prog-8.com/docs/git-env-win

# 環境構築
- ソースコードのダウンロード
  - `git clone git@github.com:NishiguchiHiromi/lifescience.git`

- 仮想環境立ち上げ
  - `cd lifescience`
  - `docker compose up`

- 仮想環境の中に入る
  - 別タブでlifescienceのフォルダに行く
  - `docker compose exec app bash`

# 実行
- `python main.py`
  
# 修正の変更をgithubにpush
 - `git add .`
 - `git commit -m "【適当なメモ】"`
 - `git push origin main`