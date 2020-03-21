# twitter API ラッパ

認証だけ受け持ってAPIをラップしてくれるやつ。  
さすがにフロントからこんなことできないので

## セットアップ

api_keys.pyみて環境変数設定

``` bash
$ pip install -r requirements.txt
```

使うAPIリストをmake.pyに記述

``` bash
$ python make.py
```

1. `/authenticate`にアクセス
2. ログイン
3. 各APIにアクセス

sessionでトークンを管理してるのでcookie必須。jsから叩くときは気をつけて
