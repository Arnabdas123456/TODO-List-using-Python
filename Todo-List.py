from tkinter import *

root = Tk()
root.resizable(False,False)

def add():
    content = text.get(1.0, END)
    main_text.insert(END, content)
    with open('data.txt', 'a')as file:
        file.write(content)
        file.seek(0)
        file.close
    text.delete(1.0, END)


def delete():
    remove = main_text.curselection()
    look = main_text.get(remove)
    with open('data.txt', 'r+')as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            item = str(look)
            if item not in line:
                f.write(line)
        f.truncate()
    main_text.delete(remove)

    with open('data.txt', 'r')as file:
        read = file.readlines()
    for i in read:
        ready = i.split()
        main_text.insert(END, ready)
    file.close()


root.geometry("644x400")
root.title("Todo App")
nav = Label(root, text="To-Do-List App", font="ariel 18 bold",
            width=10, bd=5, bg="orange", fg="black")
nav.pack(side='top', fill=BOTH)

body1 = Label(root, text="Task Section", font="ariel 12 bold",
              width=10, bd=5, bg="orange", fg="black")
body1.place(x=40, y=54)

body2 = Label(root, text="Task Lists", font="ariel 12 bold",
              width=10, bd=5, bg="orange", fg="black")
body2.place(x=385, y=54)

main_text = Listbox(root, height=9, bd=2, width=23,
                    font='ariel 20 italic bold')
main_text.place(x=280, y=100)

text = Text(root, bd=2, height=2, width=30, font='ariel 10 bold')
text.place(x=20, y=120)

addButton = Button(root, text="Add Task", font="ariel 15 bold", width=10,
                   bd=5, bg="orange", fg="black", cursor='hand2',activebackground="orange",activeforeground="white", command=add)
addButton.place(x=30, y=200)


delButton = Button(root, text="Delete Task", font="ariel 15 bold", width=10,
                   bd=5, bg="orange", fg="black", cursor='hand2', activebackground="orange", activeforeground="white", command=delete)
delButton.place(x=30, y=280)

root.mainloop()
