import os
import random
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def sanitize_path(folder_path):
    """Remove surrounding quotes from the path if present."""
    return folder_path.strip().strip('"').strip("'")

def find_video_files(folder):
    """Find all video files in a folder and its subfolders, excluding hidden files."""
    video_extensions = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v')
    video_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.startswith("._"):  # Skip hidden macOS files
                continue
            if file.lower().endswith(video_extensions):
                video_files.append(os.path.join(root, file))
    return video_files

def play_random_video():
    """Play a random video from the selected directory."""
    folder = folder_path.get().strip()
    folder = sanitize_path(folder)
    if not os.path.isdir(folder):
        messagebox.showerror("Error", f"The path '{folder}' is not a valid directory.")
        return

    video_files = find_video_files(folder)
    if not video_files:
        messagebox.showinfo("No Videos", "No video files found in the specified folder.")
        return

    video_file = random.choice(video_files)
    try:
        subprocess.run(["open", video_file], check=True)  # Uses 'open' for macOS
    except Exception as e:
        messagebox.showerror("Error", f"Failed to play video:\n{str(e)}")

def browse_folder():
    """Open a folder selection dialog."""
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

# GUI Setup
root = tk.Tk()
root.title("Random Video Player")
# root.geometry("400x150")

# Folder Selection
folder_path = tk.StringVar()
# Replace pack() with grid()
tk.Label(root, text="Select a folder containing videos:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=folder_path, width=50).grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_folder).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Play Random Video", command=play_random_video).grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
