import tkinter as tk

def s(event=None):
    n = e.get().strip()
    if n:
        r.config(text=f"¡Hola, {n}! ¿Todo piola?", fg="#A6E3A1")
    else:
        r.config(text="¡Che, poné un nombre!", fg="#F38BA8")

v = tk.Tk()
v.title("Saludador Piola")
v.geometry("400x350")
v.configure(bg="#1E1E2E")

f = tk.Frame(v, bg="#1E1E2E")
f.pack(expand=True)

tk.Label(f, text="¿Cómo te llamás?", font=("Segoe UI", 14, "bold"), bg="#1E1E2E", fg="#CDD6F4").pack(pady=(20, 10))

e = tk.Entry(f, font=("Segoe UI", 12), bg="#313244", fg="#CDD6F4", insertbackground="#CDD6F4", relief="flat", justify="center")
e.pack(pady=10, ipady=8, ipadx=10)
e.focus()

tk.Button(f, text="Saludar", font=("Segoe UI", 12, "bold"), bg="#89B4FA", fg="#1E1E2E", activebackground="#B4BEFE", activeforeground="#1E1E2E", relief="flat", cursor="hand2", command=s).pack(pady=15, ipadx=15, ipady=5)

r = tk.Label(f, text="", font=("Segoe UI", 14, "italic"), bg="#1E1E2E", fg="#A6E3A1")
r.pack(pady=10)

e.bind("<Return>", s)
v.mainloop()