def main():
    # 0 bit - zero write bit
    # 1 bit - zero move (0 is left, 1 is right)
    # 2-7 bits - zero state (0-63, 0 is halting)
    # 8 bit - one write bit
    # 9 bit - one move (0 is left, 1 is right)
    # 10-15 bit - one state (0-63, 0 is halting)

    tape = [1, 1, 0, 0, 0, 0, 0, 0]
    instructions = [0b0, 0b111100001010, 0b1001100000010, 0b1101100010010, 0b1011100010110, 0b1100000011, 0b1100000011]
    pointer = 0
    state = 1

    while state != 0:
        current_data = instructions[state]
        if tape[pointer] == 0:
            tape[pointer] = instructions[state] & 0b0000000000000001
            if ((instructions[state] & 0b0000000000000010) >> 1) == 0:
                pointer -= 1
            else:
                pointer += 1
            state = (instructions[state] & 0b0000000011111100) >> 2
        else:
            tape[pointer] = (instructions[state] & 0b0000000100000000) >> 8
            if ((instructions[state] & 0b0000001000000000) >> 9) == 0:
                pointer -= 1
            else:
                pointer += 1
            state = (instructions[state] & 0b1111110000000000) >> 10

    print(tape)

def create_state(zero_write, zero_move, zero_state, one_write, one_move, one_state):
    return (one_state << 10) + (one_move << 9) + (one_write << 8) + (zero_state << 2) + (zero_move << 1) + zero_write

if __name__ == "__main__":
    main()
