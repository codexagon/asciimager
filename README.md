# asciimager

Convert images to ASCII art from the command line.

## Features

- Convert any image (JPEG, PNG, GIF, BMP) to ASCII art
- Multiple character sets for a different look
- Customizable chunk sizes for detail control
- Colored output to better recreate the original image
- Process multiple images in a single command
- Save output to text or markdown files

## Installation

1. Clone the repository:
```bash
git clone https://github.com/codexagon/asciimager.git
cd asciimager
```

2. Install dependencies:
```bash
pip install pillow
```

## Usage

### Basic Usage
```bash
python main.py <image>
```

### Syntax
```
asciimager [options] <image>...
```

### Options

- `--charset <charset>` - Character set to use for conversion
- `--chunk-size <width> <height>` - Size of pixel chunks (default: 10 20)
- `--save <file>` - Save ASCII art to file instead of printing to console
- `--save-mode <mode>` - File save mode: append or write (default: write)
- `--color` - Render the ASCII art in color

### Examples

**Convert a single image:**
```bash
python main.py photo.jpg
```

**Convert multiple images:**
```bash
python main.py photo1.jpg photo2.png landscape.gif
```

**Use a different character set:**
```bash
python main.py --charset block photo.jpg
```

**Customize chunk size for more detail:**
```bash
python main.py --chunk-size 8 16 photo.jpg
```

**Use colored output**
```bash
python main.py --color photo.jpg
```

**Save to file:**
```bash
python main.py --save output.txt photo.jpg
python main.py --save ascii_art.md --save-mode append photo.jpg
```

**All at once:**
```bash
python main.py --charset long --chunk-size 8 16 --color --save artwork.txt photo1.jpg photo2.png
```

## Character Sets

| Name | Characters |
|------|------------|
| `default` | `@%#*+=-:. ` |
| `long` | ``@#$%&WM8B0QOZ?+=\|i!;:,.'` `` |
| `block` | `█▓▒░ ` |
| `dots` | `⣿⠿⠟⠏⠇⠃⠁⠀` |
| `minimal` | `@#:. ` |

## Supported Formats

**Input:** JPEG, PNG, GIF, BMP  
**Output:** Plain text (.txt), Markdown (.md)

## Requirements

- Python 3.6+
- Pillow (PIL)