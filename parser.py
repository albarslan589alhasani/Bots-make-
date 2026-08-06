def parse_questions(text):
    questions = []

    blocks = text.strip().split("\n\n")

    for block in blocks:
        lines = block.splitlines()

        if len(lines) < 3:
            continue

        question = lines[0]

        options = []
        correct = None

        for i, line in enumerate(lines[1:], start=1):
            line = line.strip()

            if line.startswith("✓"):
                options.append(line.replace("✓", "").strip())
                correct = i - 1
            else:
                options.append(line)

        if correct is not None:
            questions.append({
                "question": question,
                "options": options,
                "correct": correct
            })

    return questions
