from sys import argv
from commands import *
from tools import split_command, moooo_to_digit, Jump_To_Point
from re import findall


def run_command(command, commands, slots, line, points):
    command, args = split_command(command)

    command = moooo_to_digit(command)

    for command_starter in commands:
        if command_starter.command == command:
            print(command_starter.run(args, slots, line, points))
            return

    print("0, Unknown command, line " + str(line))


class Command:
    def __init__(self, arg_amount, command) -> None:
        self.arg_amount = arg_amount
        self.command = command

    def verify(self, args, line):
        if len(args) != self.arg_amount:
            return "0, invalid args, line: " + str(line)

    def run(self, args, slots, line, points):
        error = self.verify(args, line)
        if error:
            return error
        return_value = self.logic(args, slots, line, points)
        return return_value


def run_commands(file_contents, current, commands, slots, points):
    if len(file_contents) <= current:
        return

    if len(file_contents[current]) == 0:
        return

    line = file_contents[current]
    if line[0] == "m":
        line = line[1:]
        return_value = run_command(line, commands, slots, current, points)
        if isinstance(return_value, Jump_To_Point):
            current = -1
            for point in points:
                if point.point == return_value.point:
                    current = point.line
            if point == -1:
                print("ERR")
                return "0, invalid args, line: " + str(line)
            print("current", current)
            run_commands(file_contents, current, commands, slots, points)
        else:
            run_commands(file_contents, current+1, commands, slots, points)
    else:
        run_commands(file_contents, current+1, commands, slots, points)


def run():
    print("Welcome to MooLan, mOooOoOOoOOOooO")

    slots = [0] * 1023
    points = []

    commands = []

    commands.append(Put_Command(2, 0))
    commands.append(Print_Command(2, 1))
    commands.append(Copy_Command(2, 2))
    commands.append(Add1_Command(2, 3))
    commands.append(Add2_Command(3, 4))
    commands.append(Subtract1_Command(2, 5))
    commands.append(Subtract2_Command(3, 6))
    commands.append(Devide1_Command(2, 7))
    commands.append(Devide2_Command(3, 8))
    commands.append(Multiply1_Command(2, 9))
    commands.append(Multiply2_Command(3, 10))
    commands.append(Jump_Command(1, 11))
    commands.append(Point_Command(1, 12))

    with open(argv[1], "r") as f:
        file_contents = f.read()
    file_contents = file_contents.split("\n")
    run_commands(file_contents, 0, commands, slots, points)


if __name__ == "__main__":
    run()
