# First, we need to ask the user which file they want to work with.
input_filename = input("Enter the name of the file to read (e.g., original.txt): ")

# Let's create a new name for our modified file automatically.
output_filename = "modified_" + input_filename

# Now for the main part. We'll use a 'try...except' block.
# This is like saying, "Try to do this, but if something goes wrong, don't panic and crash."
try:
    # We open the original file to read from ('r').
    with open(input_filename, 'r') as original_file:
        # At the same time, we open (or create) the new file to write to ('w').
        with open(output_filename, 'w') as modified_file:
            
            print(f"\nSuccess! Reading from '{input_filename}'...")
            
            # We'll go through the original file, line by line.
            for line in original_file:
                # Here's our modification. Let's just make every line uppercase. Simple and effective.
                modified_line = line.upper()
                
                # Now, write that changed line into our new file.
                modified_file.write(modified_line)

    print(f"All done! A modified version has been saved as '{output_filename}'.")

# This 'except' part only runs if the 'try' block failed because the file wasn't found.
except FileNotFoundError:
    print(f"\nError: Sorry, the file '{input_filename}' was not found. Please check the name and try again.")

# This is a general safety net for any other kind of error, like not having permission to read the file.
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
