import csv


class Transliterator:
    def __init__(self, dictionary: dict[str, str]):
        """
        Объект для транслитерации
        :param dictionary: словарь где ключ - исходная буква, значение - транслитерированная
        """
        self._dictionary = dictionary

    def transliterate(self, *full_names: str) -> list[str]:
        """
        Транслитерация слова
        :param word: исходное слово
        :return: транслитерированное слово
        """
        return ["".join(
            self._dictionary.get(c, c) for c in full_name
        ) for full_name in full_names]


class DataHandler:
    def __init__(self, path: str, start_row: list[str]):
        """
        Объект для работы с данными, их
        :param path: путь к записываемому файлу с данными
        """
        self._path = path
        self._rows: list[list[str] | tuple[str]] = [start_row]

    def add_row(self, *row: str):
        """
        Добавление новой строки для записи в файл
        :param row: строка
        """
        self._rows.append(row)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self._path, "w", newline="") as file:
            csv.writer(file).writerows(self._rows)
