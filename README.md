# コーデックス‐20250604
ここにプロジェクトの説明を書きます。

## 家計簿アプリ
`kakeibo.py` は簡単な家計簿アプリです。Python3 が実行できる環境で以下のように使います。

### 使い方
- 収入を追加する
  ```bash
  python3 kakeibo.py add -t income -a 50000 -c salary -d "給与"
  ```
- 支出を追加する
  ```bash
  python3 kakeibo.py add -t expense -a 2000 -c food -d "ランチ"
  ```
- 記録を一覧表示する
  ```bash
  python3 kakeibo.py list
  ```
- 収支を確認する
  ```bash
  python3 kakeibo.py balance
  ```

記録は `kakeibo.json` というファイルに保存されます。
