import tkinter as tk

window = tk.Tk()
window.title("Example Tkinter")
window.geometry("200x200+500+250")
window.resizable(False, False)

label = tk.Label(window, text='Example Tk')
label.pack()

button = tk.Button(window, text="Quit", command=window.destroy)
button.pack()

print('Start')
window.mainloop()
print('FINISH')
