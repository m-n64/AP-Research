

def validate(message):
    check = input(message)
    if (check == "Y") or (check == "y"):
        return True
    elif (check == "N") or (check == "n"):
        return False
    else:
        return validate("Y/N: ")


if __name__ == "__main__":

    if validate("Continue? (Y/N): ") == True:
        print("Continuing")
    else:
        print("Cancelling")