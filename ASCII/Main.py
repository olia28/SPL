import shutil
from Chars import ascii_table

def generate_ascii_art(text, width, height, align, color):
    ascii_art_lines = []

    for char in text.upper():
        if char in ascii_table:
            ascii_art_lines.append(ascii_table[char])
        else:
            ascii_art_lines.append([' ' * 5] * 5) 

    ascii_art = [' '.join(row) for row in zip(*ascii_art_lines)]

    if align == 'center':
        ascii_art = [line.center(width) for line in ascii_art]
    elif align == 'right':
        ascii_art = [line.rjust(width) for line in ascii_art]
 
    if len(ascii_art) > height:
        ascii_art = ascii_art[:height]

    ascii_art_colored = apply_color('\n'.join(ascii_art), color)
    return ascii_art_colored

def apply_color(ascii_art, color):
    colors = {
        "white": "\033[97m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m"
    }
    reset = "\033[0m"
    return f"{colors.get(color, colors['white'])}{ascii_art}{reset}"

def save_to_file(ascii_art, filename):
    with open(filename, 'w') as file:
        file.write(ascii_art)

def main():
    print("Welcome to ASCII Art Generator!")

    text = input("Enter the text you want to convert into ASCII art: ")

    alignments = ['left', 'center', 'right']
    align = input(f"Choose alignment ({', '.join(alignments)}): ").lower()
    if align not in alignments:
        align = 'left'

    colors = ["white", "red", "green", "yellow", "blue", "magenta", "cyan"]
    color = input(f"Choose a color ({', '.join(colors)}): ").lower()
    if color not in colors:
        color = "white"

    terminal_width = shutil.get_terminal_size().columns
    terminal_height = shutil.get_terminal_size().lines

    width = input(f"Enter width (or press Enter for default {terminal_width}): ")
    if not width.isdigit():
        width = terminal_width
    else:
        width = int(width)

    height = input(f"Enter height (or press Enter for default {terminal_height}): ")
    if not height.isdigit():
        height = terminal_height
    else:
        height = int(height)

    ascii_art = generate_ascii_art(text, width, height, align, color)
    print("\nYour ASCII Art:\n")
    print(ascii_art)

    save_option = input("\nDo you want to save the ASCII art to a file? (yes/no): ").lower()
    if save_option == 'yes':
        filename = input("Enter the filename: ") + ".txt"
        save_to_file(ascii_art, filename)
        print(f"ASCII art saved to {filename}!")

if __name__ == "__main__":
    main()