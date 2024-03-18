import subprocess
import dis


def compile_cpp_to_asm(input_file, output_file):
    command = f"g++ -S test1.cpp -o cpp_code.s"

    try:
        subprocess.run(command, check=True)
        print(f"Successfully generated assembly code: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating assembly code: {e}")


# Usage
input_file = "test1.cpp"  # Path to your C++ source file
output_file = "output.asm"  # Path to the output assembly code file
compile_cpp_to_asm(input_file, output_file)


def convert_to_asm():
    input_file = "C:\\Users\\Caleb\\Desktop\\pcomier\\test.py"
    output_file = "python_code.asm"
    command = f"py2asm {input_file} -o {output_file}"

    try:
        subprocess.run(command, check=True)
        print(f"Successfully generated assembly code: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating assembly code: {e}")


# Call the function
convert_to_asm()


subprocess.run("cat python_code.asm cpp_code.s > combined_code.asm", shell=True)
subprocess.run("nasm -f elf64 combined_code.asm -o combined_code.o", shell=True)
subprocess.run("g++ combined_code.o -o executable_file", shell=True)
result = subprocess.run("./executable_file", capture_output=True, text=True, shell=True)
if result.returncode == 0:
    print("Compilation successful!")
else:
    print("Compilation failed. Error message:")
    print(result.stderr)
