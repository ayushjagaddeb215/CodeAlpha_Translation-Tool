import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Language list
language_dict = {value.title(): key for key, value in LANGUAGES.items()}
languages = sorted(language_dict.keys())

# Initialize translator
translator = Translator()

# Function to perform translation
def translate_text():
    input_text = input_text_box.get("1.0", tk.END).strip()
    src_lang = source_lang.get()
    tgt_lang = target_lang.get()

    if not input_text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    try:
        src = language_dict[src_lang]
        tgt = language_dict[tgt_lang]
        translated = translator.translate(input_text, src=src, dest=tgt)
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# GUI Setup
app = tk.Tk()
app.title("Language Translation Tool")
app.geometry("600x400")
app.config(bg="#f0f0f0")

# Widgets
tk.Label(app, text="Enter Text", font=("Helvetica", 12)).pack(pady=5)
input_text_box = tk.Text(app, height=5, width=60)
input_text_box.pack()

frame = tk.Frame(app, bg="#f0f0f0")
frame.pack(pady=10)

tk.Label(frame, text="From:", font=("Helvetica", 10)).grid(row=0, column=0, padx=5)
source_lang = ttk.Combobox(frame, values=languages, width=20)
source_lang.set("English")
source_lang.grid(row=0, column=1)

tk.Label(frame, text="To:", font=("Helvetica", 10)).grid(row=0, column=2, padx=5)
target_lang = ttk.Combobox(frame, values=languages, width=20)
target_lang.set("Spanish")
target_lang.grid(row=0, column=3)

translate_btn = tk.Button(app, text="Translate", command=translate_text, bg="#4caf50", fg="white", padx=10, pady=5)
translate_btn.pack(pady=10)

tk.Label(app, text="Translated Text", font=("Helvetica", 12)).pack(pady=5)
output_text_box = tk.Text(app, height=5, width=60)
output_text_box.pack()

app.mainloop()
