import os

def write_file(filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("Este es el texto inicial del README.md\n")


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def update_file(filepath):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write("Este texto ha sido añadido posteriormente.\n")


def clear_file(filepath):
    open(filepath, "w").close()


def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
