def read_and_modify_file():
    """
    Reads a file, modifies its contents, and writes the modified content to a new file.
    Handles errors if the file doesn't exist or can't be read.
    """
    try:
        # Prompt the user for the filename to read
        input_filename = input("Enter the name of the file to read: ")

        # Attempt to open and read the file
        with open(input_filename, 'r') as file:
            content = file.readlines()

        # Modify the content: Example, add line numbers
        modified_content = [
            f"Line {i + 1}: {line.strip()}\n" for i, line in enumerate(content)
        ]

        # Write the modified content to a new file
        output_filename = f"modified_{input_filename}"
        with open(output_filename, 'w') as file:
            file.writelines(modified_content)

        print(f"File processed successfully! Modified content saved to '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You do not have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
read_and_modify_file()
