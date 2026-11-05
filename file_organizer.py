import os
import shutil

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("Folder does not exist.")
else:
    print("Organizing files in the folder...")
    file_types = {
        "Images": [
            ".jpg", ".jpeg", ".png", ".gif", ".bmp",
            ".svg", ".webp", ".ico", ".tiff"
        ],

        "Videos": [
            ".mp4", ".mkv", ".avi", ".mov",
            ".wmv", ".flv", ".webm"
        ],

        "Music": [
            ".mp3", ".wav", ".aac", ".flac",
            ".ogg", ".wma", ".m4a"
        ],

        "Documents": [
            ".pdf", ".doc", ".docx", ".txt",
            ".rtf", ".odt", ".tex", ".md"
        ],

        "Spreadsheets": [
            ".xls", ".xlsx", ".csv", ".ods"
        ],

        "Presentations": [
            ".ppt", ".pptx", ".odp"
        ],

        "Archives": [
            ".zip", ".rar", ".7z", ".tar",
            ".gz", ".bz2"
        ],

        "Code": [
            ".py", ".java", ".cpp", ".c", ".js",
            ".html", ".css", ".php", ".sql",
            ".json", ".xml", ".yaml", ".yml",
            ".sh", ".bat", ".ipynb"
        ],

        "Executables": [
            ".exe", ".msi", ".apk", ".app",
            ".deb", ".rpm"
        ],

        "Fonts": [
            ".ttf", ".otf", ".woff", ".woff2"
        ],

        "System": [
            ".dll", ".sys", ".ini", ".cfg"
        ],

        "Others": [
            ".iso", ".log", ".tmp", ".bak",
            ".dat", ".bin"
        ]
    }

    extensions = {ext: folder for folder, exts in file_types.items() for ext in exts}
    
    
    for file in os.listdir(folder_path):
        if file == os.path.basename(__file__):
            continue
        
        source = os.path.join(folder_path, file)
        if not os.path.isfile(source):
            continue
        
        file_ext = os.path.splitext(file)[1].lower()
        if file_ext in extensions:
            folder_name = extensions[file_ext]
            folder_dir = os.path.join(folder_path, folder_name)
            os.makedirs(folder_dir, exist_ok=True)
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_dir, file))
    
    
    
    # for folder_name, extensions in file_types.items():
    #     folder_dir = os.path.join(folder_path, folder_name)
    #     os.makedirs(folder_dir, exist_ok=True)
        
    #     for ext in extensions:
    #         for file in os.listdir(folder_path):
    #             if file == os.path.basename(__file__):
    #                 continue
    #             if file.lower().endswith(ext):
    #                 shutil.move(os.path.join(folder_path, file), os.path.join(folder_dir, file))
                    
    print("Files organized successfully!")
    
    
    