"""
フォントリスト表示
"""
import tkinter as tk
from tkinter.constants import HORIZONTAL, VERTICAL
import tkinter.font
import sys

class FontLib():
    """
    フォントリスト表示用クラス
    """
    def __init__(self, text:str="sample サンプル ", font_size:int=14) -> None:
        """
        コンストラクタ
        Args:
            str:    出力文字
            int:    文字のフォントサイズ
        """
        self.root = tk.Tk()
        self.root.geometry("800x600")       # サイズ
        self.fonts = tk.font.families()     # tkが管理しているフォントのリストを取得
        self.text = text                    # 表示文字列の設定
        self.MAX_ROWS = 25                  # 行数のデフォルト
        self.MAX_COLUMN = 4                 # 列数のデフォルト
        self.FONT_SIZE = font_size          # フォントサイズの設定
        # スクロールバー付Frameの作成(Canvasにスクロールバーを付けて)
        self.canvas = tk.Canvas(self.root)  # Canvasをrootに作成
        self.frame = tk.Frame(self.canvas)  # Frame をCanvasに作成
        self.vsb = tk.Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)      # 縦スクロールバーをrootに作成
        self.hsb = tk.Scrollbar(self.root, orient=HORIZONTAL, command=self.canvas.xview)    # 横スクロールバーをrootに作成
        self.canvas.configure(yscrollcommand=self.vsb.set)  # 縦スクロールバーの動作をCanvasに設定
        self.canvas.configure(xscrollcommand=self.hsb.set)  # 横スクロールバーの動作をCanvasに設定
        # pack スクロールバーは先にpackする
        self.hsb.pack(side="bottom", fill="x")
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        # canvasにウィジェットを配置
        self.canvas.create_window((4,4), window=self.frame, anchor="nw")
        # bind
        self.frame.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event=None):
        """
        canvasを親に持つframeでサイズ変更があった場合にcanvasのscrollregionを更新する
        これでスクロールバーが動作する
        frameの<configure>シーケンスとbindして使う
        """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def font_list_by_label(self) -> None:
        """
        1.familiesを対象、ラベルで実装
        """
        for i, font_name in enumerate(self.fonts):
            # ラベルの作成 フォントはfontオプションで直に指定
            label = tk.Label(self.frame, text=f"{self.text} {font_name}",
                             font=(font_name, self.FONT_SIZE))
            # grid
            # 最大行を指定して1列目から配置
            label.grid(row=i % self.MAX_ROWS, column=i // self.MAX_ROWS, sticky="w")
            # 最大列を指定して1行目から配置
            # label.grid(row=i // self.MAX_COLUMN, column=i % self.MAX_COLUMN, sticky="w")

    def font_list_radiobutton(self) -> None:
        """
        2.familiesを対象、ラジオボタンで実装
            ScrolledFrameを使用
        """
        from tkinter_libs import ScrolledFrame
        # ScrolledFrameを使うため既にできているroot以下のウィジェットを削除
        for w in self.root.winfo_children():
            w.destroy()
        # ScrolledFrame
        self.frame = ScrolledFrame(self.root, has_h_bar=True)
        self.var_radio = tk.IntVar(value=0) # self.にしないとマウス移動で全選択になってしまう
        for i, font_name in enumerate(self.fonts):
            # ラジオボタンの作成 フォントは先にFontオブジェクトを作成してfontオプションで指定
            font_ = tkinter.font.Font(self.root, family=font_name, size=self.FONT_SIZE)
            rb = tk.Radiobutton(self.frame, text=f"{self.text} {font_name}", 
                                font=font_, variable=self.var_radio, value=i)
            # grid
            # 最大行を指定して1列目から配置
            rb.grid(row=i % self.MAX_ROWS, column=i // self.MAX_ROWS, sticky="w")
            # 最大列を指定して1行目から配置
            # rb.grid(row=i // self.MAX_COLUMN, column=i % self.MAX_COLUMN, sticky="w")

    def font_list_from_dir(self):
        """
        3.fontsフォルダを対象にpillowのtruetypeで実装
        """
        import glob, os
        from PIL import ImageFont 

        # windowsのフォントフォルダの取得
        windir = os.environ.get("WINDIR")
        files = glob.glob(windir + r"\fonts\*")
        for i, file in enumerate(files):
            basename = os.path.basename(file)
            try:
                img_font = ImageFont.truetype(file, 24)
            except:
                # pillowの対象外のファイルを除く
                # print(f"path:{basename}")
                pass
            else:
                font_name = img_font.getname()[0]
                font_ = tkinter.font.Font(self.root, family=font_name, weight="bold")
                # getnameのfamilyの日本語が文字化けするのでactualに置き換える
                font_name = font_.actual("family")
                # フォント名、フォントファイル名、サンプル文字、フォント名でのサンプルをラベルで出力
                tk.Label(self.frame, text=font_name).grid(row=i, column=1, sticky="w")
                tk.Label(self.frame, text=basename, bg="yellow").grid(row=i, column=2, sticky="w")
                tk.Label(self.frame, text=self.text,
                                font=(font_name, self.FONT_SIZE)).grid(row=i, column=3, sticky="w")
                tk.Label(self.frame, text=font_name,
                                font=(font_name, self.FONT_SIZE)).grid(row=i, column=4, sticky="w")

if __name__ == '__main__':
    """
    1:familiesを対象、ラベルで実装。
    2:familiesを対象、ラジオボタンで実装。
    3:pillowのtruetypeで実装。fontsフォルダを対象。
    """
    switch = 3
    text_ = input("\n表示したい文字を入力してください(何も入力しなければ「sample サンプル」と出ます)\n >")
    font_size = input("フォントサイズを入力してください(何も入力しなければ「14ポイント」で出力します)\n >")

    kwargs = {}
    if text_: kwargs["text"] = text_
    if font_size: kwargs["font_size"] = int(font_size)

    a = FontLib(**kwargs)
    if switch == 1:
        # a.root.state("zoomed")  # 最大化
        a.font_list_by_label()
    elif switch == 2:
        # a.root.state("zoomed")  # 最大化
        a.font_list_radiobutton()
    elif switch == 3:
        a.font_list_from_dir()
    else:
        print("選択間違い")
        sys.exit()
    a.root.mainloop()
