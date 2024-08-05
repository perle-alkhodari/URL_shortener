import ttkbootstrap as tb
import pyshorteners
from tkinter import messagebox


def submit():
    global first_run

    url = url_entry.get()
    if len(url) == 0:
        messagebox.showinfo("No URL", "Cannot submit an empty field.")
    else:
        new_url = convert_url(url)
        result_label.config(text=new_url)
        if first_run:
            copy_button.pack()
            first_run = False

def convert_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)

def copy_url():
    window.clipboard_clear()
    window.clipboard_append(result_label.cget("text"))
    window.update()

def center_window(w, h, win, push_y=0, push_x=0):
    x_coordinate = int((win.winfo_screenwidth() / 2) - (w / 2)) + push_x
    y_coordinate = int((win.winfo_screenheight() / 2) - (h / 2)) + push_y
    win.geometry(f"{w}x{h}+{x_coordinate}+{y_coordinate}")


background_color = "#180161"
light_background_color="#FFAAAA"
label_color = "#EB3678"
special_color = "#FB773C"

font_large = ("Futura", 18)
font_large_bold = ("Futura", 18, "bold")
font_medium = ("Futura", 14)
font_small = ("Futura", 10)

first_run = True

window = tb.Window()
window.title("Perle's URL Shortener")
window.config(background=background_color)
center_window(600, 400, window, -200)

title_label = tb.Label(window, text="URL Shortener", font=font_large_bold,
                       foreground=label_color,
                       background=background_color)
title_label.pack(pady=(50, 30))

frame_style = tb.Style()
frame_style.configure("frame.TFrame", background=background_color)
entry_frame = tb.Frame(window, style="frame.TFrame")
entry_frame.pack()

url_entry_label = tb.Label(entry_frame, text="URL", font=font_small,
                           foreground=special_color,
                           background=background_color)
url_entry_label.grid(row=0, column=0, padx=(0, 230))

url_entry = tb.Entry(entry_frame, width=17)
url_entry.grid(row=1, column=0, stick="e")

button_style = tb.Style()
button_style.configure("button.TButton", background=special_color, font=font_medium)
url_entry_button = tb.Button(entry_frame, text="Submit",
                             style="button.TButton",
                             command=submit)
url_entry_button.grid(row=1, column=1, padx=(0,30))

result_label = tb.Label(window, text="", font=font_medium,
                        foreground=special_color,
                        background=background_color)
result_label.pack(pady=(35, 0))

copy_button_style = tb.Style()
copy_button_style.configure("copy_button.TButton", background=background_color,
                            foreground=light_background_color,
                            font=font_small, borderwidth=0)
copy_button = tb.Button(window, text="Copy",
                        style="copy_button.TButton",
                        command=copy_url)
copy_button.pack()
copy_button.pack_forget()

window.mainloop()
