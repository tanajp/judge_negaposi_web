# ネガポジ判定

## 概要
テキストボックスに文章を入力し判定ボタンを押すと、その文章がポジティブなのかネガティブなのかをスコアとともに出力する。

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
