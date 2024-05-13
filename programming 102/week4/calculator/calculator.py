import tkinter as tk

window = tk.Tk()
window_width = 360
window_height = 360
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))
window.title('Calculator')

entry = tk.Entry(window,  font=('Arial', 24), width=15)
entry.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack()

buttons = ['7','8','9','/',
         '4','5','6','+',
         '1','2','3','*',
         'C','0','=','+'
]

def button_pressed(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

def button_clear():
    entry.delete(0, tk.END)

def button_calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as ex :
        entry.delete(0, tk.END)
        entry.insert(0,"Hata : " + str(ex))

for i, button in enumerate(buttons):
    row = i // 4
    col = i % 4
    if button == 'C':
        btn = tk.Button(button_frame, text=button, font=('Arial', 18), width=5, height=2, command=button_clear)
    elif button == '=':
        btn = tk.Button(button_frame, text=button, font=('Arial', 18), width=5, height=2, command=button_calculate)
    else:
        btn = tk.Button(button_frame, text=button, font=('Arial', 18), width=5, height=2,
                        command=lambda b=button: button_pressed(b))
    btn.grid(row=row, column=col)


window.mainloop()