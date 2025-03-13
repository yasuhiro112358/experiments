# pip
- 依存関係の管理
- 依存パッケージのインストール
- 依存パッケージの保存
- 依存パッケージのアップデート

```bash
# 依存パッケージのインストール
pip install transformers

# 依存パッケージの保存
# インストールしたパッケージをrequirements.txtに保存できる
pip freeze > requirements.txt

# 依存パッケージのインストール
# requirements.txtに記載されたパッケージをインストールできる
pip install -r requirements.txt

# 依存パッケージのアップデート
pip list --outdated
pip install --upgrade transformers
```
---
[Back to index](../README.md)