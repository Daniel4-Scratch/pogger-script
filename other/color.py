import os
import sys

# ANSI color codes
RAINBOW_COLORS = [
    '\033[91m',  # Red
    '\033[93m',  # Yellow
    '\033[92m',  # Green
    '\033[96m',  # Cyan
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
]
RESET = '\033[0m'

def colorize_and_export_ascii(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return

    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        color_index = 0
        with open(output_file, 'w') as output:
            for line in lines:
                colored_line = ''
                for char in line:
                    if char.strip():  # Skip spaces
                        colored_line += RAINBOW_COLORS[color_index] + char
                        color_index = (color_index + 1) % len(RAINBOW_COLORS)
                    else:
                        colored_line += char
                output.write(colored_line + RESET)

        print(f"Colorized ASCII art exported to {output_file}")

    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_ascii_file> <output_file>")
    else:
        colorize_and_export_ascii(sys.argv[1], sys.argv[2])
