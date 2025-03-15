# venv
- 仮想環境の作成
- 仮想環境を作成することで、プロジェクトごとに環境を分けることができる
- 仮想環境を有効化することで、プロジェクトごとに異なる依存パッケージを使用できる
- Python標準ライブラリのvenvモジュールを使用することで、仮想環境を作成できる
- Python自体のバージョン管理は、[pyenv](pyenv.md)で行う

```bash
# 仮想環境の作成
# -mオプションは指定されたモジュール（この場合はvenv）を実行するために使用される
# venvは作成する仮想環境のディレクトリ名
python3 -m venv venv

# 仮想環境の有効化
source backend/venv/bin/activate

# 仮想環境の無効化
deactivate

# 仮想環境の有効化の確認
# 仮想環境の有効化が成功している場合、仮想環境のパスが表示される
echo $VIRTUAL_ENV

```

## シェルの設定
必要に応じて、シェルの設定ファイル（~/.bashrc または ~/.zshrc ）に以下の設定を追加する
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

---
[Back to index](../README.md)