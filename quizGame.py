questions = (
    "What is the capital of France?",
    "Who is known as the father of computers?",
    "Which planet is known as the Red Planet?",
    "What is the largest ocean on Earth?",
    "Who wrote the play 'Romeo and Juliet'?",
    "Which element has the chemical symbol 'O'?",
    "What is the speed of light in vacuum?",
    "Which country invented pizza?",
    "What is the currency of Japan?",
    "Who painted the Mona Lisa?",
    "What is the square root of 64?",
)

options = (
    "A. Rome, B. Paris, C. London",
    "A. Charles Babbage, B. Alan Turing, C. John von Neumann",
    "A. Venus, B. Mars, C. Jupiter",
    "A. Atlantic, B. Indian, C. Pacific",
    "A. William Wordsworth, B. William Shakespeare, C. John Milton",
    "A. Hydrogen, B. Oxygen, C. Nitrogen",
    "A. 300,000 km/s, B. 150,000 km/s, C. 500,000 km/s",
    "A. China, B. Italy, C. France",
    "A. Dollar, B. Yen, C. Euro",
    "A. Vincent van Gogh, B. Leonardo da Vinci, C. Pablo Picasso",
    "A. 6, B. 8, C. 10",
)

answers = ("B", "A", "B", "C", "B", "B", "A", "B", "B", "B", "B")


for i in range(len(questions)):
    print(f"--Question No. {i+1}--")
    print(questions[i])
    print(options[i])
    answer = input("Enter the answer: (Q to Quit)").upper()
    if answer == answers[i]:
        print("Correct answer!")
    elif answer == "Q":
        break
    else:
        print("Invalid answer!")
        print(f"The correct answer is: {answers[i]}")
print()