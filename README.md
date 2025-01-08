# 温度アラートシステム

[![test](https://github.com/reo422/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/reo422/mypkg/actions/workflows/test.yml)

このROS2パッケージは、体温の測定結果に基づいてアラートを送信する機能を提供します。

# 概要
temperaturepublisherノードは、サンプルの体温データを1秒ごとにtemperaturealertsトピックに公開します。

bodyalertノードは、temperaturealertsトピックから体温データを受信し、体温に基づいてメッセージを表示します。

# 体温に基づくアラートメッセージ
35.8度:体を温めてください。<br>36.5度:健康です。<br>38.0度:病院に行きましょう。

# 使用方法
1. このパッケージをセットアップします。
2. temperaturepublisherノードを起動し、体温データを公開します。
```bash
   ros2 run mypkg temperaturepublisher
```
3. 別のターミナルで、bodyalertノードを起動し、受信した体温データに基づいてアクションを実行します。
```bash
   ros2 run mypkg bodyalert
```
4. また別のターミナルで、以下のコマンドを実行するとメッセージが表示されます。
```bash
   ros2 topic echo /bodyalertmessage
```

# 実行例
以下は、temperaturepublisherノードとbodyalertノードの実行結果の一例です。
```bash
data: 35.8度:体を温めてください。
---
data: 36.5度:健康です。
---
data: 38.0度:病院に行きましょう。
---
data: 35.8度:体を温めてください。
---
data: 37.4度:病院に行きましょう。
---
・・・
```
# 注意事項
temperaturepublisherノードは、サンプルデータを使用して体温を公開します。データが完了した後は、ランダムな体温値を生成して継続的にアラートを送信します。

# テスト環境
Ubuntu 20.04
<br>ryuichiueda/ubuntu22.04-ros2:latest

# ライセンス
このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。

© 2024 Reo Isaka
