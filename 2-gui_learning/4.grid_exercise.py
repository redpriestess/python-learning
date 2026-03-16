'''
Create a simple calculator app usign the grid layout manager

1234
5678
90-+
*/=.


'''
# import tkinter as tk

# app=tk.Tk()
# app.title("Calculator")
# # app.geometry("600x1000")

# def press(values):
#     entry1.insert(tk.END,values)

# def calculate():
#     try:
#         results=eval(entry1.get())
#         entry1.delete(0,tk.END)
#         entry1.insert(tk.END,results)
#     except:
#         entry1.delete(0,tk.END)
#         entry1.insert(tk.END,"ERROR")
# def bye():
#     entry1.delete(0,tk.END)


# tk.Label(app,text="Simple Calculator").grid(row=0,column=1,columnspan=4)
# entry1=tk.Entry(app,text="",font=("Aptos",15))
# entry1.grid(row=1,column=0,columnspan=4,sticky="we")

# tk.Button(app, text="1",command=lambda:press("1")).grid(row=2, column=0,padx=10,pady=10)
# tk.Button(app, text="2",command=lambda:press("2")).grid(row=2, column=1,padx=10,pady=10)
# tk.Button(app, text="3",command=lambda:press("3")).grid(row=2, column=2,padx=10,pady=10)
# tk.Button(app, text="4",command=lambda:press("4")).grid(row=2, column=3,padx=10,pady=10)

# tk.Button(app, text="5",command=lambda:press("5")).grid(row=3, column=0,padx=10,pady=10)
# tk.Button(app,text="6",command=lambda:press("6")).grid(row=3,column=1,padx=10,pady=10)
# tk.Button(app,text="7",command=lambda:press("7")).grid(row=3,column=2,padx=10,pady=10)
# tk.Button(app,text="8",command=lambda:press("8")).grid(row=3,column=3,padx=10,pady=10)

# tk.Button(app,text="9",command=lambda:press("9")).grid(row=4,column=0,padx=10,pady=10)
# tk.Button(app,text="0",command=lambda:press("0")).grid(row=4,column=1,padx=10,pady=10)
# tk.Button(app,text="-",command=lambda:press("-")).grid(row=4,column=2,padx=10,pady=10)
# tk.Button(app,text="+",command=lambda:press("+")).grid(row=4,column=3,padx=10,pady=10)

# tk.Button(app,text="*",command=lambda:press("*")).grid(row=5,column=0,padx=10,pady=10)
# tk.Button(app,text="/",command=lambda:press("/")).grid(row=5, column=1,padx=10,pady=10)
# tk.Button(app,text="=",command=calculate).grid(row=5,column=2,padx=10,pady=10)
# tk.Button(app,text=".",command=lambda:press(".")).grid(row=5,column=3,padx=10,pady=10)

# clear=tk.Button(app,text="clear",font=("Aptos",15),command=bye)
# clear.grid(row=6,column=1)

# app.mainloop()

#--------------------

DG= "#41431B"
LG="#AEB784"
LLG="#E3DBBB"
W="#F8F3E1"



import tkinter as tk

app=tk.Tk()
app.title("Calculator")

# app.geometry("600x1000")

BG_COLOR = "#1e1e2f"
DISPLAY_COLOR = "#2b2b3c"
NUMBER_COLOR = "#3a3a4f"
OPERATOR_COLOR = "#4a6fa5"
EQUAL_COLOR = "#3fa34d"
CLEAR_COLOR = "#c14953"
TEXT_COLOR = "white"

app.configure(bg=LLG)

def press(value):
    print(value)
    if value=='=':
        try:
            results=eval(entry1.get())
            entry1.delete(0,tk.END)
            entry1.insert(tk.END,results)
        except:
            entry1.delete(0,tk.END)
            entry1.insert(tk.END,"ERROR")
    else:
        entry1.insert(tk.END,value)

def bye():
    entry1.delete(0,tk.END)


tk.Label(app,
         text="Simple Calculator",
         bg=LLG,
         fg=DG,
         font=("Aptos",18)).grid(row=0,column=1,columnspan=4)

entry1=tk.Entry(app,text="",
                bg=DG,
                fg=LLG,
                insertbackground=W,
                font=("Aptos",18))
entry1.grid(row=1,column=0,columnspan=4,sticky="we")

buttons= [['1','2','3','4'],
          ['5','6','7','8'],
          ['9','0','-','+'],
          ['*','/','=','.']]

row_start=2
column_start=0

for i,button_row in enumerate(buttons):
    print(f'button row: {button_row}')
    for j,button in enumerate(button_row):
        
        if button in "+-/*":
            bg_color=LG
        elif button == "=":
            bg_color=LG
        else:
            bg_color=LG
            
        print(f'button col: {button}')
        tk.Button(app,
                  text=button,
                  bg=bg_color,
                  fg=TEXT_COLOR,
                  activebackground='green',
                  activeforeground='red',
                  relief="flat",
                  command=lambda b=button:press(b)
                  ).grid(row=row_start+i,
                         column=column_start+j,
                         padx=10,
                         pady=10,
                         sticky="nsew")
clear=tk.Button(app,text="clear",
                font=("Aptos",15),
                bg=CLEAR_COLOR,
                fg=TEXT_COLOR,
                activebackground=CLEAR_COLOR,
                activeforeground=TEXT_COLOR,
                command=bye)
clear.grid(row=6,
           column=1,
           )


clear=tk.Button(app,text="clear",font=("Aptos",15),command=bye)
clear.grid(row=6,column=1)

app.mainloop()


