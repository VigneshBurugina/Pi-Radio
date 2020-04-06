#!/usr/bin/python

import os
import webbrowser
try:
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    from Tkinter import filedialog




def display(a, b="Error!", c='200x100', d=(60, 60)):
    """ Message Box Utility"""
    def dest(r):
        r.destroy()
        return

    root = tk.Tk()
    root.geometry(c)
    root.title(b)
    root.config(background=back_color)
    msg = tk.Label(root, text=a, font=("Courier", 10), bg=back_color, highlightthickness=0)
    butt = tk.Button(root, text="OK", width=7, command=lambda: dest(root), highlightthickness=0, bg=fore_color)
    msg.place(x=25, y=15)
    butt.place(x=d[0], y=d[1])
    root.protocol("WM_DELETE_WINDOW", lambda: exit())
    root.mainloop()
    return


def play(file_path, freq):
    """Air the given audio file"""
    if file_path == "":
        display("No File Selected")
    if freq == "":
        display("No Frequency Selected")
    try:
        _test = float(freq)
        del _test
    except ValueError:
        display("Incorrect Frequency\nInput")
        exit()
    if (float(low_freq) > float(freq)) or (float(freq) > float(high_freq)):
        display('Frequency out of\nrange')
        exit()
    try:
        if file_path.split('/')[-1][-1:-4:-1] == '3pm':
            os.system(f"ffmpeg -i '{file_path}' -f s16le -ar 22.05k -ac 1 - | sudo ./pifm - {freq}")
        elif file_path.split('/')[-1][-1:-4:-1] == 'vaw':
            os.system(f"sudo ./pifm '{file_path}' {freq} 22050 stereo")
        else:
            display("Invalid File Type")
            exit()
    except Exception:
        display("Somthing's Wrong...Exiting")
        exit()
    except IOError:
        display("Error in File...Exiting")
        exit()
    

def file_dialog(b):
    """File Dialog"""
    a = def_dir
    sel_file_label = tk.Label(b, text="", bg=back_color, highlightthickness=0)
    def cls(a):
        a.destroy()
        return
    
    global file_path
    x = filedialog.askopenfilename(initialdir=a, title="", filetypes=(
        ('MP3 Audio File','.mp3'),('WAV Audio File','*.wav')))
    sel_file_label.destroy() #Check
    file_path = x###
    try:
        sel_file_label = tk.Label(b, text="", bg=back_color, highlightthickness=0)###
        sel_file_label.config(text=file_path.split('/')[-1],)####
    except AttributeError:
        display('Select a File')
        exit()
    sel_file_label.place(x=20,y=40)
    b.update()


def view_info():
    webbrowser.open('https://www.radioreference.com/apps/db/', 2)
    return
    

def settings(_fst=0):
    
    def destroy(a):
        nonlocal _fst
        if _fst == 1:
            exit()
        else:
            a.destroy()
           

    def apply(a,b,d,c):
        nonlocal _fst
        if a <= b:
            c.destroy()
            display("Invalid Range")
            exit()
        if a == "":
            a = "100.0"
        if b == "":
            b = "0.0"
        if _fst == 1:
            with open('settings.conf','w') as fl:
                fl.write('DEFAULT_FREQUENCY=99.9\n')
                fl.write(f'HIGH_FREQUENCY={a}\n')
                fl.write(f'LOW_FREQUENCY={b}\n')
        elif _fst == 0:
            with open('settings.conf','a+') as fl:
                fl.seek(0)
                print(fl.readline())
                fl.write(f'HIGH_FREQUENCY={a}\n')
                fl.write(f'LOW_FREQUENCY={b}\n')
        c.destroy()
        return
    

    if _fst == 1:
        high_freq = 'Not Set'
        low_freq = 'Not Set'
        
    root = tk.Tk()
    root.title('Settings')
    root.geometry('280x120')
    root.protocol("WM_DELETE_WINDOW", lambda: destroy(root))
    root.config(background=back_color)
    high_label = tk.Label(root,text="High Frequency-", font=("Courier", 10), bg=back_color, highlightthickness=0)
    low_label = tk.Label(root,text="Low Frequency-", font=("Courier", 10), bg=back_color, highlightthickness=0)
    high_entry = tk.Entry(root,highlightthickness=0, width=10)
    low_entry = tk.Entry(root,highlightthickness=0, width=10)
    butt = tk.Button(root, text="Apply", width=7, command=lambda: apply(high_entry.get(),low_entry.get(),def_entry.get(),root), highlightthickness=0, bg=fore_color)
    def_label = tk.Label(root,text="Default Directory-", font=("Courier", 10), bg=back_color, highlightthickness=0)
    def_entry = tk.Entry(root,highlightthickness=0, width=10)
    high_label.place(x=10,y=20)
    low_label.place(x=10,y=40)
    high_entry.place(x=170,y=20)
    low_entry.place(x=170,y=40)
    def_label.place(x=10,y=60)
    def_entry.place(x=170,y=60)
    butt.place(x=95,y=90)
    root.mainloop()
    
def about():
    root = tk.Tk()
    root.title("About Pi Radio")
    root.geometry('150x130')
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
    root.config(background=back_color)
    title = tk.Label(root, text='Pi Radio', font=("Courier", 10), bg=back_color, highlightthickness=0)
    desc = tk.Label(root, text='Version: 1.0\nGUI for PiFM\nMade by Vignesh', font=("Courier", 10), bg=back_color, highlightthickness=0)
    but = tk.Button(root, text="Contact", command=lambda: webbrowser.open('####',2), highlightthickness=0, bg=fore_color)
    title.place(x=45, y=10)
    desc.place(x=20,y=30)
    but.place(x=40,y=90)
    root.mainloop()
    
    
def main_menu():
    root = tk.Tk()
    root.title('Pi Radio')
    root.geometry('230x130')
    root.config(background=back_color)
    root.protocol("WM_DELETE_WINDOW", lambda: exit())
    menubar = tk.Menu(root)
    menu1 = tk.Menu(menubar, tearoff=0)
    menu1.add_command(label="Frequency Reference", command=lambda: view_info())
    menu1.add_command(label="Exit", command=lambda: exit())
    menu2 = tk.Menu(menubar, tearoff=0)
    menu2.add_command(label="Settings", command=lambda: settings())
    menu2.add_command(label="About", command=lambda: about())
    menubar.add_cascade(label="Menu", menu=menu1)
    menubar.add_cascade(label="Settings", menu=menu2)
    root.config(menu=menubar)
    #file = file_dialog(initial_dir)
    file_label = tk.Label(root, text='File:', font=("Courier", 10), bg=back_color, highlightthickness=0)
    freq_label = tk.Label(root, text='Frequency:', font=("Courier", 10), bg=back_color, highlightthickness=0)
    file_button = tk.Button(root, text='Select',width=7, command=lambda: file_dialog(root), highlightthickness=0, bg=fore_color)
    freq_entry = tk.Entry(root,highlightthickness=0, width=10)
    play_button = tk.Button(root, text='Play!',width=7,command=lambda: play(file_path,freq_entry.get()), highlightthickness=0, bg=fore_color)
    file_label.place(x=20,y=10)
    freq_label.place(x=20,y=70)
    file_button.place(x=120,y=10)
    freq_entry.place(x=120,y=70)
    play_button.place(x=75,y=100)
    root.mainloop()
    
    
back_color = '#CAE1F4'
fore_color = '#7ABDE4'
file_path = ""
 

if 'settings.conf' not in os.listdir():
    display('First Time?\nSet Settings','Pi Radio')
    settings(1)
        
else:
    _c = 0
    with open('settings.conf','r') as fl:
        data = fl.readlines()
    print(data)
    for i in data:
        if "HIGH_FREQUENCY=" in i:
            _c += 1
            high_freq = i[15:-1]
        elif "LOW_FREQUENCY=" in i:
            _c += 1
            low_freq = i[14:-1]
        elif "DEFAULT_FREQUENCY=" in i:
            _c += 1
            def_freq = i[17:-1]
        elif "DEFAULT_DIRECTORY=" in i:
            _c += 1
            def_dir = i[18:-1]
        else:
            pass
    if _c != 4:
        display("Invalid Config File")
        exit()
print(def_dir)
    
if __name__ == '__main__':
    main_menu()
        
        
    