import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json

config_file = "config.json"


def load_config():
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            return json.load(file)
    return {"delay": 600, "use_custom_file": False, "custom_file_path": ""}


def save_config(config):
    with open(config_file, "w") as file:
        json.dump(config, file, indent=4)


def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a Quotes File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        custom_file_var.set(file_path)


def apply_changes():
    config = {
        "delay": int(delay_var.get()),
        "use_custom_file": use_custom_var.get(),
        "custom_file_path": custom_file_var.get()
    }
    save_config(config)
    messagebox.showinfo("Settings Saved", "The settings have been saved successfully!")

config = load_config()

root = tk.Tk()
root.title("Motivational Reminder Manager")
root.geometry("400x300")


tk.Label(root, text="Notification Delay (in seconds):").pack(pady=10)
delay_var = tk.StringVar(value=str(config["delay"]))
tk.Entry(root, textvariable=delay_var).pack()

use_custom_var = tk.BooleanVar(value=config["use_custom_file"])
tk.Checkbutton(root, text="Use Custom Quotes File", variable=use_custom_var).pack(pady=10)

custom_file_var = tk.StringVar(value=config["custom_file_path"])
file_frame = tk.Frame(root)
file_frame.pack(pady=5)
tk.Entry(file_frame, textvariable=custom_file_var, width=30, state="disabled").pack(side="left", padx=5)
tk.Button(file_frame, text="Browse", command=select_file).pack(side="left")

tk.Button(root, text="Apply", command=apply_changes).pack(pady=20)
root.mainloop()
