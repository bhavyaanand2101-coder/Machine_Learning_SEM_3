from QUES import Ques

questions = [
    "What is your name? \n (a) Bhavya \n (b) Riya \n (c) Ananya \n (d) Priya",

    "What is your favorite color? \n (a) Red \n (b) Blue \n (c) Green \n (d) Yellow",

    "Which is the capital of India? \n (a) Mumbai \n (b) Delhi \n (c) Kolkata \n (d) Chennai",

    "Which language is used for web development? \n (a) HTML \n (b) Python \n (c) JavaScript \n (d) All of these",

    "Which planet is known as the Red Planet? \n (a) Earth \n (b) Mars \n (c) Jupiter \n (d) Venus",

    "How many days are there in a week? \n (a) 5 \n (b) 6 \n (c) 7 \n (d) 8",

    "Which is the largest ocean in the world? \n (a) Atlantic Ocean \n (b) Indian Ocean \n (c) Pacific Ocean \n (d) Arctic Ocean",

    "What is 10 + 20? \n (a) 20 \n (b) 30 \n (c) 40 \n (d) 50",

    "Which animal is known as the King of the Jungle? \n (a) Tiger \n (b) Lion \n (c) Elephant \n (d) Leopard",

    "Which gas do humans need to breathe? \n (a) Carbon dioxide \n (b) Oxygen \n (c) Nitrogen \n (d) Hydrogen",

    "Who is known as the Father of the Nation in India? \n (a) Jawaharlal Nehru \n (b) Mahatma Gandhi \n (c) Sardar Patel \n (d) Subhash Chandra Bose",

    "Which is the smallest prime number? \n (a) 0 \n (b) 1 \n (c) 2 \n (d) 3",

    "Which device is used to type text on a computer? \n (a) Mouse \n (b) Keyboard \n (c) Monitor \n (d) Printer",

    "Which programming language is known for its simple syntax? \n (a) Python \n (b) Assembly \n (c) Machine Code \n (d) COBOL",

    "How many continents are there in the world? \n (a) 5 \n (b) 6 \n (c) 7 \n (d) 8",

    "Which is the largest planet in our solar system? \n (a) Earth \n (b) Saturn \n (c) Jupiter \n (d) Neptune",

    "What is the boiling point of water at sea level? \n (a) 50°C \n (b) 75°C \n (c) 100°C \n (d) 150°C",

    "Which of the following is a database? \n (a) MySQL \n (b) HTML \n (c) CSS \n (d) JavaScript",

    "Which keyword is used to define a function in Python? \n (a) function \n (b) def \n (c) func \n (d) define",

    "Which data type is used to store True or False in Python? \n (a) int \n (b) string \n (c) bool \n (d) float"
]

# for i in questions:
#     print(i)

ans=[Ques(questions[0],'a'),Ques(questions[1],'b'),Ques(questions[2],'b'),Ques(questions[3],'d'),Ques(questions[4],'b'),Ques(questions[5],'c'),Ques(questions[6],'c'),Ques(questions[7],'b'),Ques(questions[8],'b'),Ques(questions[9],'b'),Ques(questions[10],'b'),Ques(questions[11],'c'),Ques(questions[12],'b'),Ques(questions[13],'a'),Ques(questions[14],'c'),Ques(questions[15],'c'),Ques(questions[16],'c'),Ques(questions[17],'a'),Ques(questions[18],'b'),Ques(questions[19],'c')]

def runquiz(questions):
    score = 0
    for i in questions:
        print(i.q)
        ans = input("Enter your answer: ")
        if ans.lower() == i.a:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    print(f"Your final score is: {score}/{len(questions)}")


if __name__ == "__main__":
    runquiz(ans)