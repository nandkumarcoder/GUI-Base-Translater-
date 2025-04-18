# GUI-Based Translator

A simple GUI-based language translator built using Python and the `googletrans` library. This application allows users to translate text from one language to another using a user-friendly interface.

## Features

- Translate text between multiple languages.
- Easy-to-use graphical interface built with `tkinter`.
- Supports a wide range of languages provided by Google Translate.

## Prerequisites

- Python 3.x installed on your system.
- Required Python libraries:
  - `tkinter` (comes pre-installed with Python)
  - `googletrans`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd GUI-Base-Translater-
   ```
3. Install the required library:
   ```bash
   pip install googletrans==4.0.0-rc1
   ```

## Usage

1. Run the Python script:
   ```bash
   python translater.py
   ```
2. Enter the text you want to translate in the "You" text box.
3. Select the source language and destination language from the dropdown menus.
4. Click the "Translate" button to see the translated text in the output box.

## File Structure

- `translater.py`: The main script containing the GUI and translation logic.

## How It Works

1. The user enters text in the input box.
2. The source and destination languages are selected using dropdown menus.
3. The `googletrans` library is used to translate the text.
4. The translated text is displayed in the output box.

## Example

- Input: "Hello" (Source: English, Destination: Hindi)
- Output: "नमस्ते"


## License

This project is licensed under the MIT License.

## Acknowledgments

- [googletrans](https://pypi.org/project/googletrans/) for providing the translation functionality.
