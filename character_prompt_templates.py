def character_prompt_template(character):
    return {
            "role": "system",
            "content": f"You are an assistant that speaks like {character}.",
        },


