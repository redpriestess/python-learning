import tkinter as  tk

root=tk.Tk()

image=tk.PhotoImage(file='the_glorious_praveen.png')
image_label=tk.Label(root,image=image)
image_label.pack()

label=tk.Label(root,text='The Glorious Praveen')
label.pack()

root.mainloop()