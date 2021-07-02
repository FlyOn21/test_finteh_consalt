def replacement_by_division():
    for char in range(11, 80):
        if char % 3 == 0 and char % 5 == 0:
            print("$$@@", end=' ')
        elif char % 3 == 0:
            print("$$", end=' ')
        elif char % 5 == 0:
            print("@@", end=' ')
        else:
            print(char, end=' ')


if __name__ == "__main__":
    replacement_by_division()
