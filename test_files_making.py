
import os
import random
import string

# Folder to create
folder = "Messy_Test_Folder"
os.makedirs(folder, exist_ok=True)

# Different file extensions
extensions = [
    ".jpg", ".png", ".jpeg", ".gif", ".svg",
    ".mp4", ".mkv", ".avi", ".mov",
    ".mp3", ".wav", ".flac",
    ".pdf", ".docx", ".txt", ".rtf",
    ".xlsx", ".xls", ".csv",
    ".pptx", ".ppt",
    ".zip", ".rar", ".7z",
    ".py", ".java", ".cpp", ".c", ".js",
    ".html", ".css", ".json", ".xml",
    ".exe", ".msi", ".apk",
    ".ttf", ".otf",
    ".iso", ".log", ".ini", ".dll",
    ".bin", ".dat", ".bak", ".md"
]

# Generate random filenames
total_files = 150

for i in range(total_files):
    ext = random.choice(extensions) #

    random_name = ''.join(
        random.choices(string.ascii_lowercase, k=6)
    )

    filename = f"{random_name}_{i}{ext}"
    filepath = os.path.join(folder, filename)

    with open(filepath, "w") as f:
        f.write(f"Test file: {filename}")

# Shuffle the directory listing isn't necessary;
# files are all in the same folder.

print("Messy folder created successfully!")
print(f"Location: {os.path.abspath(folder)}")
print(f"Total files: {total_files}")
