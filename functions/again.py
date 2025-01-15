from .calculate import calculate
from .display_history import display_history


def again(history):
    """
    Function used to provide options to the user to exit, enter a new operation with or without the previous result.
    :return: ∅
    """
    print("\nDo you want to calculate again?\nChoose your option:\n1: Start a new calculation\n"
          "2: Start a new calculation using the previous result\n3: Show the history and exit\n")

    user_choice = input("Enter your choice: ")

    match user_choice:
        case "1":
            history.append(calculate())
            again(history)

        case "2":
            result = history[-1][3]
            print(f"result: {result}\n")
            print(history)
            if history[-1][3] != "None":
                history.append(calculate(result))
                print(history)
            again(history)

        case "3":
            display_history(history)
            print("\nSee you later.")

        case _:
            print("Wrong input!\nToo BAD!!")
            again(history)
