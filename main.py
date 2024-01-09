import csv

DEFAULT_PASSWORD = "dVEjRhm5"
STOP_WORDS = ["stop", "STOP"]


def transliterate(name):

    dictionary = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'c',
        'ч': 'cz',
        'ш': 'sh',
        'щ': 'sch',
        'ъ': '',
        'ы': 'y',
        'ь': '',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'ZH',
        'З': 'Z',
        'И': 'I',
        'Й': 'Y',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'C',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Sch',
        'Ъ': '',
        'Ы': 'y',
        'Ь': '',
        'Э': 'E',
        'Ю': 'Yu',
        'Я': 'Ya',
        ',': '',
        '?': '',
        ' ': ' ',
        '~': '',
        '!': '',
        '@': '',
        '#': '',
        '$': '',
        '%': '',
        '^': '',
        '&': '',
        '*': '',
        '(': '',
        ')': '',
        '-': '',
        '=': '',
        '+': '',
        ':': '',
        ';': '',
        '<': '',
        '>': '',
        '\'': '',
        '"': '',
        '\\': '',
        '/': '',
        '№': '',
        '[': '',
        ']': '',
        '{': '',
        '}': '',
        'ґ': '',
        'ї': '',
        'є': '',
        'Ґ': 'g',
        'Ї': 'i',
        'Є': 'e',
        '—': ''
    }

    for key in dictionary:
        name = name.replace(key, dictionary[key])
    return name


def main():

    def __save_rows(rows):
        with open("users.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for row in rows:
                writer.writerow(row)

    new_rows = [['username:', 'password:', 'firstname:', 'lastname:']]
    try:
        words = input(
            "Введите имена пользователей (через пробел) или введите 'STOP', чтобы закончить: "
        )
        while words not in STOP_WORDS:
            name = words.split()
            formatted_name = transliterate(words.lower()).split()
            login = f"{formatted_name[0]}.{formatted_name[1][0]}.{formatted_name[2][0]}"
            new_rows.append([login, DEFAULT_PASSWORD, name[1], name[0]])
            print("Пользователь добавлен в файл.")
            words = input(
                "Введите имена пользователей (через пробел) или введите 'STOP', чтобы закончить: "
            )
            __save_rows(new_rows)
    except KeyboardInterrupt:
        __save_rows(new_rows)
        exit()


if __name__ == "__main__":
    main()
