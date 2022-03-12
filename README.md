# Python-fontlist
## 概要 Description
フォントリスト  
Font list viewer

Tkinterでサポートしているフォントのリストを表示します。  
Shows a list of fonts supported by Tkinter.  

## 特徴 Features

- フォント名をそのフォントで表示  
	Display font name in that font  
- フレームにスクロールバーを付けてスクロール可能  
	Scrollable with a scroll bar attached to the frame  
- フォント表示をラベルとラジオボタンで実装  
	Implemented font display with labels and radio buttons  
- ScrolledFrameクラスの使用例  
	Example of using ScrolledFrame class  
- Windows\fontsフォルダからフォントリスを作成(フォントファイル名の表示)
	Create a font list from the Windows \ fonts folder (display font file names)  

## 依存関係 Requirement

- Python 3.8.5  

## 使い方 Usage

```python
if __name__ == '__main__':
    """
    1:familiesを対象、ラベルで実装。
    2:familiesを対象、ラジオボタンで実装。ScrolledFrameを使用
    3:pillowのtruetypeで実装。fontsフォルダを対象。
    """
    switch = 1
```

ソースコード内の「switch」変数を1-3に切り替えて実行  
Switch the "switch" variable in the source code to 1-3 and execute  


- 画面の説明 Screen description  
	- switch=1:フォントをラベルで表示。縦横のスクロールバーが出る  
		switch = 1: Display fonts as labels. Vertical and horizontal scroll bars appear    
	- switch=2:フォントをラジオボタンで表示。縦横のスクロールバーが出る。ScrolledFrameクラスを使用    
		switch = 2: Display fonts with radio buttons. Vertical and horizontal scroll bars appear. Use ScrolledFrame class     
	- switch=3:フォントとフォントファイル名を表示。  
		switch = 3: Display font and font file name.    

## プログラムの説明サイト Program description site

[スクロールバー付Frameで作るフォント一覧の作り方【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/tkinter/scrolled-frame)  

## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSE.txtを確認してください。  
This software is released under the MIT License, see LICENSE.txt.

