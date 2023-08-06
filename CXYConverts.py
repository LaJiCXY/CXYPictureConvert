from PIL import Image as IMG
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from os import system

base_color="#FFFAE0"

ui=Tk()
st=StringVar()
v=IntVar()
cm=IntVar()
st.set("!请先设置再开始转换!")

def convertIMG(g,mode):
	md2='RGB'
	gs=[".png",".jpg",".bmp",".webp",".ico",".tga",".pcx",".tif"]
	if g==7:
		md2='CMYK'
	if mode==0:
		w=askopenfilename(title="选择源文件",filetypes=[("支持的格式", ".png .jpg .bmp .jpeg .webp .ico .tga .tif .pcx"),("所有格式","*")])
		with IMG.open(w) as im:
			im.convert(md2).save(w+gs[g])
			print("图片已保存为:"+w+gs[g])
		showinfo("提示","图片已转换完成")
		st.set("转换完成")
	if mode==1:
		w=askopenfilenames(title="选择文件夹",filetypes=[("支持的格式", ".png .jpg .bmp .jpeg .webp .ico .tga .tif .pcx"),("所有格式","*")])
		x=0
		for i in w:
			st.set("转换进度:"+str(x)+"|"+str(len(w)))
			with IMG.open(i) as im:
				im.convert(md2).save(i+gs[g])
				print("图片已保存为:"+i+gs[g])
			x+=1
		q=askquestion("选择","图片已转换完成!\n是否要删除转换前的文件?")
		if q=='yes':
			for i in w:
				system("del /F \""+i.replace("/","\\")+"\"")
			showinfo("提示","删除完成")
		st.set("转换完成")

ui.geometry("300x150+500+500")
ui.title("CXY Converts")
ui.resizable(False,False)
ui.iconbitmap("./conv.ico")
Label(ui,text="点击下方按钮开始转换",bg=base_color).pack()
Button(text="开始使用",font=("STKAITI.TTF",24),command=lambda: convertIMG(cm.get(),v.get()),width=10,bg="#FFFFFF").pack()
l=Label(ui,textvariable=st,bg=base_color).pack()
opt=Menu(ui,tearoff=False)
lg=Menu(opt,tearoff=False)
md=Menu(opt,tearoff=False)
lg.add_radiobutton(label="单次",variable=v,value=0)
lg.add_radiobutton(label="批量",variable=v,value=1)
md.add_radiobutton(label="可移植图像(PNG)	[RGB]",variable=cm,value=0)
md.add_radiobutton(label="JPEG(JPG)		[RGB]",variable=cm,value=1)
md.add_radiobutton(label="位图图像(BMP)		[RGB]",variable=cm,value=2)
md.add_radiobutton(label="网页图像(WEBP)	[RGB]",variable=cm,value=3)
md.add_radiobutton(label="图标(ICO)		[RGB]",variable=cm,value=4)
md.add_radiobutton(label="光追图像(TGA)		[RGB]",variable=cm,value=5)
md.add_radiobutton(label="电脑交换图像(PCX)	[RGB]",variable=cm,value=6)
md.add_radiobutton(label="标签图像(TIF)		[CMYK]",variable=cm,value=7)
opt.add_cascade(label="转换模式",menu=lg)
opt.add_cascade(label="输出格式",menu=md)
ui.config(bg=base_color,menu=opt)
ui.mainloop()
