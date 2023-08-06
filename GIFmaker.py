from tkinter import filedialog,messagebox
from tkinter import *
from PIL import Image,ImageSequence
from json import loads
class GIFmaker:
	#窗口
	def __init__(self):
		save_r=""
		v=''
		v1=''
		self.se=None
		self.lgs=0
		if self.lgs==1:
			a="english"
		elif self.lgs==0:
			a="chinese"
		with open("./languagepack","r",encoding='utf-8') as lg:
			lan=loads(lg.read())
		self.language=lan[a]
		del lg,a
		self.w=''
		self.fps=12

	def set_fps(self):
		self.frm=Tk()
		base_color="#FFFAE0"
		self.frm.title("FPS")
		self.frm.geometry("200x100+300+300")
		self.frm.config(bg=base_color)
		Label(self.frm,text="FPS:",font=("STKAITI.TTF",15),bg=base_color).place(x=10,y=20)
		fre=Entry(self.frm,font=("STKAITI.TTF",15),bg=base_color,width=10)
		fre.place(x=50,y=20)
		fre.insert(0,str(self.fps))
		def frmok():
			if int(fre.get())<=15 and int(fre.get())>=0:
				self.fps=int(fre.get())
			else:
				messagebox.showerror("Error","FPS Too Large! Max:15")
			self.frm.destroy()
                
		Button(self.frm,text=self.language[5],font=("STKAITI.TTF",10),command=frmok,width=10).place(x=10,y=50)
		
	def gui_w(self):
		self.w=Tk()
		self.v=IntVar()
		self.v1=IntVar()
		self.v1.set(self.lgs)
		base_color="#FFFAE0"
		self.w.title(self.language[0])
		self.w.geometry("500x300+300+300")
		self.w.iconbitmap("Main.ico")
		self.w.resizable(False,False)
		m=Menu(self.w)
		opt=Menu(m,tearoff=False)
		lg=Menu(opt,tearoff=False)
		lg.add_radiobutton(label="中文",variable=self.v1,value=0,command=self.clg)
		lg.add_radiobutton(label="English",variable=self.v1,value=1,command=self.clg)
		m.add_cascade(label=self.language[-2],menu=opt)
		opt.add_cascade(label=self.language[-1],menu=lg)
		opt.add_command(label="FPS",command=self.set_fps)
		self.w.config(bg=base_color,menu=m)
		Label(self.w,text=self.language[1],font=("STKAITI.TTF",20),bg=base_color).place(x=10,y=20)
		self.se=Entry(self.w,font=("STKAITI.TTF",20),bg=base_color,width=20)
		self.se.place(x=130,y=20)
		Button(text=self.language[2],font=("STKAITI.TTF",12),command=self.save_road,width=6).place(x=430,y=20)
		Radiobutton(text=self.language[3],font=("STKAITI.TTF",20),variable=self.v,value=0,bg=base_color,activebackground=base_color).place(x=60,y=100)
		Radiobutton(text=self.language[4],font=("STKAITI.TTF",20),variable=self.v,value=1,bg=base_color,activebackground=base_color).place(x=310,y=100)
		Button(text=self.language[5],font=("STKAITI.TTF",20),width=10,command=self.sucess).place(x=50,y=200)
		Button(text=self.language[6],font=("STKAITI.TTF",20),command=lambda: self.se.delete(0,END),width=10).place(x=300,y=200)
		self.w.mainloop()
                
	#功能
	def make_gif(self):
		path = filedialog.askopenfilenames(title=self.language[7],
										filetypes=[(self.language[8], ".png .jpg .bmp .jpeg .gif"),(self.language[9],"*")],
										 initialdir="Desktop")

		imgl=[]
		for i in path:
			img = Image.open(i)
			imgl.append(img)

		imgl[0].save(self.save_r,save_all=True,append_images=imgl[1:],duration=1/self.fps*1000)

	def replay_gif(self):
		path = filedialog.askopenfilename(title=self.language[7],
										 filetypes=[(self.language[8], ".gif")],
										 initialdir="Desktop")

		img=Image.open(path)
		nmp=0

		for i in ImageSequence.Iterator(img):
			i.save("./Img.TMP\\"+str(nmp)+".tmp.png")
			nmp+=1
			
		imgl=[]
		for i in range(nmp):
			img = Image.open("./Img.TMP\\"+str(i)+".tmp.png")
			imgl.insert(0,img)

		imgl[0].save(self.save_r,save_all=True,append_images=imgl[1:],duration=1/self.fps*1000)
		
	def save_road(self):
		self.se.delete(0,END)
		self.se.insert(0,filedialog.asksaveasfilename(title='选择文件保存路径与文件名'))
		
	def sucess(self):
		self.save_r=self.se.get()
		try:
			if self.v.get()==0:
				self.make_gif()
			elif self.v.get()==1:
				self.replay_gif()
		except Exception as er:
			messagebox.showerror(self.language[10],self.language[11]+str(er))
		else:
			messagebox.showinfo(self.language[12],self.language[13])
			
	def clg(self):
		if self.v1.get()==0:
			self.lgs=0
		elif self.v1.get()==1:
			self.lgs=1
		self.w.destroy()
		if self.lgs==1:
			a="english"
		elif self.lgs==0:
			a="chinese"
		with open("./languagepack","r",encoding='utf-8') as lg:
			lan=loads(lg.read())
		self.language=lan[a]
		self.gui_w()
wd=GIFmaker()
wd.gui_w()



