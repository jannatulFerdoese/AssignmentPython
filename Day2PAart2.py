def intcode(nums):
    idx = 0
    while nums[idx] != 99:
        num = nums[idx]
        val1 = nums[nums[idx + 1]]
        val2 = nums[nums[idx + 2]]
        idx3 = nums[idx + 3]
        if num == 1:
            nums[idx3] = val1 + val2
        elif num == 2:
            nums[idx3] = val1 * val2
        idx += 4
    return nums

def calculate_output(program,y):
    for noun in range(100):
        for verb in range(100):
            program[1] = noun
            program[2] = verb
            program_arr = intcode(program.copy())

            if program_arr[0] == y:
                return 100 * noun + verb

if __name__ == "__main__":
    with open("Day2data.txt") as file:
        program = file.read()
        program = [int(x) for x in program.split(",")]
        y = 19690720
        output = calculate_output(program,y)
        print(output)