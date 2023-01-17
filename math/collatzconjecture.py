from sys import argv

RED ='\033[0;31m'
RESET='\033[0;0m'

def err(string: str):
    print(f"{RED}{string}{RESET}")

def print_help():
        print(f"""Collatz Conjecture - the math magic.
Watch the 4-2-1 loop in your terminal.

    Usage: {argv[0]} <number> [iterations]

Iterations can be either an integer or set to "auto" to stop printing until the sequence reaches 1.""")

def numparse(num: int | str) -> int:
    try:
        parsed = int(num)

        if parsed < 0:
            err(f"ERROR: negative number not allowed")
            exit(1)

        return int(num)
    except ValueError:
        err(f"ERROR: invalid number: {num}")
        exit(1)

if len(argv) > 1:
    if argv[1] == "--help":
        print_help()
        exit(0)
    NUM = numparse(argv[1])
    if len(argv) < 3:
        ITER = "auto"
    else:
        ITER = numparse(argv[2])

else:
    err("ERROR: no arguments supplied!")
    exit(1)

def calculate(num: int) -> int:
    if num % 2:
        ans = int(num * 3 + 1)
        print(f"{num} × 3 + 1 = {RED}{ans}{RESET}")
    else:
        ans = int(num / 2)
        print(f"{num} ÷ 2 = {RED}{ans}{RESET}")

    return ans

def loop() -> None:
    i = 0
    ans = NUM
    while i < ITER:
        ans = int(calculate(ans))
        i += 1

def loop_auto() -> None:
    i = 0
    ans = NUM
    while ans != 1:
        ans = int(calculate(ans))
        i += 1

def main():
    try:
        print(f"{RED}Collatz Conjecture of {NUM}{RESET}")

        if ITER == "auto":
            loop_auto()
        else:
            loop()
    except KeyboardInterrupt:
        err("Terminated")

main()