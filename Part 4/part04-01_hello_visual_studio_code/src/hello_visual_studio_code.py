while True:
    editor = input("Editor: ")
    if editor.lower() == "Visual Studio Code".lower():
        print("an excellent choice!")
        break
    elif editor.lower() == "Word".lower():
        print("awful")
    else:
        print("not good")