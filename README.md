---
title: Character-Style Chatbot
emoji: ⚡
colorFrom: yellow
colorTo: indigo
sdk: docker
pinned: false
license: mit
---

# Character-Style Chatbot

## Description

This project is an interactive chatbot that responds using the speaking styles of various iconic characters or famous authors. From Shakespeare to Yoda, you can engage in conversations with the chatbot as it imitates the language and style of these characters.

The chatbot is built using Python, the OpenAI API for generating responses, and Gradio for creating a user-friendly interface. Additionally, it allows you to select a specific list of characters to limit the options based on your preferences.

## Features

- **Multiple characters**: The chatbot mimics the speaking styles of characters like William Shakespeare, Yoda, Eckhart Tolle, Homer Simpson, and more.
- **Character selection**: You can choose from a personalized list of characters to limit the available options.
- **Interactive interface**: Uses Gradio for a simple and engaging user experience.
- **Dynamic responses**: The chatbot generates creative replies using OpenAI language models.
- **Easy customization**: Add new characters or adjust the list with minimal effort.

## Requirements

- **Python 3.7+**
- **OpenAI API Key** – You’ll need an OpenAI API key to generate the chatbot’s responses.
- **Gradio** – To create the chatbot’s interactive interface.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/character-style-chatbot.git
   cd character-style-chatbot
   ```

2. Create a virtual environment and install the dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure your OpenAI API key:

   Create a `.env` file in the project root with the following content:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```bash
   python app.py
   ```

## Usage

After running the application, a Gradio interface will open where you can interact with the chatbot. You can select from a predefined list of characters to determine the style of the responses. Then, start chatting, and the chatbot will reply in the chosen character’s style.

### Character Selection

In the interface, you’ll have an option to select which characters are available. You can limit the list based on your preferences, such as only allowing historical figures, science fiction characters, or philosophical authors.

## Customization

To add more characters or modify the list, edit the `characters.py` file, where you can define each character’s unique style and manage their availability in the list.

Example for adding a new character:

```python
characters = [
    "William Shakespeare",
    "Eckhart Tolle",
    "Yoda (Star Wars)",
    "Homer Simpson (The Simpsons)",
    "Holden Caulfield (The Catcher in the Rye) ",
    "Tyler Durden (Fight Club)",
    "Virginia Woolf",
    "Dr. Gregory House (House M.D.)",
    "Tyrion Lannister (Game of Thrones)",
    "Gandalf (The Lord of the Rings)",
    # Add more characters here
]
```

If you want to adjust the list of available characters, edit the `config.py` file to include only the characters you want in the list.

## Technologies

- **Python**
- **OpenAI API** – For generating the chatbot’s responses.
- **Gradio** – For the interactive interface.

## Contributions

Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
