"""
wrapped_gridを使ったフォントリスト
"""
import tkinter as tk
import tkinter.font
from tkinter_libs import TkinterLib
from tkinter_libs import ScrolledFrame

class FontLib():
    """
    フォントリスト表示用クラス
    """
    def __init__(self, text:str="sample サンプル ", font_size:int=14, flex=False) -> None:
        """
        コンストラクタ
        Args:
            str:    出力文字
            int:    文字のフォントサイズ
            bool:   幅に入るだけgridするかどうか(True:入るだけ、False:列数固定)
        """
        self.root = tk.Tk()
        self.root.geometry("1124x800")    # サイズ
        self.fonts = tk.font.families()
        self.text = text
        self.FONT_SIZE = font_size
        # scroll付きFrameの作成
        self.frame = ScrolledFrame(self.root, background="lavender", has_h_bar=True)
        self.frame.parent_frame.pack(fill="both", expand=True)
        # bind wrapped_gridへのbind 親の幅に合わせてgridする
        # frame だと発生しない、canvasだと発生、rootだと発生しまくり
        self.labels = []
        self.frame.parent_canvas.bind("<Configure>", lambda event: TkinterLib.wrapped_grid(
            self.frame.parent_canvas, *self.labels, event=event, flex=flex), add=True)

    def font_list_by_label_wrapped_grid(self) -> None:
        """
        familiesを対象、ラベルで実装
        """
        self.labels = []
        for i, font_name in enumerate(self.fonts):
            label = tk.Label(self.frame, text=f"{i+1}:{self.text} {font_name}",
                             font=(font_name, self.FONT_SIZE), relief=tk.RIDGE, wraplength=200)
            self.labels.append(label)
            # 仮にgridする
            label.grid(row=i, column=0, sticky=tk.W)

if __name__ == '__main__':
    """
    familiesを対象、ラベルで実装。wrapped_grid使用
    """
    kwargs = {}
    kwargs["text"] = ""         # 表示テキスト(""でもフォント名は出る)
    kwargs["font_size"] = 11    # フォントサイズ
    kwargs["flex"] = False      # 可変幅にするかどうか

    a = FontLib(**kwargs)
    a.font_list_by_label_wrapped_grid()
    a.root.mainloop()
