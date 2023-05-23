def fuel(mass):
    return mass // 3 - 2


def sum_fuel_required(masses):
    return sum(fuel(mass) for mass in masses)


if __name__ == '__main__':
    masses = []
    with open("Day1data.txt") as file:
        for line in file:
            masses.append(int(line.strip()))

    print(f"result : {sum_fuel_required(masses)}")
