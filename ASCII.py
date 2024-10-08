import pyfiglet
from termcolor import colored
import shutil
import textwrap

def get_available_fonts():
    return [
        "doom", 
        "isometric2", 
        "3-d", "3d-ascii", 
        "3d_diagonal", 
        "banner3-D", 
        "starwars", 
        "slant", 
        "5lineoblique", 
        "block"
    ]

def generate_ascii_art(text, font, color, width, height, align):
    try:
        figlet = pyfiglet.Figlet(font=font, width=width)
        ascii_art = figlet.renderText(text)
        
        if align == 'center':
            ascii_art_custom = '\n'.join(textwrap.fill(line, width=width, subsequent_indent='', initial_indent=' '*((width-len(line))//2)) for line in ascii_art.splitlines())
        elif align == 'right':
            ascii_art_custom = '\n'.join(textwrap.fill(line, width=width, subsequent_indent='', initial_indent=' '*(width-len(line))) for line in ascii_art.splitlines())
        else:
            ascii_art_custom = ascii_art

        lines = ascii_art_custom.splitlines()
        if len(lines) > height:
            ascii_art_custom = '\n'.join(lines[:height])
        
        return colored(ascii_art_custom, color)
    except Exception as e:
        print(f"Error rendering with font '{font}': {e}")
        return None

def save_to_file(ascii_art, filename):
    with open(filename, 'w') as file:
        file.write(ascii_art)

def main():
    print("Welcome to ASCII Art Generator!")

    text = input("Enter the text (you can include symbols) you want to convert into ASCII art: ")
    
    fonts = get_available_fonts()
    print("\nAvailable fonts:")
    for i, font in enumerate(fonts[:10], 1):
        print(f"{i}. {font}")
    
    while True:
        try:
            font_choice = int(input(f"Choose a font (1-{min(10, len(fonts))}): "))
            font = fonts[font_choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please select a valid font number.")

    colors = ["white", "orange", "red", "blue", "yellow", "magenta", "cyan"]
    print("\nAvailable colors: " + ", ".join(colors))
    color = input(f"Choose a color ({', '.join(colors)}): ").lower()
    if color not in colors:
        print(f"Invalid color, defaulting to white.")
        color = "white"

    alignments = ['left', 'center', 'right']
    print("\nText placement options: left, center, right")
    align = input(f"Choose alignment ({', '.join(alignments)}): ").lower()
    if align not in alignments:
        print(f"Invalid alignment, defaulting to left.")
        align = 'left'

    terminal_width = shutil.get_terminal_size().columns
    print(f"\nDefault terminal width is {terminal_width}.")
    width = input(f"Enter custom width or press Enter to use terminal width ({terminal_width}): ")
    if width.isdigit():
        width = int(width)
    else:
        width = terminal_width

    terminal_height = shutil.get_terminal_size().lines
    print(f"\nDefault terminal height is {terminal_height}.")
    height = input(f"Enter custom height or press Enter to use terminal height ({terminal_height}): ")
    if height.isdigit():
        height = int(height)
    else:
        height = terminal_height

    print("\nPreview of your ASCII art:")
    ascii_art_preview = generate_ascii_art(text, font, color, width, height, align)
    if ascii_art_preview:
        print(ascii_art_preview)

        save_option = input("\nDo you want to save this ASCII art to a file? (yes/no): ").lower()
        if save_option == 'yes':
            filename = input("Enter the filename (without extension): ") + ".txt"
            save_to_file(ascii_art_preview, filename)
            print(f"ASCII art saved to {filename}!")
        else:
            print("ASCII art not saved.")
    else:
        print("Failed to generate ASCII art. Please try again.")

if __name__ == "__main__":
    main()
