# twitter API ラッパ

認証だけ受け持ってAPIをラップしてくれるやつ。  
さすがにフロントからこんなことできないので

## セットアップ

api_keys.py

``` python
API_KEY = ''
API_SECRET_KEY = ''
```

``` bash
$ pip install -r requirements.txt
```

1. `/authenticate`にアクセス
2. ログイン
3. 各APIにアクセス

sessionでトークンを管理してるのでcookie必須。jsから叩くときは気をつけて
