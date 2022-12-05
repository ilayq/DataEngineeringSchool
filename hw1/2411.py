from random import randint


def game() -> None:
    print("choose mode: solo/duo")
    mode = input()
    if mode == 'solo':    
        n = randint(1, 100)
        c = 0
        while int(input()) != n:
            print("wrong")
            c += 1
        print(f"correct, {c} tries")
    elif mode == 'duo':
        n = int(input())
        c = 0
        while int(input()) != n:
            print("wrong")
            c += 1
        print(f"correct, {c} tries")
    else:
        print('Wrong mode, try again')
        game()


if __name__ == "__main__":
    game()
