from tools import digit_to_moooo, moooo_to_digit, Jump_To_Point
from main import Command


class Put_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot = moooo_to_digit(args[0])
        value = moooo_to_digit(args[1])

        slots[slot] = value

        return "1"


class Print_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot = moooo_to_digit(args[0])
        type = moooo_to_digit(args[1])

        if type == 0:
            return "m" + digit_to_moooo(slots[slot])
        elif type == 1:
            return slots[slot]
        elif type == 2:
            return chr(slots[slot])

        return "0, Incorrect type, line " + str(line)


class Copy_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot_from = moooo_to_digit(args[0])
        slot_to = moooo_to_digit(args[1])

        slots[slot_to] = slots[slot_from]

        return "1"


class Add1_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot = moooo_to_digit(args[0])
        amount = moooo_to_digit(args[1])

        slots[slot] += amount

        return "1"


class Add2_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot1 = moooo_to_digit(args[0])
        slot2 = moooo_to_digit(args[1])
        slot_out = moooo_to_digit(args[2])

        slots[slot_out] = slots[slot1] + slots[slot2]

        return "1"


class Subtract1_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot = moooo_to_digit(args[0])
        amount = moooo_to_digit(args[1])

        slots[slot] -= amount

        return "1"


class Subtract2_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot1 = moooo_to_digit(args[0])
        slot2 = moooo_to_digit(args[1])
        slot_out = moooo_to_digit(args[2])

        slots[slot_out] = slots[slot1] - slots[slot2]

        return "1"


class Devide1_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot = moooo_to_digit(args[0])
        amount = moooo_to_digit(args[1])

        slots[slot] /= amount

        return "1"


class Devide2_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot1 = moooo_to_digit(args[0])
        slot2 = moooo_to_digit(args[1])
        slot_out = moooo_to_digit(args[2])

        slots[slot_out] = slots[slot1] / slots[slot2]

        return "1"


class Multiply1_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot = moooo_to_digit(args[0])
        amount = moooo_to_digit(args[1])

        slots[slot] *= amount

        return "1"


class Multiply2_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        slot1 = moooo_to_digit(args[0])
        slot2 = moooo_to_digit(args[1])
        slot_out = moooo_to_digit(args[2])

        slots[slot_out] = slots[slot1] * slots[slot2]

        return "1"


class Jump_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        point = moooo_to_digit(args[0])

        return Jump_To_Point(point)


class Point_Command(Command):
    def logic(self, args, slots, line, points) -> str:
        point = moooo_to_digit(args[0])

        points.append(Jump_To_Point(point))
