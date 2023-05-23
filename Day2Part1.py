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

if __name__=="__main__":
 with open("Day2data.txt") as file:
     program = file.read()
     program = [int(n) for n in program.split(",")]
     program[1] = 12
     program[2] = 2
     intcode(program)
     print(program[0])