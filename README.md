# Excel to SQLite CLI アプリケーション

## 概要

このツールは、指定した Excel ワークブック（.xlsx）から、各ワークシートを SQLite3 データベースのテーブルとして変換する Python コマンドラインアプリケーションです。

---

## インストール方法

### オプション 1: pip でインストール（推奨）

Python 3.11 以上がインストールされている必要があります。

```powershell
pip install excel2sqlite_cli-0.1.0-py3-none-any.whl
```

インストール後、コマンドラインから直接実行できます:

```powershell
excel2sqlite --excel サンプル.xlsx --config 設定.yaml --output 結果.db
```

### オプション 2: 開発版として実行

プロジェクトディレクトリで:

```powershell
pip install -e .
excel2sqlite --excel サンプル.xlsx --config 設定.yaml --output 結果.db
```

---

## 使い方

### コマンド例

```powershell
excel2sqlite --excel サンプル.xlsx --config 設定.yaml --output 結果.db
```

または wheel をインストールしない場合:

```powershell
python -m excel2sqlite_cli.main --excel サンプル.xlsx --config 設定.yaml --output 結果.db
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

### セットアップ

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

### ビルド方法

#### オプション 1: Python パッケージのみビルド（推奨）

uv を使用して wheel と sdist をビルド:

```powershell
uv build
```

**出力:**

- `dist/excel2sqlite_cli-0.1.0-py3-none-any.whl` - Python wheel（配布用）
- `dist/excel2sqlite_cli-0.1.0.tar.gz` - ソース配布

この wheel を配布ユーザーが `pip install` でインストールできます。

#### オプション 2: スタンドアロン実行ファイルのビルド（非推奨）

PyInstaller を使用してスタンドアロン .exe ファイルをビルドすることもできますが、一部のセキュリティソフトウェアが false positive を報告する場合があります。

```powershell
python build_exe.py --standalone
```

**注意:** PyInstaller で生成された exe ファイルは、セキュリティソフトウェア（Windows Defender など）により、誤ってマルウェアとして検出される場合があります。これは PyInstaller の仕様上の制限であり、実際にはマルウェアではありません。そのため、配布には Python wheel の使用をお勧めします。

#### オプション 3: 完全ビルド（Wheel + exe）

```powershell
python build_all.py
```

**出力:**

- `dist/excel2sqlite_cli-0.1.0-py3-none-any.whl` - Python wheel
- `dist/excel2sqlite_cli-0.1.0.tar.gz` - ソース配布
- `dist/excel2sqlite_cli.exe` - スタンドアロン実行ファイル（セキュリティ警告の可能性あり）

前回のビルドを削除してから実行する場合:

```powershell
python build_all.py --clean
```
