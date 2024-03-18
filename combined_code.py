import tkinter as tk
import google.generativeai as genai
import os
import time
import sys
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown

genai.configure(api_key="AIzaSyCYJ6DI0snwMnM305p5T4RS0FpsiA9xiFk")

model = genai.GenerativeModel("gemini-pro")


def get_chatbot_response(user_message):
    messages = []
    message = user_message
    messages.append(
        {
            "role": "user",
            "parts": [message],
        }
    )

    response = model.generate_content(messages)

    messages.append(
        {
            "role": "model",
            "parts": [response.text],
        }
    )
    response.text.replace("Gemini", "incala")
    response.text.replace("Gemini", "incala")  ## add some thing
    return response.text.replace("trained by Google", "trained by incala")


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


def send_message(event=None):
    message = entry.get()
    if message == "q;":
        sys.exit(1)
    entry.delete(0, tk.END)
    chat_history.config(state=tk.NORMAL)

    chat_history.insert(tk.END, "You  : " + message + "\n", "user")
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)
    root.update_idletasks()
    message = get_chatbot_response(message)
    response = to_markdown("AI : " + message + "\n")
    # Simulate bot typing
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, response.data, "bot")
    chat_history.insert(tk.END, "__" * 40, "break")
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)


def show_previous_message(event=None):
    chat_history_list = ["no history"]
    if chat_history_list:
        previous_message = chat_history_list.pop()
        entry.delete(0, tk.END)
        entry.insert(0, previous_message)


def show_next_message(event=None):
    chat_history_list = ["end of  history"]
    if chat_history_list:
        previous_message = chat_history_list.pop()
        entry.delete(0, tk.END)
        entry.insert(0, previous_message)


root = tk.Tk()
root.title("Chat Bot")

root.configure(background="black")


chat_history = tk.Text(root, state=tk.DISABLED)
chat_history.tag_config("user", foreground="blue")
chat_history.tag_config("bot", foreground="green")
chat_history.tag_config("break", foreground="red")
chat_history.pack()

user_text = tk.Text(root, height=50, width=150)
entry = tk.Entry(root, width=200)
root.bind("<Down>", show_next_message)
root.bind("<Up>", show_previous_message)
entry.bind("<Return>", send_message)  # Bind the Enter key to send_message function
entry.pack()


# Welcome message
chat_history.config(state=tk.NORMAL)
chat_history.insert(tk.END, "AI: Hello! How can I help you today?\n", "bot")
chat_history.config(state=tk.DISABLED)
if __name__ == "__main__":
    root.mainloop()
