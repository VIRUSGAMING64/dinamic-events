import os
import shutil
from pathlib import Path

def remove_directory(path):
    if path.exists() and path.is_dir():
        try:
            shutil.rmtree(path)
            print(f"Removed directory: {path}")
        except Exception as e:
            print(f"Error removing {path}: {e}")

def remove_file(path):
    if path.exists() and path.is_file():
        try:
            os.remove(path)
            print(f"Removed file: {path}")
        except Exception as e:
            print(f"Error removing {path}: {e}")

def clean_project():
    root_dir = Path(__file__).parent
    dirs_to_remove = ["__pycache__", ".cph"]
    
    for path in root_dir.rglob("*"):
        if path.is_dir() and path.name in dirs_to_remove:
            remove_directory(path)
            
    remove_directory(root_dir / "saved")
    remove_file(root_dir / "logs.txt")

    print("Cleanup complete.")

if __name__ == "__main__":
    clean_project()
