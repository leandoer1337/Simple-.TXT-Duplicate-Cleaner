import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from collections import Counter
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works in dev & PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Clean file utility
def clean_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    counter = Counter(lines)
    duplicates = {line: count for line, count in counter.items() if count > 1}
    cleaned_lines = list(dict.fromkeys(lines))  # Preserves order
    return cleaned_lines, duplicates

# Clean single file
def scan_and_clean_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return
    try:
        cleaned_lines, duplicates = clean_file(file_path)
        cleaned_path = os.path.join(
            os.path.dirname(file_path),
            f"{os.path.splitext(os.path.basename(file_path))[0]}_cleaned.txt"
        )
        with open(cleaned_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(cleaned_lines))
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Cleaned: {os.path.basename(file_path)}\n")
        result_text.insert(tk.END, f"Saved as: {os.path.basename(cleaned_path)}\n\n")
        if duplicates:
            result_text.insert(tk.END, "Removed duplicate lines:\n\n")
            for line, count in duplicates.items():
                result_text.insert(tk.END, f'"{line}" - appeared {count} times\n')
        else:
            result_text.insert(tk.END, "No duplicates found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to clean the file:\n{e}")

# Clean folder
def scan_and_clean_folder():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return
    result_text.delete(1.0, tk.END)
    summary = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                cleaned_lines, duplicates = clean_file(file_path)
                cleaned_file_path = os.path.join(
                    folder_path,
                    f"{os.path.splitext(filename)[0]}_cleaned.txt"
                )
                with open(cleaned_file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(cleaned_lines))
                summary += f"File: {filename}\n"
                if duplicates:
                    summary += f"Removed {sum(count - 1 for count in duplicates.values())} duplicates.\n"
                    summary += f"Saved: {os.path.basename(cleaned_file_path)}\n\n"
                else:
                    summary += f"No duplicates found. Cleaned file still saved.\n\n"
            except Exception as e:
                summary += f"Error processing {filename}: {str(e)}\n\n"
    result_text.insert(tk.END, summary or "No .txt files found in the selected folder.")

# Dark theme colors
BG_COLOR = "#1e1e1e"
FG_COLOR = "#dcdcdc"
BTN_COLOR = "#333333"
BTN_HOVER = "#444444"
FONT = ("Consolas", 10)

# GUI setup
root = tk.Tk()
root.title("Simple .TXT Duplicate Cleaner")
root.geometry("750x520")
root.configure(bg=BG_COLOR)
root.iconbitmap(resource_path("icon.ico"))

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(pady=10)

def on_enter(e): e.widget.config(bg=BTN_HOVER)
def on_leave(e): e.widget.config(bg=BTN_COLOR)

btn_file = tk.Button(frame, text="Clean Single .TXT File", command=scan_and_clean_file,
                     width=30, bg=BTN_COLOR, fg=FG_COLOR, font=FONT, relief=tk.FLAT)
btn_file.grid(row=0, column=0, padx=10)
btn_file.bind("<Enter>", on_enter)
btn_file.bind("<Leave>", on_leave)

btn_folder = tk.Button(frame, text="Clean Folder of .TXT Files", command=scan_and_clean_folder,
                       width=30, bg=BTN_COLOR, fg=FG_COLOR, font=FONT, relief=tk.FLAT)
btn_folder.grid(row=0, column=1, padx=10)
btn_folder.bind("<Enter>", on_enter)
btn_folder.bind("<Leave>", on_leave)

result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=25,
                                        bg="#2a2a2a", fg=FG_COLOR, insertbackground=FG_COLOR,
                                        font=FONT)
result_text.pack(padx=10, pady=10)

root.mainloop()
