import base64


def justify(line: str):
    return line.rstrip() + " " * (8 - len(line.rstrip())) + "\n"


def encode(lines: list[str]) -> str:
    return base64.b64encode("".join(lines).encode()).decode()


with open("symbols.txt", "r") as file:
    lines = file.readlines()
    print(*lines)
    lines = list(map(justify, lines))
    print(encode(lines))
