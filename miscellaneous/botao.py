# test the use of a tkinter module button
# testare l'uso di un pulsante del modulo tkinter


import sys
print(sys.version_info[0])
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

root = tk.Tk()
frm = tk.Frame(root,height=100,width=200)
frm.grid()
tk.Label(frm, text="Hello World!",width=100).grid(column=0, row=0)
tk.Button(frm, text="Quit", command=root.destroy,width=50).grid(column=1, row=1)
root.mainloop()


