# shokudo
食堂のやつ


## PostgreSQL

### テーブル作成
```SQL
CREATE TABLE *table_name* (*column_name*, *data_type*, ... );
```

### テーブル一覧
```SQL
\dt
```

### テーブルに行を挿入
```SQL
INSERT INTO *table_name* ('*value*','*value*', ...); 
```

### テーブルへ問い合わせ
```SQL
SELECT * FROM *table_name*;
```


## セキュリティリスク対策

### 不正アクセス
クロスサイトリクエストフォージェリ（Cross-Site Request Forgeries）攻撃、クロスサイトスクリプティング（X Site Scripting）攻撃への対策をする
→不正なメニュー情報の変更を防止する

### CSRF
他のサイトからの不正なリクエストを通して、ユーザが意図しない処理が行われる攻撃

#### 対策
入力フォームにトークンを埋め込み、ユーザからデータが送信された時、埋め込まれているトークンがサーバ側で設定したトークンと一致する場合のみリクエストを受け付ける
### XSS
Webサイトの入力フォームから悪意のあるスクリプトを埋め込まれる攻撃

#### 対策
ウェブページの表示に影響する特殊記号（例: 「<」、「>」、「&」など）をエスケープ処理する。

### 情報の盗聴
盗聴に対する保護が必要な個人情報等の貴重なデータが存在しないため、対策せず

### データの破壊・削除
SQLインジェクション攻撃への対策をする
→不正なSQLリクエストによるデータベース内の情報の改竄・消去を防止する

#### 対策
SQL文の組み立てをプレースホルダで実装する。
### さんこうぶんけん
- https://www.ipa.go.jp/security/vuln/websecurity/csrf.html
- https://www.ipa.go.jp/security/vuln/websecurity/cross-site-scripting.html
- https://www.ipa.go.jp/security/vuln/websecurity/sql.html
