from tkinter import*
from tkinter import ttk
from googletrans import Translator,LANGUAGES
def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    t=Translator()
    t1=t.translate(text,src=src1,dest=dest1)
    return t1.text
def data():
    s=comb_s.get()
    d=comb_d.get()
    masg = s_txt.get(1.0,END)
    textget =change(text=masg , src=s , dest=d )
    d_txt.delete(1.0,END)
    d_txt.insert(END,textget)



root =Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="blue")

l_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="blue")
l_txt.place(x=100,y=40,height=50,width=300)

Frame = Frame(root).pack(side=BOTTOM) 
 
l_txt=Label(root,text="You",font=("Time New Roman",20,"bold"),bg="blue")
l_txt.place(x=100,y=100,height=20,width=300)

s_txt=Text(Frame,font=("Time New Roman",15,),wrap=WORD)
s_txt.place(x=10,y=130,height=150,width=480)

mylist=list(LANGUAGES.values())
comb_s=ttk.Combobox(Frame,value=mylist)
comb_s.place(x=10,y=300,height=40,width=150)
comb_s.set("english")

button_change=Button(Frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_d=ttk.Combobox(Frame,value=mylist)
comb_d.place(x=330,y=300,height=40,width=150)
comb_d.set("english")

d_txt=Text(Frame,font=("Time New Roman",15,"bold"))
d_txt.place(x=10,y=360,height=150,width=480)


root.mainloop()