# import dependencies
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as tkm
import os

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "com.surgecorporation.surgeproductions.notesurge.v0.8.4-alpha"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

# start main application and command
window = Tk()
window.title("NoteSurge")

menu = Menu(window)
window.config(menu=menu)

editor = ScrolledText(window, font=("Helvetica 14"), wrap=WORD)
editor.pack(fill=BOTH, expand=1)
editor.focus()
file_path = ""



# crate a command that allows you to open a file from device
def open_file(event=None):
    global code, file_path

    open_path = askopenfilename(filetypes=[("Text File", "*.txt"), ("All Files", "*.*")])
    file_path = open_path

    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)

    orig_path = os.path.basename(open_path)
    File_Name = os.path.splitext(orig_path)[0]
    window.title(f"{File_Name} - NoteSurge")
        
# create a shortcut to open file
window.bind("<Control-o>", open_file)


# create a function that allows you to save a file to  your device
def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt"), ("All Files", "*.*")])
        file_path = save_path
    else:
        save_path = file_path
    
    with open(save_path, "w") as file:
            code = editor.get(1.0, END)
            file.write(code)


    orig_path = os.path.basename(save_path)
    File_Name = os.path.splitext(orig_path)[0]
    window.title(f"{File_Name} - NoteSurge")
        
    tkm.showinfo(title="Success", message="File Saved Successfully!")


# create a shortcut to save file that was just edited
window.bind("<Control-s>", save_file)

# create a function to save file for the first time with a certain name
def save_as(event=None):
    global code, file_path
    save_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt"), ("All Files", "*.*")])
    file_path = save_path

    with open(save_path, "w") as file:
            code = editor.get(1.0, END)
            file.write(code)


    orig_path = os.path.basename(save_path)
    File_Name = os.path.splitext(orig_path)[0]
    window.title(f"{File_Name} - NoteSurge")
        
    tkm.showinfo(title="Success", message="File Saved Successfully!")

window.bind("<Control-S>", save_as) 



def new_file():
    warn = tkm.askyesno(title="Warning", message="Did you save your file? \n If Not All Data Will Be Lost", icon="warning")
    
    if warn == True:
        global file_path
        editor.delete(1.0, END)
        file_path = ""
    
    


# create a function that allows you to close the file/ IDE
def close(event=None):
    warn = tkm.askyesno(title="Warning!", message="Are you sure you would like to close?", icon="warning")
    
    if warn == True:
        window.destroy()


window.bind("<Control-q>", close)


# create a command that allows you to cut, copy and paste text
def cut_text(event=None):
    editor.event_generate(("<<Cut>>"))


def copy_text(event=None):
    editor.event_generate(("<<Copy>>"))


def paste_text(event=None):
    editor.event_generate(("<<Paste>>"))
    


# create menus/navigation
file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
function_menu= Menu(menu, tearoff=0)
format_menu = Menu(menu, tearoff=0)
view_menu = Menu(menu, tearoff=0)

# name each menu
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="Functions", menu=function_menu)
menu.add_cascade(label="Format", menu=format_menu)
menu.add_cascade(label="View", menu=view_menu)

# create shortcut and names for commands
file_menu.add_command(label="New", accelerator="Ctrl+N", command=new_file)
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=close)

# create a shortcut and name to copy, paste and cut.
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=cut_text)
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=copy_text)
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=paste_text)

editor.tag_configure("start", background="yellow", foreground="blue")
editor.tag_configure("bold", font = ("Helvetica", "14", "bold"))
editor.tag_configure("ic", font = ("Helvetica", "14", "italic"))
editor.tag_configure("ue", font = ("Helvetica", "14", "underline"))
editor.tag_configure("allfn", font = ('Helvetica', '12', 'bold underline italic'))

editor.tag_configure('bit', font = ('Helvetica', '12', 'bold italic'))
editor.tag_configure('but', font = ('Helvetica', '12', 'bold underline'))
editor.tag_configure('uit', font = ('Helvetica', '12', 'underline italic'))
    

def highlight():
        try:
            editor.tag_add("start", "sel.first", "sel.last")        
        except Tk.TclError:
            pass
        
def clear_ht():
        editor.tag_remove("start",  "sel.first", 'sel.last')
        
def bold():
    try:
        editor.tag_add("bold", "sel.first", "sel.last")
    except Tk.TclError:
            pass
        
def clear_bd():
        editor.tag_remove("bold",  "sel.first", 'sel.last')\
            
def ic():
    try:
        editor.tag_add("ic", "sel.first", "sel.last")
    except Tk.TclError:
            pass
        
def clear_ic():
        editor.tag_remove("ic",  "sel.first", 'sel.last')
        
def ue():
    try:
        editor.tag_add("ue", "sel.first", "sel.last")
    except Tk.TclError:
            pass
        
def clear_ue():
        editor.tag_remove("ue",  "sel.first", 'sel.last')

def allfn():
    try:
        editor.tag_add("allfn", "sel.first", "sel.last")
    except Tk.TclError:
            pass
        
def clear_allfn():
        editor.tag_remove("allfn",  "sel.first", 'sel.last')
        
def bit():
    try:
        editor.tag_add("bit", "sel.first", "sel.last")
    except Tk.TclError:
            pass
        
def clear_bit():
        editor.tag_remove("bit",  "sel.first", 'sel.last')
        
def but():
    try:
        editor.tag_add("but", "sel.first", "sel.last")
    except Tk.TclError:
            pass
        
def clear_but():
        editor.tag_remove("but",  "sel.first", 'sel.last')
        
def uit():
    try:
        editor.tag_add("uit", "sel.first", "sel.last")
    except Tk.TclError:
            pass
        
def clear_uit():
        editor.tag_remove("uit",  "sel.first", 'sel.last')

# Functions
function_menu.add_command(label="Highlight", command=highlight)
function_menu.add_command(label="Undo Highlight", command=clear_ht)
function_menu.add_separator()
function_menu.add_command(label="Bold", command=bold)
function_menu.add_command(label="Undo Bold", command=clear_bd)
function_menu.add_separator()
function_menu.add_command(label="Italic", command=ic)
function_menu.add_command(label="Undo Italic", command=clear_ic)
function_menu.add_separator()
function_menu.add_command(label="Underline", command=ue)
function_menu.add_command(label="Undo Underline", command=clear_ue)
function_menu.add_separator()
function_menu.add_command(label="Underline & Bold & Italic", command=allfn)
function_menu.add_command(label="Undo Underline & Bold & Italic", command=clear_allfn)
function_menu.add_separator()
function_menu.add_command(label="Bold & Italic", command=bit)
function_menu.add_command(label="Undo Bold & Italic", command=clear_bit)
function_menu.add_separator()
function_menu.add_command(label="Underline & Bold", command=but)
function_menu.add_command(label="Undo Underline & Bold", command=clear_but)
function_menu.add_separator()
function_menu.add_command(label="Underline & Italic", command=uit)
function_menu.add_command(label="Undo Underline & Italic", command=clear_uit)

# change text to what you want to show on status bar
status_bars = ttk.Label(window, text="\t\t Surge Productions \t\t\t\t\t Characters: 0 \t Words: 0")
status_bars.pack(side="bottom")

# create a command that allows you to show or hide the status bar
show_status_bar = BooleanVar()
show_status_bar.set(True)


def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False
    else:
        status_bars.pack(side=BOTTOM)
        show_status_bar = True


view_menu.add_checkbutton(label="Status Bar",
                        onvalue=True,
                        offvalue=0,
                        variable=show_status_bar,
                        command=hide_statusbar)

text_change = False


# create a command that automatically changes word count and character count
def change_word(event=None):
    global text_change
    if editor.edit_modified():
        text_change = True
        word = len(editor.get(1.0, "end-1c").split())
        chararcter = len(editor.get(1.0, "end-1c").replace(" ", ""))
        status_bars.config(text=f"Surge Productions \t\t\t\t\t Characters: {chararcter} \t Words: {word}")
    editor.edit_modified(False)


editor.bind("<<Modified>>", change_word)

if file_path == "":
    start = tkm.askyesno(title="Start Up Question!",message="Would You Like To Open A File?", icon="question")

    if start == True:
        open_file()

window.iconbitmap(os.path.join(basedir, "icon.ico"))
window.mainloop()
