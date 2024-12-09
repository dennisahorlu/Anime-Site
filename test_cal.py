from cal import square

def main():
    test_square()


def test_square():
    if square(5) !=25:
        print("2 squared was not 4")
    elif square(5) == 25:
        print("Test passed successfully!")

    if square(3) !=9:
        print("3 squared was not 9")
    elif square(3) == 9:
        print("Congrats!, test was successful")

if __name__== "__main__":
    main()