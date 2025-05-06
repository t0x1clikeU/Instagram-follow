# Instagram Auto Follows Tool

**Dev: t0x1c**

Instagramの複数アカウントを使用して、指定したユーザーを自動でフォローするツールです。

---

## ⚠️ 注意事項

> このツールはInstagramの利用規約に違反する可能性があります。使用は**自己責任**で行ってください。アカウントの**制限・凍結**のリスクがあります。  

---

## ✅ 主な機能

- アカウントの自動ログイン（セッション保存）
- 指定ユーザーへのフォロー
- フォロー済みチェック
- アカウントBAN（制限）判定
- ログ出力（`follow_log.log`）

---

## 🧾 必要環境

- Python 3.8+
- `instagrapi` ライブラリ

```bash
pip install instagrapi
```


## 📂 ファイル構成
```
├── main.py                 # メインスクリプト
├── acc.txt                 # アカウント情報を記入（ID:PASS）
├── Session/                # セッションファイル保存フォルダ
├── follow_log.log          # ログ出力
```
## 🛠️ 使い方

1.acc.txt にログインさせたいInstagramアカウントを ID:PASS 形式で記入します。

example1@example.com:password123

test:password456

2.スクリプトを実行します



