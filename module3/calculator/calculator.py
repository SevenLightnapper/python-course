import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg='darkgrey')

        self.center_window(500, 500)

        self.entry = tk.Entry(root, width=20, font=('Arial', 24),
                              borderwidth=2, relief='solid', bg='white', fg='black')
        self.entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky="ew")

        self.create_buttons()

    def center_window(self, window_width, window_height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0

        for button in buttons:
            command = lambda x=button: self.on_button_click(x)
            (tk.Button(self.root, text=button, width=5, height=2, font=('Arial', 18),
                       command=command, bg='grey', fg='white', overrelief='solid')
             .grid(row=row, column=col, padx=5, pady=5, sticky="nsew"))
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        for i in range(1, 5):
            self.root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

        else:
            current_text = self.entry.get()
            new_text = current_text + str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, new_text)


if __name__ == "__main__":
    root_ = tk.Tk()
    calc = Calculator(root_)
    root_.mainloop()
