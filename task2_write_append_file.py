# Step 1: Write user input to a file
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write)
print("Data Successfully written to output.txt.")

# Step 2: Append additional text to the file
text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(" " + text_to_append)  # add a space before appending
print("Data successfully appended.")

# Step 3: Read and display final content
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    final_content = file.read()
    print(final_content)
