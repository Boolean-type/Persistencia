from persistencia import *

FILEPATH = "README.md"
if __name__ == "__main__":
    write_file(FILEPATH)
    read_file(FILEPATH)
    update_file(FILEPATH)
    read_file(FILEPATH)
