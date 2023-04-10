import re


def read_template(str):
    with open(str) as file:
        return file.read().strip()


def parse_template(str: str):
    regex_pattern = r"{(.+?)}"  # match all the words between the curly braces

    stripped = re.sub(regex_pattern, "{}", str)
    parts = tuple(re.findall(regex_pattern, str))

    return stripped, parts


def merge(str: str, answers: tuple):
    return str.format(*answers)


def write_result(str: str, path: str):
    with open(path, "w") as file:
        file.write(str)
        print()
        print(f"Your result has been written to {path}.")


def main():
    print("Welcome to Madlibs!")
    print('you will be asked to enter words to fill out a story.')
    print('after you enter all the words, the story will be printer to you and written to a file.')

    path = "assets/make_me_a_video_game_template.txt"
    template = read_template(path)

    stripped, parts = parse_template(template)

    answers = []
    for part in parts:
        answer = input(f"Give me a {part}: ")
        answers.append(answer)

    result = merge(stripped, tuple(answers))

    print(result)
    write_result(result, "assets/your_result.txt")


if __name__ == "__main__":
    main()
