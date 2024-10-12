import time

def print_slow(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

def love_confession():
    print_slow("Hey there!")
    time.sleep(1)
    print_slow("I have something I want to tell you...")
    time.sleep(2)
    print_slow("It's a bit nerve-racking, but here goes...")
    time.sleep(2)
    print_slow("...")
    time.sleep(2)
    print_slow("I like you!")
    time.sleep(1)
    print_slow("More than just a friend.")
    time.sleep(1.5)
    print_slow("I hope we can talk about this when you're ready. :)")
    time.sleep(2)
    print_slow("P.S. No pressure, just wanted to let you know how I feel!")

if __name__ == "__main__":
    love_confession()
