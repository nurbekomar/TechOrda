import tkinter as tk

window = tk.Tk()
window.title('HW_19_2')
window.geometry("220x220+500+250")
window.resizable(False, False)
# window.attributes('-alpha', 0.5)

label_name = tk.Label(window, text='name: Nurbek')
label_name.pack()

label_age = tk.Label(window, text='age: 29')
label_age.pack()

label_email = tk.Label(window, text='email: omarnurbek13@gmail.com')
label_email.pack()

window.mainloop()
