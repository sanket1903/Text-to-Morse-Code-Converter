import tkinter as tk
from tkinter import messagebox

# Morse code dictionary with letters, digits, symbols, and extended mappings
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/',

    # Extended symbols (custom mappings)
    '#': '........', '%': '.......-', '^': '......-.',
    '*': '.....-..', '{': '....--..', '}': '...---..',
    '[': '..--...', ']': '..---..', '\\': '.--..--',
    '<': '.-..-..', '>': '...-.-.', '|': '.-.-.-.',
    '~': '..--.-.', '`': '...--.-'
}

# Reverse dictionary for decoding
REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    try:
        return ' '.join(MORSE_CODE_DICT[char.upper()] for char in text)
    except KeyError as e:
        return f"Error: Unsupported character '{e.args[0]}'"

def morse_to_text(morse):
    try:
        return ''.join(REVERSE_MORSE_DICT[code] for code in morse.split())
    except KeyError:
        return "Error: Invalid Morse Code symbol"

def convert():
    mode = var.get()
    input_text = input_field.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Required", "Please enter some text.")
        return

    if mode == 1:
        output = text_to_morse(input_text)
    else:
        output = morse_to_text(input_text)

    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, output)

# GUI Setup
root = tk.Tk()
root.title("Morse Code Developer by Sanket Parulekar")
root.geometry("650x520")
root.resizable(False, False)

# Heading
tk.Label(root, text="Morse Code Developer", font=("Arial", 18, "bold"), fg="Brown").pack(pady=10)
tk.Label(root, text="by Sanket Parulekar", font=("Arial", 12, "italic")).pack()

# Conversion Mode
var = tk.IntVar(value=1)
tk.Label(root, text="\nSelect Conversion Mode:", font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Text to Morse", variable=var, value=1, font=("Arial", 11)).pack(anchor='w', padx=30)
tk.Radiobutton(root, text="Morse to Text", variable=var, value=2, font=("Arial", 11)).pack(anchor='w', padx=30)

# Input Field
tk.Label(root, text="\nInput", font=("Arial", 11)).pack()
input_field = tk.Text(root, height=6, width=75)
input_field.pack(pady=5)

# Convert Button
tk.Button(root, text="Convert", command=convert, bg="lightgreen", font=("Arial", 12, "bold")).pack(pady=10)

# Output Field
tk.Label(root, text="Output", font=("Arial", 11)).pack()
output_field = tk.Text(root, height=6, width=75)
output_field.pack(pady=5)

# Footer
tk.Label(root, text="\nNote: Symbols like #, %, *, etc. are mapped for UI only, not official Morse.", fg="gray", font=("Arial", 9)).pack()

root.mainloop()
