# ファイル操作ツール: `file_manipulator.py`

`file_manipulator.py` は、ファイルに対して便利な操作を実行できるPythonスクリプトです。以下の機能をサポートしています：

1. **ファイル内容の逆順変換**  
2. **ファイルのコピー**  
3. **ファイル内容の複製**  
4. **ファイル内の文字列置換**  

---

## 使用方法

このスクリプトは **コマンドライン** から実行します。

### 基本構文

```bash
python3 file_manipulator.py <command> <arguments...>
```

- **`<command>`**: 実行するコマンド名（`reverse`, `copy`, `duplicate-contents`, `replace-string`）。
- **`<arguments>`**: コマンドごとに必要な引数を指定します。

---

## コマンド一覧

### 1. `reverse`

指定したファイルの内容を逆順にし、結果を新しいファイルとして保存します。

**構文**:
```bash
python3 file_manipulator.py reverse <inputpath> <outputpath>
```

**引数**:
- `inputpath`: 入力ファイルのパス。
- `outputpath`: 出力ファイルのパス。

**例**:
```bash
python3 file_manipulator.py reverse input.txt reversed_output.txt
```
- `input.txt` の内容を逆順にして `reversed_output.txt` に保存します。

---

### 2. `copy`

指定したファイルをコピーして、新しいファイルとして保存します。

**構文**:
```bash
python3 file_manipulator.py copy <inputpath> <outputpath>
```

**引数**:
- `inputpath`: 入力ファイルのパス。
- `outputpath`: コピー先のファイルのパス。

**例**:
```bash
python3 file_manipulator.py copy input.txt copy_output.txt
```
- `input.txt` をコピーして `copy_output.txt` に保存します。

---

### 3. `duplicate-contents`

ファイルの内容を指定回数複製し、その内容を同じファイルに上書きします。

**構文**:
```bash
python3 file_manipulator.py duplicate-contents <inputpath> <n>
```

**引数**:
- `inputpath`: 入力ファイルのパス。
- `n`: ファイル内容を複製する回数（整数）。

**例**:
```bash
python3 file_manipulator.py duplicate-contents input.txt 3
```
- `input.txt` の内容を3回複製して上書き保存します。

---

### 4. `replace-string`

指定した文字列を新しい文字列に置き換えます。

**構文**:
```bash
python3 file_manipulator.py replace-string <inputpath> <needle> <newstring>
```

**引数**:
- `inputpath`: 入力ファイルのパス。
- `needle`: 検索する文字列。
- `newstring`: 置き換える新しい文字列。

**例**:
```bash
python3 file_manipulator.py replace-string input.txt oldword newword
```
- `input.txt` 内の `oldword` を `newword` に置き換えます。

---

## 実行例まとめ

1. **ファイル内容の逆順変換**:
    ```bash
    python3 file_manipulator.py reverse input.txt output.txt
    ```

2. **ファイルのコピー**:
    ```bash
    python3 file_manipulator.py copy input.txt output_copy.txt
    ```

3. **ファイル内容の複製**:
    ```bash
    python3 file_manipulator.py duplicate-contents input.txt 2
    ```

4. **文字列の置換**:
    ```bash
    python3 file_manipulator.py replace-string input.txt needle newstring
    ```

---

## 注意事項

- 入力ファイル（`inputpath`）が存在することを確認してください。
- 上書き保存が発生する場合があるため、重要なファイルのバックアップを事前に取得してください。

---

## 動作環境

- **Python3 3.x** がインストールされていること。
- 必要なモジュールは標準ライブラリのみです。

---
