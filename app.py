from openai_service import get_completion_from_messages
from character_prompt_templates import character_prompt_template
from characters import characters


def get_answer(messages):
    response = get_completion_from_messages(messages, temperature=1)
    return response

def get_character_prompt(character):
    return character_prompt_template(character)

def get_characters():
    return characters
