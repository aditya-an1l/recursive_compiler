import os
import subprocess


def compile_c_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".c"):
            base_filename = os.path.splitext(filename)[0]
            command = f"gcc -o {base_filename} {filename}"
            print(f"Compiling {filename} into {base_filename}...")

            result = subprocess.run(command, shell=True)

            if result.returncode == 0:
                print(f"Successfully compiled {filename}")
            else:
                print(f"Error compiling {filename}")


directory = "."
if __name__ == "__main__":
    compile_c_files(directory)
