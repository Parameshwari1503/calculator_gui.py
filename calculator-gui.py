import tkinter as tk

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result= eval(screen.get())  
            screen.set("result")
        except:
            screen.set("Error")

    elif text == "c":
        screen.set("")
    else:
        screen.set(screen.get() + text)
root = tk.Tk()
root.title("calculator")
root.geometry("300x400")
root.configure(bg="#2c3e50")

screen = tk.StringVar()
screen.set("")
entry = tk.Entry(root, textvar=screen,font="Arial 24", bd=10,
relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8 ,pady=15, padx=10)

Button = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
]
for row in Button:
       frame = tk.Frame(root,bg="#2c3e50")
       frame.pack(expand=True,fill="both")

       for btn in row:
            b = tk.Button(frame, text=btn, font="Arial 16", fg="white",
               bg="#34495e",
activebackground="#16a085", width=5, height=2)
            b.pack(side="left")
            b.bind("<Button-1>", click)
                   
clear = tk.Button(root, text="c",font="Arial 16", fg="white", bg="#e74c3c",
                  activebackground="#c0392b", height=2)
clear.pack(fill="both", padx=10, pady=10)
clear.bind("<Button-1>", click)

root.mainloop()
