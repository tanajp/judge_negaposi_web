# ネガポジ判定

## 概要
テキストボックスに文章を入力し判定ボタンを押すと、その文章がポジティブなのか   
ネガティブなのかをスコアとともに出力する。

<br>

## 開発環境
Python 3.7.4

<br>

## 使用サービス
[単語感情極性対応表](http://www.lr.pi.titech.ac.jp/~takamura/pubs/pn_ja.dic)

<br>

## ディレクトリ構成
・   
┣ app.py  
┣ polarity.txt   
┣ static   
┃    ┗ style.css   
┗ templates     
　　　┣ jinja2.html     
　　　┣ app.html    
　　　┗ negaposi.html      
   
## 必要なファイル
| ファイル名 | 役割 |
----|---- 
| style.css | HTML文書の体裁を整える。 |
| jinja2.html | テンプレートエンジン |
| app.html | テキスト入力画面 |
| negaposi.html | 判定結果表示画面 |
| app.py | ソースコード |
| polarity.txt | 単語感情極性対応表 |


## 動作イメージ
![スクリーンショット 2020-01-08 18 55 46](https://user-images.githubusercontent.com/50686226/71968565-88a88100-3248-11ea-877d-a2bbf8885d4e.png) ![スクリーンショット 2020-01-08 18 55 55](https://user-images.githubusercontent.com/50686226/71968591-978f3380-3248-11ea-9b4e-669f91f07c11.png)
