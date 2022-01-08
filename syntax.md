# CowLan Docs:

## Basics:

MooLan consists of 1023 slots, every slot can store a number from 0 up to 1023.

Start every line with `m`, other lines will be ignored.

`o` = `0`

`O` = `1`

## Command Structure:

`<COMMAND> <ARG1> <ARG2> <ARG3> etc...`

## Commands:

- Put:
  - Description: Puts a number in a slot.
  - Usage: `mo <SLOT> <VALUE>`, Example: `mo Oo OoOo` (Puts 10 in slot 2)
- Print:
  - Description: Prints contents of a slot.
  - Usage: `mO <SLOT> <TYPE: BINARY(0)/INT(1)/ASCII(2)>`, Example: `mO Oo O` (Prints contents of slot 2 as an int)
- Copy:
  - Description: Copies the contents of a slot to another one.
  - Usage: `mOo <SLOT FROM> <SLOT TO>`, Example: `mO Oo OO` (Copies content of slot 2 to 3)
- Add 1:
  - Description: Adds a number to the contents of a slot.
  - Usage: `mOO <SLOT> <AMOUNT>`, Example: `mOO OO Ooo` (Adds 4 to slot 3)
- Add 2:
  - Description: Adds contents of 2 slots together.
  - Usage: `mOoo <SLOT 1> <SLOT 2> <SLOT OUT>`, Example: `mOoo Oo OO o` (Adds slot 2 and 3 together and puts the output in slot 1)
- Subtract 1:
  - Description: Subtracts a number to the contents of a slot.
  - Usage: `mOoO <SLOT> <AMOUNT>`, Example: `mOoO OO Ooo` (Subtracts 4 to slot 3)
- Subtract 2:
  - Description: Subtracts contents of 2 slots from each other.
  - Usage: `mOOo <SLOT 1> <SLOT 2> <SLOT OUT>`, Example: `mOOo Oo OO o` (Subtracts slot 2 and 3 and puts the output in slot 1)
- Devide 1:
  - Description: Devides a number to the contents of a slot.
  - Usage: `mOOO <SLOT> <AMOUNT>`, Example: `mOOO OO Ooo` (Devides 4 to slot 3)
- Devide 2:
  - Description: Devides contents of 2 slots.
  - Usage: `mOooo <SLOT 1> <SLOT 2> <SLOT OUT>`, Example: `mOooo Oo OO o` (Devides slot 2 and 3 and puts the output in slot 1)
- Multiply 1:
  - Description: Multiplies a number to the contents of a slot.
  - Usage: `mOooO <SLOT> <AMOUNT>`, Example: `mOooO OO Ooo` (Multiplies 4 to slot 3)
- Multiply 2:
  - Description: Multiplies contents of 2 slots together.
  - Usage: `mOoOo <SLOT 1> <SLOT 2> <SLOT OUT>`, Example: `mOoOo Oo OO o` (Multiplies slot 2 and 3 together and puts the output in slot 1)
- Jump
  - Description: Jumps to another point
  - Usage: `mOoOO <POINT ID>`, Example: `mOoOo OO` (Jumps to point 3)
  - Notes:
    - Point has to be defined **BEFORE** the jump
- Point
  - Description: A point to jump to later
  - Usage: `mOOoo <POINT ID>`, Example: `mOoOo OO` (Creates point 3)
