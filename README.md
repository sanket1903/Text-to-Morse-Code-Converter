# Text-to-Morse-Code-Converter

🔠 Morse Code Developer
A simple yet powerful desktop application built using Python and Tkinter that allows users to convert between Text and Morse Code — and vice versa. Designed and developed by Sanket Parulekar, this application also supports several extended symbols for enhanced usability.


📌 Features

🔁 Bidirectional Conversion:


    1. Text to Morse Code
    

    2. Morse Code to Text

🧠 Extended Symbol Support:


Includes mappings for symbols like @, #, %, *, etc.


🪟 User-Friendly Interface:


Built with Tkinter for an intuitive and clean GUI


❗ Error Handling:


Alerts for unsupported characters and invalid Morse inputs


🖼️ GUI Preview

The interface includes:


Radio buttons to choose conversion mode


Text input area


A "Convert" button


Output area to display results


🔤 Supported Characters

Alphabets: A–Z (case-insensitive)


Numbers: 0–9


Punctuation: . , ? ' ! / ( ) & : ; = + - _ " $ @ and more


Whitespace: space ( ) is translated to /


Custom symbols: `# % ^ * { } [ ] \ < > | ~ ``


Note: Extended/custom symbols are not part of the official Morse Code standard — they are added for UI versatility.


🚀 How to Run

🧩 Prerequisites

Python 3.x installed on your system


▶️ Run the App

Clone or download this repository.


Run the Python file

🛠️ Code Structure

MORSE_CODE_DICT: Dictionary for encoding text to Morse


REVERSE_MORSE_DICT: Reverse mapping for decoding


Functions:


text_to_morse(text)


morse_to_text(morse)


convert() - triggered on button click


GUI Elements:


Labels, Radio Buttons, Text Fields, and Button


Responsive UI with input/output areas


📎 Example Usage

Text to Morse:

Input: HELLO WORLD

Output: .... . .-.. .-.. --- / .-- --- .-. .-.. -..


Morse to Text:

Input: .... . .-.. .-.. --- / .-- --- .-. .-.. -..

Output: HELLO WORLD


👨‍💻 Developer

Sanket Parulekar

📍 Dombivli, India

🎓 Computer Engineering Student

🏆 Python Developer | AI Enthusiast | Hackathon Finalist


📜 License

This project is licensed under the MIT License.
