import tkinter as tk
from tkinter import ttk

class Card:
    def __init__(self, parent, image_path, caption, username):
        self.parent = parent
        self.image_path = image_path
        self.caption = caption
        self.username = username
        self.card_frame = tk.Frame(self.parent, bg='white', bd=2, relief='groove')
        self.card_frame.pack(pady=50, padx=50, fill='x')
        self.image_label = tk.Label(self.card_frame, image=self.image_path)
        self.image_label.pack(side='left', padx=10, pady=10)
        self.caption_label = tk.Label(self.card_frame, text=self.caption, font=('Arial', 14), wraplength=500)
        self.caption_label.pack(side='top', padx=10, pady=(10, 0))
        self.username_label = tk.Label(self.card_frame, text=self.username, font=('Arial', 12))
        self.username_label.pack(side='top', padx=10, pady=(0, 10))

class ScrollableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind('<Configure>', lambda event: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side='left', fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')

    def add_card(self, image_path, caption, username):
        card = Card(self.scrollable_frame, image_path, caption, username)
        card.pack(fill='x', padx=10, pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x700')

    scrollable_frame = ScrollableFrame(root)
    scrollable_frame.pack(fill='both', expand=True)

    for i in range(10):
        scrollable_frame.add_card('logo.png', f"Example caption {i+1}", f"Example username {i+1}")

    root.mainloop()
