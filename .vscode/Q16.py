def count_lines_and_words(filename):
    try:
        with open(filename, "r") as file:
         lines=file.readlines()
         line_count=len(lines)
         word_count=sum(len(line.split()) for line in lines)

        print(f"TOTAL LINES IN {filename}: {line_count}")
        print(f"TOTAL WORDS IN {filename}: {word_count}")

    except FileNotFoundError:
       print(f"File {filename} not found")

count_lines_and_words("sample.txt")
