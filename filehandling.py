try:
    with open("my_file.txt", 'w') as file:
        file.write("This is the first line.\n")
        file.write("The second line has a number: 42.\n")
        file.write("Finally, the third line.\n")
    print("File created and written successfully.")

except (PermissionError, IOError) as e:
    print(f"Error occurred while creating or writing to the file: {e}")

finally:
    print("File creation block executed.")


try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nContents of 'my_file.txt':")
        print(content)

except FileNotFoundError as e:
    print(f"Error: The file was not found: {e}")
except PermissionError as e:
    print(f"Error: Permission denied: {e}")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")

finally:
    print("File reading block executed.")


try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending the fourth line.\n")
        file.write("Fifth line with some text.\n")
        file.write("And the sixth line, too.\n")
    print("Additional lines appended successfully.")

except (PermissionError, IOError) as e:
    print(f"Error occurred while appending to the file: {e}")

finally:
    print("File appending block executed.")
