import re

stri = "What is the capital of France? a) Paris b) Berlin c)london What is the capital of France? a) Paris b) Berlin c)london"

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


class q_c:

    def set_question(self, question):
        self.question = question

    def set_choice(self, choice):
        self.choice = choice

    def get_question(self, question):
        return self.question

    def get_choice(self, choice):
        return self.choice


q_c_list = []

while stri != "":
    if part := re.split(r"[\.\?]\s*", stri, 1) or any(
        word in QUESTION_WORDS for word in stri
    ):
        obj_qc = q_c()
        obj_qc.set_question(part[0])
        if part := re.split(r"\[a-zA-Z]\[\.\)]", part[1], 1):
            obj_qc.set_choice(part[0])
        else:
            obj_qc.set_choice("")
    q_c_list.append(obj_qc)

    if len(part) < 0:
        stri = part[1]
    else:
        stri = ""
