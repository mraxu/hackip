import sys

def split_file(file_path, output_prefix, chunk_size=131072):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    for i in range(0, total_lines, chunk_size):
        chunk_lines = lines[i:i+chunk_size]
        output_file = f"{output_prefix}_{i // chunk_size}.txt"
        with open(output_file, 'w') as file:
            file.writelines(chunk_lines)
        print(f"Created: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: split_file.py <file_path> <output_prefix>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    output_prefix = sys.argv[2]
    split_file(file_path, output_prefix)
