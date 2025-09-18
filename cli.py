# command line parser

# Charset choices
SETS = {
    "default": "@%#*+=-:. ",
    "long": "@#$%&WM8B0QOZ?+=|i!;:,.'` ",
    "block": "█▓▒░ ",
    "dots": "⣿⠿⠟⠏⠇⠃⠁⠀",
    "minimal": "@#:. ",
}

def parse_args(args):
    # Usage: asciimager <image>
    if len(args) < 1:
        print("Usage: asciimager <image>")
        exit(1)
    
    charset = SETS["default"] # default
    chunk_size = (10, 20) # default
    write_to_file = False # default
    output_file = None
    
    for i in range(len(args)):
        arg = args[i]
        if arg.startswith("--"):
            flag = arg[2:]

            if flag == "charset":
                if (i + 1) >= len(args) or args[i + 1].startswith("--"):
                    print("Please provide a charset choice.")
                    exit(2)
                
                charset_choice = args[i + 1]

                if charset_choice in SETS:
                    charset = SETS[charset_choice]
                else:
                    print("Invalid charset choice.")
                    exit(3)

            elif flag == "chunk-size":
                if (i + 2) >= len(args):
                    print("Please provide the chunk size.")
                    exit(4)

                chunk_size_choice = (int(args[i + 1]), int(args[i + 2]))
                chunk_size = chunk_size_choice

            elif flag == "save":
                if (i + 1) >= len(args):
                    print("Please provide a file name to save to.")
                    exit(6)
                
                write_to_file = True
                output_file = args[i + 1]

            else:
                print(f"Invalid flag: {flag}. Please enter a valid flag.")
                exit(5)



    return {
        "image": args[0],
        "charset": charset,
        "chunk_size": chunk_size,
        "write_to_file": write_to_file,
        "output_file": output_file,
    }
