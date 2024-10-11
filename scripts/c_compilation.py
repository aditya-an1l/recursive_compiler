import os
import subprocess


# Function to compile all .c files in the current directory
def compile_c_files(directory):
    # List all files in the given directory
    for filename in os.listdir(directory):
        # Check if the file ends with .c extension
        if filename.endswith(".c"):
            # Get the base filename (without extension)
            base_filename = os.path.splitext(filename)[0]
            # Construct the gcc command
            command = f"gcc -o {base_filename} {filename}"
            print(f"Compiling {filename} into {base_filename}...")

            # Execute the gcc command
            result = subprocess.run(command, shell=True)

            # Check if the compilation was successful
            if result.returncode == 0:
                print(f"Successfully compiled {filename}")
            else:
                print(f"Error compiling {filename}")


# Specify the directory to search for .c files
directory = "."  # You can change this to any path you want

# Compile the C files
compile_c_files(directory)
