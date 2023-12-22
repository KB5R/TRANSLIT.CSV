from config import SYMBOLS, DEFAULT_PASSWORD, FILE_PATH, START_ROWS
from classes import Transliterator, DataHandler


def main():
    tr = Transliterator(SYMBOLS)
    with DataHandler(FILE_PATH, START_ROWS) as dh:
        while True:
            full_name = input(
                "Введите имя в формате (Иванов Иван Иванович) или нажмите Ctrl + C или крестик, чтобы закончить\n: "
            ).lower().split()
            if len(full_name) != 3:
                print("Некорректные данные!")
                continue
            last_name, first_name, _ = full_name
            tr_last_name, tr_first_name, tr_middle_name = tr.transliterate(*full_name)
            login = f"{tr_last_name}.{tr_first_name[0]}.{tr_middle_name[0]}"
            dh.add_row(login, DEFAULT_PASSWORD, first_name.title(), last_name.title())


if __name__ == "__main__":
    main()
