import ascii_magic
import tkinter as tk
import os

def image_to_ascii():
    ascii_path = "../ASCII.html"
    if os.path.exists(ascii_path):
        os.remove(ascii_path)
    url = image_url.get()
    if url:
        try:
            ascii_image = ascii_magic.from_url(url)
            ascii_image.to_html_file(ascii_path, columns=200, width_ratio=2)
            print("Converted image to ASCII")
            log_message.set("Converted image to ASCII: ASCII.html")
        except Exception as e:
            print(e)
            log_message.set("Error: " + str(e))
    else:
        log_message.set("Please mention a valid image link.")

#UI
root = tk.Tk()
root.title("Alpha")
root.geometry("600x400")


icon = tk.PhotoImage(file="logo.png")
icon = icon.subsample(16, 16)

logo = tk.Label(root, image=icon)
logo.pack(pady=5)

title = tk.Label(root, text="Alpha", font=("Arial", 20))
title.pack(pady=50)



image_url_title = tk.Label(root, text="Image URL", font=("Arial", 10))
image_url_title.pack()

image_url = tk.Entry(root)
image_url.pack()

image_url_button = tk.Button(root, text="Convert to ASCII", command=image_to_ascii)
image_url_button.pack()



log_message = tk.StringVar()
log_label = tk.Label(root, textvariable=log_message)
log_label.pack(pady=2)

credit = tk.Button(root, text="@GaelHF")
credit.pack()

root.mainloop()