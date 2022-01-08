def moooo_to_digit(moooo):
    binary = moooo.replace("o", "0")
    binary = binary.replace("O", "1")

    return int(binary, 2)


def digit_to_moooo(digit):
    binary = format(digit, "b")

    moooo = binary.replace("0", "o")
    moooo = moooo.replace("1", "O")

    return moooo


def split_command(command):
    command = command.split(" ")

    return command[0], command[1:]


class Jump_To_Point():
    def __init__(self, point):
        self.point = point


class Point():
    def __init__(self, point, line):
        self.point = point
        self.line = line
