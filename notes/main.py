from notes import Notes

terminate_program = False
exit_count = -1
notes_folder = Notes()

while exit_count != 1:
    print("""
        Welcome to the Notes
        Please Select option from below:
          1. Create Note
          2. View Notes
""")
    try:
        choosen_option = int(input("Enter the option: "))

        match choosen_option:
            case 1:
                title = input("Enter the title of notes: ")

                data = input("Enter the data of notes: ")

                if len(data) < 5:
                    print("Enter more than 5 characters in file ")
                    data = input("")

                notes_folder.create_notes(title, data)
                
            case 2:
                notes_exists = notes_folder.get_notes()

                if not notes_exists:
                    print("file not exists")
                else:
                    notes_index = int(input("Enter the num of file: "))
                    notes_folder.view_notes(notes_index)


            case _:
                print("oops wrong selection")


        print("If you want to exit please enter 1")
        exit_count = int(input(""))
    except :
        print("something went wrong")