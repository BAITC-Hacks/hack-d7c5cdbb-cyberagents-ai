def classify_message(message):
    text = message.lower()

    # Справка
    if (
        "справк" in text
        or "как получить" in text
        or "где парковка" in text
        or "где парковк" in text
    ):
        return (
            "справка",
            "Вот информация по вашему вопросу. "
            "Мы поможем предоставить необходимые сведения."
        )

    # Жалоба
    if (
        "очередь" in text
        or "холодная" in text
        or "пропал" in text
        or "не работает" in text
    ):
        return (
            "жалоба",
            "Спасибо за обращение. "
            "Мы передадим информацию ответственным сотрудникам."
        )

    # Другое
    return (
        "другое",
        "Ваш запрос принят. Мы поможем с вашим обращением."
    )


def main():
    with open("messages.txt", "r", encoding="utf-8") as file:
        messages = [line.strip() for line in file if line.strip()]

    for number, message in enumerate(messages, start=1):
        category, answer = classify_message(message)

        print(f"{number}. Сообщение: {message}")
        print(f"   Категория: {category}")
        print(f"   Ответ: {answer}")
        print()


if __name__ == "__main__":
    main()