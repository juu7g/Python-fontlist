# Python-fontlist
## �T�v Description
�t�H���g���X�g `en` Font list viewer  

Tkinter�ŃT�|�[�g���Ă���t�H���g�̃��X�g��\�����܂��B  
`en` Shows a list of fonts supported by Tkinter.  

## ���� Features

- fonts_list.py
	- �t�H���g�������̃t�H���g�ŕ\��  
		`en` Display font name in that font  
	- �t���[���ɃX�N���[���o�[��t���ăX�N���[���\  
		`en` Scrollable with a scroll bar attached to the frame  
	- �t�H���g�\�������x���ƃ��W�I�{�^���Ŏ���  
		`en` Implemented font display with labels and radio buttons  
	- ScrolledFrame�N���X�̎g�p��  
		`en` Example of using ScrolledFrame class  
	- Windows\fonts�t�H���_����t�H���g���X���쐬(�t�H���g�t�@�C�����̕\��)
		`en` Create a font list from the Windows \ fonts folder (display font file names)  
- fonts_list_wrapped_grid.py
	- ScrolledFrame �N���X���g�p���ăX�N���[���o�[�̕\���ƃ}�E�X�z�C�[���ł̃X�N���[�����ł��܂�  
		`en` Since it uses the ScrolledFrame class, you can display the scroll bar and scroll with the mouse wheel.
	- �E�B���h�E�̕���ς��Ă��E�B���h�E�̕��Ń��x����܂�Ԃ��܂�  
		`en` Wraps the label at the width of the window even if you change the width of the window

## �ˑ��֌W Requirement

- Python 3.8.5  

## �g���� Usage

- fonts_list.py

	```Python
	if __name__ == '__main__':
    	"""
    	1:families��ΏہA���x���Ŏ����B
    	2:families��ΏہA���W�I�{�^���Ŏ����BScrolledFrame���g�p
    	3:pillow��truetype�Ŏ����Bfonts�t�H���_��ΏہB
    	"""
    	switch = 1
	```

	�\�[�X�R�[�h���́uswitch�v�ϐ���1-3�ɐ؂�ւ��Ď��s  
	`en` Switch the "switch" variable in the source code to 1-3 and execute  

	- ��ʂ̐��� `en` Screen description  
		- switch=1:�t�H���g�����x���ŕ\���B�c���̃X�N���[���o�[���o��  
			`en` switch = 1: Display fonts as labels. Vertical and horizontal scroll bars appear    
		- switch=2:�t�H���g�����W�I�{�^���ŕ\���B�c���̃X�N���[���o�[���o��BScrolledFrame�N���X���g�p    
			`en` switch = 2: Display fonts with radio buttons. Vertical and horizontal scroll bars appear. Use ScrolledFrame class     
		- switch=3:�t�H���g�ƃt�H���g�t�@�C������\���B  
			`en` switch = 3: Display font and font file name.    

- fonts_list_wrapped_grid.py

	```Python
	if __name__ == '__main__':
    	"""
    	families��ΏہA���x���Ŏ����Bwrapped_grid�g�p
    	"""
    	kwargs = {}
    	kwargs["text"] = ""         # �\���e�L�X�g(""�ł��t�H���g���͏o��)
    	kwargs["font_size"] = 11    # �t�H���g�T�C�Y
    	kwargs["flex"] = False      # �ϕ��ɂ��邩�ǂ���
	```

	FontLib �N���X�̃R���X�g���N�^�ɓn���������w��  
	`en` Specify the argument to be passed to the constructor of FontLib class  
	- `text` �F�\���e�L�X�g `en` Display text
	- `font_size` �F�t�H���g�T�C�Y `en` Font size
	- `flex` �F�ϕ��ɂ��邩�ǂ��� `en` Whether to make it variable width

## �v���O�����̐����T�C�g Program description site

- [�X�N���[���o�[�tFrame�ō��t�H���g�ꗗ�̍����yPython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/Python/tkinter/scrolled-frame)  
- [���b�v����grid(wrapped_grid)�ō��t�H���g�ꗗ�̍����yPython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/Python/tkinter/wrapped-grid)

## ��� Authors
juu7g

## ���C�Z���X License
���̃\�t�g�E�F�A�́AMIT���C�Z���X�̂��ƂŌ��J����Ă��܂��BLICENSE.txt���m�F���Ă��������B  
`en` This software is released under the MIT License, see LICENSE.txt.