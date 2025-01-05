# 温度アラートシステム

[![test](https://github.com/reo422/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/reo422/mypkg/actions/workflows/test.yml)

このリポジトリは、体温の測定結果に基づいてアラートを送信するROS2ノードです。

# 概要
・temperaturepublisherノードは、サンプルの体温データを1秒ごとにtemperaturealertsトピックに公開します。

・bodyalertノードは、temperaturealertsトピックから体温データを受信し、体温に基づいてメッセージを表示します。

　36.0度未満:体を温めてください。
　36.0度から37.0度:健康です。
  37.0度以上:病院に行きましょう。

# 使用方法
1. このパッケージをセットアップし、依存関係をインストールします。
2. temperaturepublisherノードを起動し、体温データを公開します。
```bash
   ros2 run mypkg temperaturepublisher
```
3. 別のターミナルで、bodyalertノードを起動し、受信した体温データに基づいてアクションを実行します。
```bash
   ros2 run mypkg bodyalert
```

# 実行例
temperaturepublisherノード、bodyalertノードの実行結果
```bash
[INFO] [1736085876.774851391] [bodyalert]: 35.8度:体を温めてください。
[INFO] [1736085877.762016491] [bodyalert]: 36.5度:健康です。
[INFO] [1736085878.761839937] [bodyalert]: 38.0度:病院に行きましょう。
[INFO] [1736085881.760506401] [bodyalert]: 35.8度:体を温めてください。
[INFO] [1736085882.761341638] [bodyalert]: 37.4度:病院に行きましょう。
[INFO] [1736085884.761043553] [bodyalert]: 36.4度:健康です。
[INFO] [1736085885.760956194] [bodyalert]: 36.3度:健康です。
・・・
```
# 注意事項
・temperaturepublisherノードは、サンプルデータを使用して体温を公開します。データが完了した後は、ランダムな体温値を生成して継続的にアラートを送信します。
# ライセンス
このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。

© 2024 Reo Isaka
