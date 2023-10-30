while True:
    try:
        file_name = input("Enter the name of the text file you want to open: ")
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"File Content:\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please enter a valid filename.")
    except ValueError:
        print("Invalid input. Please enter a valid filename.")
    else:
        write_option = input("Do you want to write to this file (w), create a new file (n), or exit (e)? ")
        if write_option == 'w':
            new_content = input("Enter the content you want to write to the file: ")
            with open(file_name, 'a') as file:
                file.write(new_content)
                print("Content successfully added to the file.")
        elif write_option == 'n':
            new_file_name = input("Enter the name of the new file: ")
            try:
                with open(new_file_name, 'w') as new_file:
                    new_content = input("Enter the content you want to write to the new file: ")
                    new_file.write(new_content)
                    print("Content successfully written to the new file.")
            except FileNotFoundError:
                print(f"File '{new_file_name}' not found. Please enter a valid filename.")
        elif write_option == 'e':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter 'w' to write to the file, 'n' to create a new file, or 'e' to exit.")
    finally:
        print("File closed.")
