'''
Frames are container widgets
purpose: Group widgets together
         Organize the layout of the program
        
without them: all widgets will sit on the root window

root
    - button
    - label1
    - label2
    - entry1
    - entry2
    
root 
    frame 1
        label1
        entry1
    frame 2
        label2
        entry2
    frame 3
        button
'''

# import tkinter as tk 
# root=tk.Tk()

# frame=tk.Frame(root)
# frame.pack()

# label= tk.Label(frame,text='Hello from the frame!')
# label.pack()

# root.mainloop()

''' A MORE CONCRETE EXAMPLE OF FRAME USAGE '''
# import tkinter as tk

# root = tk.Tk()
# root.geometry("400x300")

# top_frame = tk.Frame(root, bg="lightblue", height=50)
# top_frame.pack(fill="x")

# left_frame = tk.Frame(root, bg="lightgray", width=100)
# left_frame.pack(side="left", fill="y")

# main_frame = tk.Frame(root, bg="white")
# main_frame.pack(expand=True, fill="both")

# tk.Label(top_frame, text="Application Title",bg="lightblue").pack()

# tk.Button(left_frame, text="Menu 1").pack(pady=5)
# tk.Button(left_frame, text="Menu 2").pack(pady=5)

# tk.Label(main_frame, text="Main Content Area").pack()

# root.mainloop()

''' USING FRAME TO MAKE PACK AND GRID WORK TOGETHER '''

import tkinter as tk 

root=tk.Tk()

root.geometry('300x400')
# frame=tk.Frame(root)
# frame.pack()

label= tk.Label(root,text='Are you a dog person?')
label.pack()

frame = tk.Frame(root)
frame.pack(pady=20)

yes_button=tk.Button(frame,text='Yes')
yes_button.grid(row=0,column=0,padx=20)

yes_button2=tk.Button(frame,text='Yes2')
yes_button2.grid(row=0,column=1,padx=20)


root.mainloop()