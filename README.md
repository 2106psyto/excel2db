# Excel to SQLite CLI アプリケーション

## 概要

このツールは、指定した Excel ワークブック（.xlsx）から、各ワークシートを SQLite3 データベースのテーブルとして変換する Python コマンドラインアプリケーションです。

---

## インストール方法

1. 配布された EXE ファイル（例: `excel2sqlite-cli.exe`）をダウンロードします。
2. EXE ファイルを任意のフォルダに配置し、コマンドプロンプトでそのフォルダに移動します。
3. 以下のようにコマンドを実行します:

   ```powershell
   excel2sqlite-cli.exe --excel サンプル.xlsx --config 設定.yaml --output 結果.db
   ```

※ EXE ファイルのパスが通っていれば、どこからでも実行できます。

開発・テスト・ビルド手順は `README.md` の「開発者向け」セクションを参照してください。

---

## 使い方

### コマンド例

```powershell
   excel2sqlite-cli.exe --excel サンプル.xlsx --config 設定.yaml --output 結果.db
```

- `--excel` : 変換元の Excel ファイルパス
- `--config` : YAML 設定ファイルパス
- `--output` : 出力する SQLite3 データベースファイルパス

---

## 設定ファイル（YAML）例

```yaml
worksheets:
  - name: "Sheet1"
    start_cell: "C21"
  - name: "集計"
    start_cell: "A1"
```

- `name` : インポートするワークシート名
- `start_cell` : データテーブルの開始セル（例: "C21", "A1"）

---

## トラブルシューティング

- 設定ファイルの書式が間違っている場合、エラーが表示されます。
- Excel ファイルやシート名が存在しない場合もエラーになります。
- 日本語データもそのまま保存されますが、SQLite クライアントによっては表示に注意してください。

---

## ライセンス

MIT ライセンス

---

## クレジット

- [openpyxl](https://openpyxl.readthedocs.io/)
- [PyYAML](https://pyyaml.org/)
- [jsonschema](https://python-jsonschema.readthedocs.io/)

---

## 開発者向け

1. Python 3.11 以上をインストールしてください。
2. 仮想環境を作成・有効化します（推奨）:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. 必要なパッケージをインストールします:

   ```powershell
   pip install .
   ```
