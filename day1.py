import typing as t


def main():
    measurements = read_input("input1.txt")
    increases = sliding_window_increase(measurements)
    print(increases)


def count_increase(measurements: t.List[int]) -> int:
    total_increase = 0
    current: t.Optional[int] = None

    for i in measurements:
        if current is not None and i > current:
            total_increase += 1
        current = i

    return total_increase


def sliding_window_increase(measurements: t.List[int]) -> int:
    total_increase = 0
    first_i = 0
    current = sum(measurements[:3])

    for i in measurements[3:]:
        n = (current - measurements[first_i]) + i
        if n > current:
            total_increase += 1
        current = n
        first_i += 1

    return total_increase


def read_input(filename) -> t.List[int]:
    with open(filename) as fp:
        res = fp.read().split()

    return [int(i) for i in res]


if __name__ == "__main__":
    main()
