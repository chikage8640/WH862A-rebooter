# WH862A用 自動再起動スクリプト

## なんこれ
コミュファで使われてるONU一体型ルーター「WH862A」を再起動するスクリプト。  
コミュファ光ではルーターを再起動するとグローバルIPが変わるので、なんやかんやで鯖から自動で再起動かけたいときに使います。

## 動作環境
Docker composeが使えればどんな環境でも動くはず。  
一応手元の環境はこんな感じ。

- Ubuntu Server 22.04.3
- Docker version 24.0.6, build ed223bc

あ、あともちろんだけどルーターの管理コンソールにアクセスできるネットワークで実行してね。

## 使い方
事前準備として、docker-compose.ymlと同じディレクトリに.envファイルを作っといてください。中身は以下の通り。
```
ROUTER_IP=192.168.0.1 # ルーターのipアドレス（大抵は192.168.0.1のはず）
PASSWORD=hogehoge # ルーターの管理コンソールのパスワード
```

そしたら以下のコマンドを実行。

```
docker compose up --abort-on-container-exit
```

これで勝手に再起動します。  
ちなみに`--abort-on-container-exit`つけないとseleniumが起動しっぱなしになるので注意。

あとはcronで実行するなりお好きにお使いください。

ちなみに自分は以下のコマンドをcronに書いてます。

```
docker compose -f /home/chikage/router_reboot/docker-compose.yml up --abort-on-container-exit; sleep 40; ddclient
```

## 中身どうなっとるん

やってることはseleniumで管理コンソールにアクセスして再起動ボタン押してるだけです。

ルーターの管理コンソールのHTMLちょっと読んだんですけど、どうもJSが発火するだけの処理とかではない感じだったので解析してPOSTとかはあきらめてます。  
（どうも不可視のチェックボックスとテキストボックスが配置されてて、そこにセッションIDなるものが入ってるっぽい。POSTの通信キャプチャしてみたけどヘッダー無しとか言われてしまったのでめんどくてそれ以上やってない。あとはだれかやってくれ。）

時間ある人は管理ページのソース読んでみるとおもしろいかも。頭に「雀の往来」って書かれてたり、DSのブラウザの対応が書かれてたり、MacのIE用の実装とかいう古代遺産があったり、ラジバンダリ……とその古さを感じさせるいいコードとなっております（笑）  
というかいいかげんCTCはルーターを更新してくれてもいいんじゃありませんの？  
10Gbpsプランにしないとルーターが11ax対応品にならないのはまあ10000歩譲ってわかるけど、ONU一体だからルーターとっかえるわけにもいかないのはさあ……メッシュwifi使いたけりゃ月額払いな！ってのもどうかと思いますよ。まあこんなとこ見てないと思うけど。

## 作った人

美瀬和夏（はるせちかげ）  
Misskey.io: [@chikage8640@misskey.io](https://misskey.io/@chikage8640)

## ライセンス
[MIT License](/LICENSE)
