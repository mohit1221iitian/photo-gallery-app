from tkinter import *
from PIL import Image,ImageTk
import os

def func():
	global counter
	img_label.config(image=img_array[counter%len(img_array)])
	counter+=1;




counter=1
root=Tk()
root.minsize(500,700)
root.maxsize(500,700)
root.title('IMAGE APPLICATION')
root.configure(background='light blue')
text_label=Label(root,text='IMAGE VIEWER',fg='black',bg='light blue')
text_label.configure(font=('algerian',40))
text_label.pack(pady=(10,10))
root.iconbitmap('icon address')

files=os.listdir('images folder address')
img_array=[]
for file in files:
	img=Image.open(os.path.join('images folder address',file))
	resized_img=img.resize((400,450))
	img_array.append(ImageTk.PhotoImage(resized_img))

img_label=Label(root,image=img_array[0])
img_label.pack(pady=(30,40))

next_btn=Button(root,text='Next',font=('Arial', 20, 'bold','italic'),bg='white',fg='black',width=15,height=100,command=func)
next_btn.pack(pady=(10,35))

root.mainloop()
