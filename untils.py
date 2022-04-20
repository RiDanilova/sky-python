import json
from pprint import pprint as pp

def load_questions():
    with open ("questions.json","r", encoding="utf-8") as file:
        questions = json.load(file)
    return questions

def count_questions(questions):

    counter = 0

    for cat_questions in questions.values():
       counter += len(cat_questions)
    return counter



def show_field(questions):
    top_level_cats = questions.keys()

    for top_cat in top_level_cats:
        print(top_cat.ljust(17), end= "")
        cat_questions = questions[top_cat]
        for question_price, question_data in cat_questions.items():
            if question_data['asked']:
                print(" " * 3, end= "   ")
            else:
                print(question_price, end= "   ")
        print()

def parse_input(user_input, questions):

    user_input_parsed = user_input.split(" ")

    if len(user_input_parsed) != 2:
        return False

    cat = user_input_parsed[0].title()
    price = user_input_parsed[1]

    if cat not in questions:
        return False

    category_from_questions = questions[cat]

    if price not in category_from_questions:
        return False

    questions_data = category_from_questions[price]

    if questions_data["asked"]:
        return False

    question_text = questions_data["question"]
    question_answer = questions_data["answer"]

    return {"cat": cat, "price": price, "question": question_text, "answer": question_answer}

def show_question(question_text):
    print(f"Слово {question_text} в переводе означает ....")


def show_stats(stats):
    print(f"У нас закончились вопросы!")
    print(f" ")
    print(f"Ваш счет:         {stats.get('points')}")
    print(f"Верных ответов:   {stats.get('correct')}")
    print(f"Неверных ответов: {stats.get('incorrect')}")

def save_result_to_file(stats):
    filename = "record.json"
    with open(filename, 'w') as file:
        json.dump(stats, file)

stats = {"points": 1, "correct": 2, "incorrect": 3}
save_result_to_file(stats)


questions = load_questions()
pp(count_questions(questions))