import tkinter as tk
from tkinter import*


root=tk.Tk()
root.geometry("480x290")
#root.configure(bg="purple")
bg = PhotoImage(file = "/home/akash/Pictures/img6.png")
label1 = Label(root, image = bg)
label1.place(x = -120, y = -10)
root.title("welcome in mit chat app")
#Label(root,text="OPTION",width=15,bd=6,bg="violet",font=('calibre',10,'normal')).pack()
#Label(root,text="Application Version 1.0.0",width=25,bd=4,bg="lightgreen",font =('calibre',10,'normal')).pack(side=BOTTOM)

B=StringVar()
H=StringVar()

t1=Entry(root,text=H,width=25,bd=3,bg="cyan2",font = ('calibre',13,'normal'))
t1.place(x=70,y=170,height=40)
t2=Entry(root,text=B,width=25,bd=3,bg="cyan2",font = ('calibre',13,'normal'))
t2.place(x=70,y=70,height=40)

#user_input=H.get()
def BOT():
 from chatterbot import ChatBot
 from chatterbot.trainers import ListTrainer
 con=[
    "Hello",
    "Hi,welcome in MIT!",
    "i am a student.",
    "ok,what do you want?",
    "information about addmission",
    "ok,which course?",
    "B.Tech",
    "ok,which branch?",
    "computer science",
    "call at 1808210012"
    "ok,thank you",
    "you're welcome"
    ]
 
 #trainer = ChatterBotCorpusTrainer(chatbot)
 chatbot = ChatBot("Ron Obvious")
 trainer = ListTrainer(chatbot)
 trainer.train(con)


 # The following loop will execute each time the user enters input
   # a=str(input("1).chat\n2).exit\nchoose option : "))
   # if a=="exit":
   #break
    #else:
 user_input=H.get()
 try:
         #user_input = input("Enter something : ")
         #user_input=H.get()
         bot_response = chatbot.get_response(user_input)
         #print(bot_response)
         Label(root,text=bot_response,width=25,height=1,bd=0.00003,font = ('calibre',13,'normal'),bg="cyan2").place(x=74,y=80)
         #Entry(root,text=bot_response,width=25,bd=3,font = ('calibre',13,'normal')).place(x=100,y=130)
         # Press ctrl-c or ctrl-d on the keyboard to exit
         return bot_response
 except (KeyboardInterrupt, EOFError, SystemExit):
        return "error"
#user_input=H.get()
def WEB():
    import web
Button(root,text="DOWNLOAD CODE",width=14,height=2,bd=3,bg="green",command=WEB).place(x=80,y=230)
Button(root,text="YOU",width=15,height=2,bd=3,bg="violet").place(x=70,y=120)
Button(root,text="BOOT",width=15,height=2,bd=3,bg="violet").place(x=70,y=20)

Button(root,text="send",width=8,height=2,bd=3,bg="green",font = ('calibre',8,'normal'),command=BOT).place(x=360,y=170)
Button(root,text="send",width=8,height=2,bd=3,bg="blue",font = ('calibre',8,'normal'),command=BOT).place(x=360,y=70)


def destroy():
    #conn.close()
    root.destroy()
Button(root,text="EXIT",width=14,height=2,bd=3,bg="red",command=destroy).place(x=220,y=230)
root.resizable(0,0)
root.mainloop()
