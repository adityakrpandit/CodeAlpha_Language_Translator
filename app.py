import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from deep_translator import GoogleTranslator
import pyperclip

# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("AI Language Translator Pro")
root.geometry("900x650")
root.configure(bg="#f4f6f9")
root.resizable(False, False)

# ---------------- LANGUAGES ---------------- #

languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Turkish": "tr"
}

history = []

# ---------------- FUNCTIONS ---------------- #

def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()

        if text == "":
            messagebox.showwarning(
                "Warning",
                "Please enter some text."
            )
            return

        source = languages[source_lang.get()]
        target = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

        history.append(
            f"{source_lang.get()} ➜ {target_lang.get()}\n{text}\n{translated}\n"
        )

        status.config(text="✅ Translation Successful")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- OTHER FUNCTIONS ---------------- #

def copy_text():
    text = output_text.get("1.0", tk.END).strip()

    if text:
        pyperclip.copy(text)
        status.config(text="📋 Text Copied")


def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    status.config(text="🗑 Cleared")


def swap_languages():
    source = source_lang.get()
    target = target_lang.get()

    if source == "Auto Detect":
        messagebox.showinfo(
            "Info",
            "Auto Detect cannot be swapped."
        )
        return

    source_lang.set(target)
    target_lang.set(source)
    status.config(text="🔄 Languages Swapped")


def save_translation():
    text = output_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning(
            "Warning",
            "Nothing to save."
        )
        return

    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File", "*.txt")]
    )

    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text)

        status.config(text="💾 File Saved")


def show_history():

    if len(history) == 0:
        messagebox.showinfo(
            "History",
            "No translations yet."
        )
        return

    history_window = tk.Toplevel(root)
    history_window.title("Translation History")
    history_window.geometry("700x500")

    txt = tk.Text(history_window, wrap="word")
    txt.pack(fill="both", expand=True)

    txt.insert("1.0", "\n\n".join(history))

# ---------------- TITLE ---------------- #

title = tk.Label(
root,
text="🌍 AI Language Translator Pro",
font=("Arial", 22, "bold"),
bg="#f4f6f9",
fg="#2c3e50"
)
title.pack(pady=15)

# ---------------- SOURCE LANGUAGE ---------------- #

tk.Label(
root,
text="Source Language",
bg="#f4f6f9",
font=("Arial",12)
).pack()

source_lang = ttk.Combobox(
root,
values=list(languages.keys()),
state="readonly",
width=30
)
source_lang.current(1)     
source_lang.pack(pady=5)

# ---------------- INPUT ---------------- #

tk.Label(
root,
text="Enter Text",
bg="#f4f6f9",
font=("Arial",12)
).pack()

input_text = tk.Text(
root,
height=7,
width=85,
font=("Arial",11)
)
input_text.pack(pady=10)

# ---------------- TARGET LANGUAGE ---------------- #

tk.Label(
root,
text="Target Language",
bg="#f4f6f9",
font=("Arial",12)
).pack()

target_lang = ttk.Combobox(
root,
values=list(languages.keys())[1:],
state="readonly",
width=30
)
target_lang.current(0)     
target_lang.pack(pady=5)

# ---------------- BUTTONS ---------------- #

button_frame = tk.Frame(root, bg="#f4f6f9")
button_frame.pack(pady=15)

buttons = [
("Translate", translate_text, "#3498db"),
("Copy", copy_text, "#27ae60"),
("Swap", swap_languages, "#f39c12"),
("Clear", clear_text, "#e74c3c"),
("Save", save_translation, "#8e44ad"),
("History", show_history, "#16a085")
]

for i, (text, cmd, color) in enumerate(buttons):
    tk.Button(
        button_frame,
        text=text,
        command=cmd,
        bg=color,
        fg="white",
        font=("Arial",11,"bold"),
        width=12
    ).grid(row=0,column=i,padx=5)

# ---------------- OUTPUT ---------------- #

tk.Label(
root,
text="Translated Text",
bg="#f4f6f9",
font=("Arial",12)
).pack()

output_text = tk.Text(
root,
height=7,
width=85,
font=("Arial",11)
)
output_text.pack(pady=10)

# ---------------- STATUS BAR ---------------- #

status = tk.Label(
root,
text="Ready",
bg="#34495e",
fg="white",
anchor="w",
padx=10
)
status.pack(fill="x", side="bottom")

# ---------------- RUN ---------------- #

root.mainloop()