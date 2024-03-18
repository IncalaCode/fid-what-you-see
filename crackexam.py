import pyperclip
import time
from PIL import Image

from PIL import ImageGrab
import clipboard
import re
import google.generativeai as genai

import re

genai.configure(api_key="AIzaSyCYJ6DI0snwMnM305p5T4RS0FpsiA9xiFk")

model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat()

question_word_list = [
    "what",
    "where",
    "when",
    "how",
    "why",
    "did",
    "do",
    "does",
    "have",
    "has",
    "am",
    "is",
    "are",
    "can",
    "could",
    "may",
    "would",
    "will",
    "should" "didn't",
    "doesn't",
    "haven't",
    "isn't",
    "aren't",
    "can't",
    "couldn't",
    "wouldn't",
    "won't",
    "shouldn't",
    "?",
]


def clean(input_string):

    string = re.sub(r"\s{3,}", " ", input_string)
    string = string.replace("\n", " ")
    string = string.replace("\r", " ")
    return string


def find_str(string, index):
    store = ""
    for _ in range(len(text)):
        if _ == index:
            return store
        else:
            store += text[_]


def is_question(text):
    text = clean(text)

    questions = []
    choices = []
    while text != "":
        if re.search(r"[\.\?] (.*) \s*", text):
            index = re.split(r"[\.\?](.*)\s*", text)

            if re.search(r"[a-zA-Z]\)\s*", text):
                index = text.find(r"[a-zA-Z]\)\s*")
                choices = text.split(find_str(text, index))
        if text == "":
            if question:
                return True, questions, choices
            else:
                return False, None, None


def cp_str(data):
    value = is_question(data)
    if value[0]:
        pyperclip.copy("")
        stor_response, stor_response_error = print(api(value[1], value[2]))


def is_image(data):
    print(data)
    data.save("img", "png")


def api(question, choices):
    print(question, choices)
    stor_response_error = []
    stor_response = []
    for _ in range(len(question)):
        try:
            message = (
                "context = {answer:'',expanlination:''},question:'"
                + question[_]
                + "',choices:'"
                + choices[_]
                + "'getAnswer:true and getExplaination:true in form of context"
            )

            response = chat.send_message(message)
            stor_response = print(response.text)
        except Exception as e:
            stor_response_error = print(f"something went wrong : {e}")
    return stor_response, stor_response_error


def main():
    ti = time.time()
    duration = 3 * 60 * 60
    counter = 0

    while time.time() - ti < duration:

        if isinstance(pyperclip.paste(), str) and len(pyperclip.paste()) > 0:
            cp_str(pyperclip.paste())
        elif ImageGrab.grabclipboard() != None:
            is_image(ImageGrab.grabclipboard())
        elif (
            isinstance(pyperclip.paste(), str)
            and len(pyperclip.paste()) > 0
            and ImageGrab.grabclipboard() != None
        ):
            print("both are there............")
        print("wating ... ", counter)
        counter += 1
        time.sleep(1)


main()
