import os

FILENAME = "README.md"

def write_file():
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write("Este es el texto inicial del README.md\n")
    print("Archivo creado y texto escrito.")


def read_file():
    with open(FILENAME, "r", encoding="utf-8") as f:
        content = f.read()
    print("Contenido del archivo:")
    print(content)

def update_file():
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write("Este texto ha sido añadido posteriormente.\n")
    print("Archivo actualizado.")


def clear_file():
    open(FILENAME, "w").close()
    print("Contenido del archivo eliminado.")


def delete_file():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
        print("Archivo eliminado.")
    else:
        print("El archivo no existe.")

if __name__ == "__main__":
    write_file()
    read_file()
    update_file()
    read_file()
