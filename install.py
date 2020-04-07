import os
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
    
def display(a, b="Error!", c='200x100', d=(60, 60),e=(25,15)):
    """GUI Message Box"""
    def dest(r):
        r.destroy()
        return

    root = tk.Tk()
    root.geometry(c)
    root.title(b)
    root.config(background=back_color)
    msg = tk.Label(root,
                   text=a,
                   font=("Courier", 10),
                   bg=back_color,
                   highlightthickness=0)
    butt = tk.Button(root,
                     text="OK",
                     width=7,
                     command=lambda: dest(root),
                     highlightthickness=0,
                     bg=fore_color)
    msg.place(x=e[0], y=e[1])
    butt.place(x=d[0], y=d[1])
    root.protocol("WM_DELETE_WINDOW", lambda: exit())
    root.mainloop()
    return

    
def ask(a, b="Error!", c='200x100', d=(60, 60)):
    """GUI Message Box"""
    
    def dest(r):
        r.destroy()
        exit()
        return
    
    
    def start(r):
        r.destroy()
        os.system('sudo python3 pi_radio.py')
        exit()
    
    root = tk.Tk()
    root.geometry('200x100')
    root.title(b)
    root.config(background=back_color)
    msg = tk.Label(root,
                   text='Do You Want\nto start Pi Radio?',
                   font=("Courier", 10),
                   bg=back_color,
                   highlightthickness=0)
    butt1 = tk.Button(root,
                     text="No",
                     width=7,
                     command=lambda: dest(root),
                     highlightthickness=0,
                     bg=fore_color)
    butt1 = tk.Button(root,
                     text="Yes",
                     width=7,
                     command=lambda: start(root),
                     highlightthickness=0,
                     bg=fore_color)
    msg.place(x=25, y=15)
    butt.place(x=d[0], y=d[1])
    root.protocol("WM_DELETE_WINDOW", lambda: exit())
    root.mainloop()
    return

def install(a):
    try:
        os.system("wget http://omattos.com/pifm.tar.gz")
        os.system("tar -xvf pifm.tar.gz")
        os.system("rm pifm.tar.gz")
        os.system("apt-get install ffmpeg")
    except Exception:
        display("Installation\nFailed")
    display("Installation\nFinished","Pi Radio")
    a.restroy()
    ask()
    
back_color = '#CAE1F4'
fore_color = '#7ABDE4'

if 'pi_radio.py' not in os.listdir():
    display('Pi Radio file\n(pi_radio.py) is missing',e=(00,10))
    exit()
    
root = tk.Tk()
root.geometry('200x100')
root.title('Pi Radio')
root.protocol("WM_DELETE_WINDOW", lambda: exit())
root.config(background=back_color)
disp = tk.Label(root,
                text="Install Pi Radio\ndependencies?",
                font=("Courier", 10),
                bg=back_color,
                highlightthickness=0,
                )
ok_butt = tk.Button(root,
                    text='Ok',
                    width=7,
                    command=lambda: install(root),
                    highlightthickness=0,
                    bg=fore_color,
                    )
disp.place(x=35,y=10)
ok_butt.place(x=55,y=60)
root.mainloop()