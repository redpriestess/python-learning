# import tkinter as tk
# root = tk.Tk()
# root.title("Grid Layout")
# root.geometry("400x400")

# full_width=400

# root.update_idletasks()
# print(int(root.winfo_width()*0.1))

# tk.Label(root, text="Username").place(x=int(root.winfo_width()*0.1),y=10)
# tk.Entry(root).place(x=70,y=10)

# tk.Label(root, text="Password").place(x=int(root.winfo_width()*0.1),y=40)
# tk.Entry(root, show="*").place(x=70,y=40)

# tk.Button(root,text='Exit').place(x=380,y=380)

# tk.Button(root, text="Login").place(x=int(root.winfo_width()*0.1),y=380)
# root.mainloop()

'''
Create a simple application with 5 buttons and a label that will display
 'Good morning!' in 5 different langugages. 
The language buttons should be arrange in a circular shape
'''

# import tkinter as tk
# translate=tk.Tk()
# translate.title("Translator")
# translate.geometry("400x600")

# def korean():
#     korealabel.configure(text="좋은 아침이에요")

# def english():
#     englishlabel.configure(text="Good morning")

# def german():
#     germanlabel.configure(text="Guten Morgen")

# def mandarin():
#     mandarinlabel.configure(text="早上好")

# def japanese():
#     japaneselabel.configure(text="おはよう")

# tk.Label(translate,text="Enter good morning and select a language").place(x=100,y=5)

# translate_entry=tk.Entry(translate,text="",font=("Aptos",12))
# translate_entry.place(x=100,y=30)


# koreabutton=tk.Button(translate,text="korean",command=korean)
# koreabutton.place(x=50,y=70)
# korealabel=tk.Label(translate,text="")
# korealabel.place(x=120,y=70)

# englishbutton=tk.Button(translate,text="english",command=english)
# englishbutton.place(x=50,y=110)
# englishlabel=tk.Label(translate,text="")
# englishlabel.place(x=120,y=110)

# germanbutton=tk.Button(translate,text="german",command=german)
# germanbutton.place(x=50,y=150)
# germanlabel=tk.Label(translate,text="")
# germanlabel.place(x=120,y=150)


# mandarinbutton=tk.Button(translate,text="mandarin",command=mandarin)
# mandarinbutton.place(x=50,y=190)
# mandarinlabel=tk.Label(translate,text="")
# mandarinlabel.place(x=120,y=190)


# japanesebutton=tk.Button(translate,text="japanese",command=japanese)
# japanesebutton.place(x=50,y=230)
# japaneselabel=tk.Label(translate,text="")
# japaneselabel.place(x=120,y=230)

# translate.mainloop()


import tkinter as tk
translate=tk.Tk()
translate.title("Translator")
translate.geometry("400x600")

output_label = tk.Label(translate, text="", font=("Aptos", 16))
output_label.place(x=100, y=30)


def korean(event):
    output_label.configure(text="좋은 아침이에요")

def english(event):
    output_label.configure(text="Good morning")

def german(event):
    output_label.configure(text="Guten Morgen")

def mandarin(event):
    output_label.configure(text="早上好")

def japanese(event):
    output_label.configure(text="おはよう")


canvas=tk.Canvas(translate, width=400, height=600) 
canvas.place(x=0,y=80)

def create_circle_button(x1,y1,x2,y2,text,color,function):
    circle=canvas.create_oval(x1,y1,x2,y2,fill=color)
    
    center_x=(x1+x2)/2
    center_y=(y1+y2)/2
    text_id = canvas.create_text(center_x, center_y, text=text)

    canvas.tag_bind(circle,"<Button-1>",function)
    canvas.tag_bind(text_id,"<Button-1>",function)  

create_circle_button(50, 50, 150, 150, "Korean", "lightblue", korean)
create_circle_button(200, 50, 300, 150, "English", "lightgreen", english)
create_circle_button(50, 200, 150, 300, "German", "lightpink", german)
create_circle_button(200, 200, 300, 300, "Mandarin", "lightyellow", mandarin)
create_circle_button(125, 350, 225, 450, "Japanese", "lavender", japanese)

translate.mainloop()