# Prompt user for the names of two files
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

# Open input file and read contents
with open(input_file, 'r') as f:
    data = f.read()

# Write contents to output file
with open(output_file, 'w') as f:
    f.write(data)

print("Contents of", input_file, "have been copied to", output_file)