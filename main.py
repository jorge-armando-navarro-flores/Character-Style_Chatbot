import gradio as gr
from app import get_answer, get_character_prompt, get_characters


with gr.Blocks() as demo:
    character_dropdown = gr.Dropdown(label="Character Selection", value="William Shakespeare", choices=get_characters())
    chatbot = gr.Chatbot(get_character_prompt("William Shakespeare"), type="messages")

    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        chat_history.append({"role": "user", "content": message})
        response = get_answer(chat_history)
        chat_history.append({"role": "assistant", "content": response})
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    character_dropdown.input(get_character_prompt, inputs=[character_dropdown], outputs=[chatbot])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
