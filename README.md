# Python-fontlist
## 概要 Description
フォントリスト `en` Font list viewer  

Tkinterでサポートしているフォントのリストを表示します。  
`en` Shows a list of fonts supported by Tkinter.  

## 特徴 Features

- fonts_list.py
	- フォント名をそのフォントで表示  
		`en` Display font name in that font  
	- フレームにスクロールバーを付けてスクロール可能  
		`en` Scrollable with a scroll bar attached to the frame  
	- フォント表示をラベルとラジオボタンで実装  
		`en` Implemented font display with labels and radio buttons  
	- ScrolledFrameクラスの使用例  
		`en` Example of using ScrolledFrame class  
	- Windows\fontsフォルダからフォントリスを作成(フォントファイル名の表示)
		`en` Create a font list from the Windows \ fonts folder (display font file names)  
- fonts_list_wrapped_grid.py
	- ScrolledFrame クラスを使用してスクロールバーの表示とマウスホイールでのスクロールができます  
		`en` Since it uses the ScrolledFrame class, you can display the scroll bar and scroll with the mouse wheel.
	- ウィンドウの幅を変えてもウィンドウの幅でラベルを折り返します  
		`en` Wraps the label at the width of the window even if you change the width of the window

## 依存関係 Requirement

- Python 3.8.5  

## 使い方 Usage

- fonts_list.py

	```Python
	if __name__ == '__main__':
    	"""
    	1:familiesを対象、ラベルで実装。
    	2:familiesを対象、ラジオボタンで実装。ScrolledFrameを使用
    	3:pillowのtruetypeで実装。fontsフォルダを対象。
    	"""
    	switch = 1
	```

	ソースコード内の「switch」変数を1-3に切り替えて実行  
	`en` Switch the "switch" variable in the source code to 1-3 and execute  

	- 画面の説明 `en` Screen description  
		- switch=1:フォントをラベルで表示。縦横のスクロールバーが出る  
			`en` switch = 1: Display fonts as labels. Vertical and horizontal scroll bars appear    
		- switch=2:フォントをラジオボタンで表示。縦横のスクロールバーが出る。ScrolledFrameクラスを使用    
			`en` switch = 2: Display fonts with radio buttons. Vertical and horizontal scroll bars appear. Use ScrolledFrame class     
		- switch=3:フォントとフォントファイル名を表示。  
			`en` switch = 3: Display font and font file name.    

- fonts_list_wrapped_grid.py

	```Python
	if __name__ == '__main__':
    	"""
    	familiesを対象、ラベルで実装。wrapped_grid使用
    	"""
    	kwargs = {}
    	kwargs["text"] = ""         # 表示テキスト(""でもフォント名は出る)
    	kwargs["font_size"] = 11    # フォントサイズ
    	kwargs["flex"] = False      # 可変幅にするかどうか
	```

	FontLib クラスのコンストラクタに渡す引数を指定  
	`en` Specify the argument to be passed to the constructor of FontLib class  
	- `text` ：表示テキスト `en` Display text
	- `font_size` ：フォントサイズ `en` Font size
	- `flex` ：可変幅にするかどうか `en` Whether to make it variable width

## プログラムの説明サイト Program description site

- [スクロールバー付Frameで作るフォント一覧の作り方【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/tkinter/scrolled-frame)  
- [ラップするgrid(wrapped_grid)で作るフォント一覧の作り方【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/tkinter/wrapped-grid)

## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSE.txtを確認してください。  
`en` This software is released under the MIT License, see LICENSE.txt.