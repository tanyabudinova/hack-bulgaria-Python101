from os import system


def book(*files):
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                yield line


def read_chapter(next_line, book_lines):
    while next_line[0] != '#':
        print(next_line.strip())
        next_line = next(book_lines)
    system("""bash -c 'read -s -n 1 -p "Press space to continue..."'""")
    print()
    print(next_line)
    read_chapter(next(book_lines), book_lines)


def book_reader(*files):
    book_lines = book(*files)
    print(next(book_lines))
    next_line = next(book_lines)
    try:
        read_chapter(next_line, book_lines)
    except StopIteration:
        pass
