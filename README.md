# Python-fontlist
## �T�v Description
�t�H���g���X�g  
Font list viewer

Tkinter�ŃT�|�[�g���Ă���t�H���g�̃��X�g��\�����܂��B  
Shows a list of fonts supported by Tkinter.  

## ���� Features

- �t�H���g�������̃t�H���g�ŕ\��  
	Display font name in that font  
- �t���[���ɃX�N���[���o�[��t���ăX�N���[���\  
	Scrollable with a scroll bar attached to the frame  
- �t�H���g�\�������x���ƃ��W�I�{�^���Ŏ���  
	Implemented font display with labels and radio buttons  
- ScrolledFrame�N���X�̎g�p��  
	Example of using ScrolledFrame class  
- Windows\fonts�t�H���_����t�H���g���X���쐬(�t�H���g�t�@�C�����̕\��)
	Create a font list from the Windows \ fonts folder (display font file names)  

## �ˑ��֌W Requirement

- Python 3.8.5  

## �g���� Usage

```python
if __name__ == '__main__':
    """
    1:families��ΏہA���x���Ŏ����B
    2:families��ΏہA���W�I�{�^���Ŏ����BScrolledFrame���g�p
    3:pillow��truetype�Ŏ����Bfonts�t�H���_��ΏہB
    """
    switch = 1
```

�\�[�X�R�[�h���́uswitch�v�ϐ���1-3�ɐ؂�ւ��Ď��s  
Switch the "switch" variable in the source code to 1-3 and execute  


- ��ʂ̐��� Screen description  
	- switch=1:�t�H���g�����x���ŕ\���B�c���̃X�N���[���o�[���o��  
		switch = 1: Display fonts as labels. Vertical and horizontal scroll bars appear    
	- switch=2:�t�H���g�����W�I�{�^���ŕ\���B�c���̃X�N���[���o�[���o��BScrolledFrame�N���X���g�p    
		switch = 2: Display fonts with radio buttons. Vertical and horizontal scroll bars appear. Use ScrolledFrame class     
	- switch=3:�t�H���g�ƃt�H���g�t�@�C������\���B  
		switch = 3: Display font and font file name.    

## �v���O�����̐����T�C�g Program description site

[�X�N���[���o�[�tFrame�ō��t�H���g�ꗗ�̍����yPython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/Python/tkinter/scrolled-frame)  

## ��� Authors
juu7g

## ���C�Z���X License
���̃\�t�g�E�F�A�́AMIT���C�Z���X�̂��ƂŌ��J����Ă��܂��BLICENSE.txt���m�F���Ă��������B  
This software is released under the MIT License, see LICENSE.txt.

