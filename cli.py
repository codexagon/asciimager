import os

# Available charsets
SETS = {
    "default": "@%#*+=-:. ",
    "long": "@#$%&WM8B0QOZ?+=|i!;:,.'` ",
    "block": "█▓▒░ ",
    "dots": "⣿⠿⠟⠏⠇⠃⠁⠀",
    "minimal": "@#:. ",
}

valid_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

# Parse command-line arguments
def parse_args(args):
    if len(args) < 1:
        print("Usage: asciimager [options] <image>...")
        exit(1)
    
    images = []

    # Defaults
    charset = SETS["default"]
    chunk_size = (10, 20)
    write_to_file = False
    output_file = None
    save_mode = "append"

    i = 0
    while i < len(args):
        arg = args[i]

        # Parse flags
        if arg.startswith("--"):
            flag = arg[2:] # extract the base flag text

            # Set charset to be used
            if flag == "charset":
                if (i + 1) >= len(args) or args[i + 1].startswith("--"):
                    print("Please provide a charset choice.")
                    exit(2)
                
                charset_choice = args[i + 1]

                if charset_choice in SETS:
                    charset = SETS[charset_choice]
                else:
                    print(f"Invalid charset choice {charset_choice}.")
                    print("Valid options are: long, block, dots, minimal")
                    exit(3)
                
                i += 2 # skip flag and value
            
            # Set chunk size to be used
            elif flag == "chunk-size":
                if (i + 2) >= len(args):
                    print("Please provide the chunk size.")
                    exit(4)
                
                if args[i + 1].startswith("--") or args[i + 2].startswith("--"):
                    print("Please provide two integers for the chunk size.")
                    exit(4)

                try:
                    width, height = int(args[i + 1]), int(args[i + 2])
                    if width <= 0 or height <= 0:
                        print("Chunk size must be positive integers.")
                        exit(4)
                    
                    chunk_size = (width, height)
                except ValueError:
                    print(f"Invalid chunk size: ({args[i + 1]} {args[i + 2]}). Please provide integers.")
                    exit(4)
                
                i += 3 # skip flag and both values
            
            # Whether the output should be saved to a file
            elif flag == "save":
                if i + 1 >= len(args):
                    print("Please provide a file name to save to.")
                    exit(5)

                if not args[i + 1].endswith((".txt", ".md")):
                    print("Invalid file type. Can only write to text and markdown files.")
                    exit(5)
                
                write_to_file = True
                output_file = args[i + 1]

                i += 2 # skip flag and value

            # Whether to append to the file or overwrite it
            elif flag == "save-mode":
                if i + 1 >= len(args):
                    print("Please provide a mode for saving.")
                    exit(10)

                if args[i + 1] not in ["append", "write"]:
                    print(f"Invalid save mode: {args[i + 1]}.")
                    print("Valid modes are: append, write")
                    exit(10)

                if not write_to_file:
                    print("Cannot use this flag without or before the --save flag.")
                    print("Make sure to enter this flag after the --save flag.")
                    exit(10)

                save_mode = args[i + 1]

                i += 2 # skip flag and value

            elif flag == "help":
                show_help()
                exit(0)

            else:
                print(f"Invalid flag: {flag}. Please enter a valid flag.")
                exit(6)
        
        # Check if given image files have a valid extension
        elif any(arg.lower().endswith(extension) for extension in valid_extensions):
            images.append(arg)
            i += 1
        
        else:
            print(f"Invalid argument: {arg}. Please enter valid arguments only.")
            exit(7)

    # Check if at least one image is provided
    if not images:
        print("Please provide at least one image to render.")
        exit(8)

    # Check if provided image files exist
    for img in images:
        if not os.path.exists(img):
            print(f"Error: file '{img}' not found")
            exit(9)

    return {
        "images": images,
        "charset": charset,
        "chunk_size": chunk_size,
        "write_to_file": write_to_file,
        "output_file": output_file,
        "save_mode": save_mode,
    }

def show_help():
    print(
        """
asciimager - convert images to ASCII art from the terminal

Usage: asciimager [options] <image>...

Arguments:
    <image>...                          One or more images to convert to ASCII art

Options:
    --charset <charset>                 The character set to be used to make the ASCII art
    --chunk-size <width> <height>       Set the size of each chunk which is represented by one character
    --save <file>                       Save the generated ASCII art to a file instead of printing to stdout
    --save-mode <mode>                  Choose the file save mode (append or write)
    --help                              Brings up this text

Note: There is no need to specify any files when using the --help flag.
        """
    )
