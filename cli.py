# command line parser

import charsets

def parse_args(args):
    # Usage: asciimager <image>
    if len(args) != 1:
        print("Usage: asciimager <image>")
        exit(1)
    
    return {
        "image": args[0],
        "charset": charsets.charset_default, # default
        "chunk_size": (10, 20) # default
    }
