# Git
メインブランチ
`main`を安定版とする。このブランチは直接編集しない。

開発用ブランチ
`develop`ブランチを開発用とする。
ここでテストを行い、mainにマージする。

機能ブランチ
`develop`ブランチから派生させ、`develop`ブランチにマージする。
`feature/header-design`
`feature/add-contact-form`
など。

バグ修正用ブランチ
`develop`から切り出し、マージする。
`bugfix/fix-footer-issue`

リリースブランチ
`release/v1.0`
`develop`から切り出し、
（`git checkout develop` → `git checkout -b release/v1.0`）
`main`と`develop`にマージする。

ホットフィックスブランチ
`main`緊急修正用。
`main`から切り出し、`main`と`develop`にマージする。