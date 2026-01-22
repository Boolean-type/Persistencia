import os
from persistencia import *

def test_write_file_creates_file(tmp_path):
    # Testea que write_file crea el archivo si no existe
    file = tmp_path / "README.md"
    write_file(file)
    assert file.exists()

def test_write_file_overwrites_existing_content(tmp_path):
    # Testea que write_file sobrescribe el contenido previo del archivo
    file = tmp_path / "README.md"
    file.write_text("Contenido antiguo", encoding="utf-8")
    write_file(file)
    content = file.read_text(encoding="utf-8")   
    # El contenido antiguo no debe existir
    assert "Contenido antiguo" not in content
    assert "texto inicial" in content


def test_read_file_returns_content(tmp_path):
    # Testea que read_file devuelve correctamente el contenido del archivo
    file = tmp_path / "README.md"
    file.write_text("Hola mundo", encoding="utf-8")
    content = read_file(file)
    assert content == "Hola mundo"


def test_read_file_empty_file(tmp_path):
    # Testea que read_file devuelve una cadena vacía si el archivo está vacío
    file = tmp_path / "README.md"
    file.touch()
    content = read_file(file)
    assert content == ""



def test_update_file_appends_content(tmp_path):
    # Testea que update_file añade contenido sin borrar el existente
    file = tmp_path / "README.md"
    write_file(file)
    update_file(file)
    content = file.read_text(encoding="utf-8")
    assert "texto inicial" in content
    assert "añadido posteriormente" in content


def test_update_file_creates_file_if_missing(tmp_path):
    # Testea que update_file crea el archivo si no existe
    file = tmp_path / "README.md"
    update_file(file)
    assert file.exists()


def test_clear_file_empties_content(tmp_path):
    # Testea que clear_file elimina todo el contenido del archivo
    file = tmp_path / "README.md"
    write_file(file)
    clear_file(file)
    assert file.read_text(encoding="utf-8") == ""


def test_clear_file_keeps_file(tmp_path):
    # Testea que clear_file no elimina el archivo, solo su contenido
    file = tmp_path / "README.md"
    write_file(file)
    clear_file(file)
    assert file.exists()


def test_delete_file_removes_file(tmp_path):
    # Testea que delete_file elimina el archivo si existe
    file = tmp_path / "README.md"
    write_file(file)
    delete_file(file)
    assert not file.exists()


def test_delete_file_when_file_does_not_exist(tmp_path):
    # Testea que delete_file no falla si el archivo no existe
    file = tmp_path / "README.md"
    delete_file(file)
    assert not file.exists()