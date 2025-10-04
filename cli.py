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
        show_error("invalid usage.\nUsage: asciimager [options] <image>...", 1)
    
    images = []

    # Defaults
    charset = SETS["default"]
    chunk_size = (10, 20)
    write_to_file = False
    output_file = None
    save_mode = "append"
    use_color = False
    inverse = False
    preview = False

    i = 0
    while i < len(args):
        arg = args[i]

        # Parse flags
        if arg.startswith("--"):
            flag = arg[2:] # extract the base flag text

            # Set charset to be used
            if flag == "charset":
                if (i + 1) >= len(args) or args[i + 1].startswith("--"):
                    show_error("no charset provided. Please provide a charset to use.", 2)
                
                charset_choice = args[i + 1]

                if charset_choice in SETS:
                    charset = SETS[charset_choice]
                else:
                    show_error(f"invalid charset '{charset_choice}'.\nValid options are: long, block, dots, minimal", 2)
                
                i += 2 # skip flag and value
            
            # Set chunk size to be used
            elif flag == "chunk-size":
                if (i + 2) >= len(args):
                    show_error("no chunk size provided. Please provide it.", 3)
                
                if args[i + 1].startswith("--") or args[i + 2].startswith("--"):
                    show_error("please provide two positive integers for the chunk size.", 3)

                try:
                    width, height = int(args[i + 1]), int(args[i + 2])
                    if width <= 0 or height <= 0:
                        show_error("chunk size must be positive integers.", 3)
                    
                    chunk_size = (width, height)
                except ValueError:
                    show_error(f"invalid chunk size ({args[i + 1]} {args[i + 2]}). Please provide integers.", 3)
                
                i += 3 # skip flag and both values
            
            # Whether the output should be saved to a file
            elif flag == "save":
                if i + 1 >= len(args):
                    show_error("no file provided. Please provide a file to save to.", 4)

                if not args[i + 1].endswith((".txt", ".md")):
                    show_error("invalid file type. Can only write to text and markdown files.", 4)
                
                write_to_file = True
                output_file = args[i + 1]

                i += 2 # skip flag and value

            # Whether to append to the file or overwrite it
            elif flag == "save-mode":
                if i + 1 >= len(args):
                    show_error("no save mode provided. Please provide a mode.", 5)

                if args[i + 1] not in ["append", "write"]:
                    show_error(f"invalid save mode '{args[i + 1]}'.\nValid modes are: append, write", 5)

                if not write_to_file:
                    show_error("cannot use this flag without or before the --save flag.\n" \
                    "Make sure to enter --save-mode flag after the --save flag.", 5)

                save_mode = args[i + 1]

                i += 2 # skip flag and value

            elif flag == "help":
                show_help()
                exit(0)

            elif flag == "color":
                use_color = True

                i += 1 # skip flag

            elif flag == "inverse":
                inverse = True

                i += 1 # skip flag

            elif flag == "preview":
                preview = True
                
                i += 1 # skip flag

            else:
                show_error(f"invalid flag '{flag}'. Please enter a valid flag.", 6)
        
        # Check if given image files have a valid extension
        elif any(arg.lower().endswith(extension) for extension in valid_extensions):
            images.append(arg)
            i += 1
        
        else:
            show_error(f"invalid argument {arg}. Please enter valid arguments only.", 7)

    # Check if at least one image is provided
    if not images:
        show_error("no images provided. Please provide at least one image.", 8)

    # Check if provided image files exist
    for img in images:
        if not os.path.exists(img):
            show_error(f"file '{img}' not found.", 9)

    return {
        "images": images,
        "charset": charset,
        "chunk_size": chunk_size,
        "write_to_file": write_to_file,
        "output_file": output_file,
        "save_mode": save_mode,
        "use_color": use_color,
        "inverse": inverse,
        "preview": preview,
    }

def show_error(message, exit_code=1):
    print(f"Error: {message}")
    exit(exit_code)

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
    --color                             Renders the ASCII art with color
    --help                              Brings up this text

Note: There is no need to specify any files when using the --help flag.
        """
    )
