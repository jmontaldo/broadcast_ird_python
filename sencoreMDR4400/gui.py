from main import buscar
import tkinter as tk

def search():
    value = input_value.get()
    data = buscar(value)
    text_space.delete("1.0", tk.END)
    text_space.insert(tk.END, data)

window = tk.Tk()
window.title("Monitor")

input_label = tk.Label(window, text="Ingresa el numero de ID: ")
input_label.pack(pady=5)
input_value = tk.Entry(window)
input_value.pack(pady=5)

button = tk.Button(window, text="Buscar", command=search)
button.pack(pady=10)

text_space = tk.Text(window, height=18, width=40)
text_space.pack(pady=10)

window.mainloop()
