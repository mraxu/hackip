def split_file(input_file_path, output_prefix, lines_per_file=131072):
    with open(input_file_path, 'r') as file:
        file_count = 1
        while True:
            chunk = file.readlines(lines_per_file)
            if not chunk:
                break
            with open(f"{output_prefix}_{file_count}.txt", 'w') as outfile:
                outfile.writelines(chunk)
            file_count += 1

if __name__ == "__main__":
    import sys
    input_file_path = sys.argv[1]
    output_prefix = sys.argv[2]

    split_file(input_file_path, output_prefix)
