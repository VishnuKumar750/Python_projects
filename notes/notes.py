import os

class Notes:
    folder_path = "./notes"
    notes = []

    def __init__(self):
        # create a folder if not exists
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path, exist_ok=True)
        else:
            for filename in os.listdir(self.folder_path):
                if os.path.isfile(os.path.join(self.folder_path, filename)):
                    self.notes.append(filename)


    def get_file_name(self, index):
        return self.notes[index - 1]
        
    def get_notes_len(self):
        return len(self.notes)
    
    # create_notes
    def create_notes(self, title, data):
        try: 
            file_name = title
            f = open(f"{self.folder_path}/{file_name}.txt", "a")
            f.write(data)
            f.close()

            
            print(f"{file_name} is created...")

            self.notes.clear()

            for filename in os.listdir(self.folder_path):
                if os.path.isfile(os.path.join(self.folder_path, filename)):
                    self.notes.append(filename)

        except :
            print("something went wrong!")

    # get list of notes
    def get_notes(self):
        try:
            if self.get_notes_len() < 1:
                return False
            else:
                for i in range(0, len(self.notes)):
                    print((i + 1),  " -> ",  self.notes[i])  
                return True
        except Exception as e:
            print(f"get notes: {e}")
        


    # view notes 
    def view_notes(self, index):
        try:
            print("""choose from given option:
                  1. view file 
                  2. add text 
                  3. update the file
                  4. delete the file
                  """)
            choice = int(input(""))

            if choice > 0 and choice < 5:
                if choice == 1:
                    self.read_file(index)
                elif choice == 2:
                    input_data = input("")
                    self.add_text(index, input_data)
                elif choice == 3:
                    input_data = input("")
                    self.update_note(index, input_data)
                elif choice == 4:
                    self.delete_note(index)
                else:
                    pass
            else:
                print("wrong selection! ")

        except:
            print("file not exists.")

    # read_file
    def read_file(self, index):
        try:
            file_name = self.get_file_name(index)
            file_path = os.path.join(self.folder_path,file_name)
            f = open(file_path, "r")

            print(file_name)
            print(f.read())
            print("\n")

            f.close()
        except Exception as e:
            print(f"Error while reading file: {e}")

    # add text
    def add_text(self, index, data):
        try:
            file_name = self.get_file_name(index)
            file_path = os.path.join(self.folder_path, file_name)

            f = open(file_path, "a")
            f.write(data)
            f.close()

            print("Text added")

        except Exception as e:
            print(f"Error appending data: {e}")
       
    # delete notes
    def delete_note(self, index):
        file_name = self.get_file_name(index)
        file_path = os.path.join(self.folder_path, file_name)

        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print("File deleted...")
                self.notes.clear()

                for filename in os.listdir(self.folder_path):
                    if os.path.isfile(os.path.join(self.folder_path, filename)):
                        self.notes.append(filename)

            except Exception as e:
                print(f"Error deleting file: {e}")
        else:
            print("The file does not exist")

    # update note
    def update_note(self, index, data):
        try:
            file_path = os.path.join(self.folder_path, self.get_file_name(index))

            f = open(file_path, "w")
            f.write(data)
            f.close()

        except Exception as e:
            print(f"Error updating file: {e}")
        