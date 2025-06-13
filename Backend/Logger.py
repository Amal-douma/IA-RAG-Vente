import os
from datetime import datetime

def save_question_answer_log(question, answer):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"/app/logs/log_{timestamp}.txt"

    os.makedirs("/app/logs", exist_ok=True)

    content = f"Question: {question}\nRéponse: {answer}\nTimestamp: {timestamp}\n"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return filename
