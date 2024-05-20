from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("TODO LIST")
root.geometry("500x500")
root.resizable(True,True)
root.configure(background="#223441")

def viewstatus():
    done=0
    undone=0
    total=list.size()
    for i in range(total):
        if(list.itemcget(i, "fg") == "green"):
            done=done+1
        else:
            undone=undone+1
    messagebox.showinfo("Tasks",f"Total Tasks: {total} \n Completed Tasks: {done} \n Incompleted Tasks: {undone}")

def add():
    input=entry.get()
    if(input!=" "):
        list.insert(END,input)
        list.itemconfig(END, fg="red")
        entry.delete(0,END)

def done():
    index=list.curselection()
    if(index):
        list.itemconfig(index, fg="green")

def delete():
    index=list.curselection()
    if(index):
        list.delete(index)

head=Label(root,text="To-Do List",font=("Forte",25),bg="#223441",fg="white")
head.pack(pady=20)

entry=Entry(root,fg="black",font=("Arial",15,"bold"))
entry.pack(pady=10)

addbtn=Button(root,text="ADD TASK",height="1",width="10",font=("Arial",12,"bold"),command=add)
addbtn.pack(pady=5)

list=Listbox(root,font=("Arial",14,"bold"),selectmode=SINGLE,width=40,height=14)
list.pack(pady=10)

donebtn=Button(root,text="DONE",height="1",width="8",font=("Arial",12,"bold"),command=done)
donebtn.place(x=570,y=535)

statusbtn=Button(root,text="VIEW STATUS",height="1",width="14",font=("Arial",12,"bold"),command=viewstatus)
statusbtn.place(x=685,y=535)

deletebtn=Button(root,text="DELETE",height="1",width="10",font=("Arial",12,"bold"),command=delete)
deletebtn.place(x=858,y=535)

root.mainloop()