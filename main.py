# print('Hello world!')
# name = (input('what is your name?'))
# age = int(input('What is your age?'))
# age_2030 = int(age) + int(5)
# print(f'Hi {name} in 2030 you will be {age_2030} years old')


# MedSchool quiz MCQs
def medtrivia():
    print('Hello there, welcome to MedTrivia')
    print('You have 5 questions and only 3 attempts')
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        correct_ans = ['B', 'B', 'C', 'B', 'B']
        answers = []
        print(f'Attempt {attempts + 1} of {max_attempts}----')

        q1 = input('Q1.Which muscle is responsible for initiating abduction of the arm at the shoulder joint? \n'
                   'A. Deltoid\n'
                   'B. Supraspinatus\n'
                   'C. Infraspinatus\n'
                   'D. Subscapularis\n'
                   'Answer: ').strip().upper()
        answers.append(q1)
        q2 = input('Q2.Which of the following does not form the Arterial Circle of Willis? \n'
                   'A.Posterior Communicating Artery\n'
                   'B.Basilar Artery\n'
                   'C.Anterior Cerebral Artery\n'
                   'D.Middle Cerebral Artery\n'
                   'Answer: ').strip().upper()
        answers.append(q2)
        q3 = input("Q3.According to Erikson’s psychosocial theory, the primary developmental task of adolescence is: \n"
                   'A.Trust vs. Mistrust\n'
                   'B.Autonomy vs. Shame\n'
                   'C.Identity vs. Role Confusion\n'
                   'D. Intimacy vs. Isolation\n'
                   'Answer: ').strip().upper()
        answers.append(q3)
        q4 = input('Q4.Which of the following enzymes is deficient in phenylketonuria (PKU)? \n'
                   'A. Tyrosinase\n'
                   'B. Phenylalanine hydroxylase\n'
                   'C. Homogentisate oxidase\n'
                   'D. Dihydrofolate reductase\n'
                   'Answer: ').strip().upper()
        answers.append(q4)
        q5 = input('Q5.What happens to the heart rate when the parasympathetic nervous system is stimulated? \n'
                   'A. It increases\n'
                   'B. It decreases\n'
                   'C. It stays the same\n'
                   'D. It first increases, then decreases\n'
                   'Answer: ').strip().upper()
        answers.append(q5)
        # score calculation
        score = 0
        for i in range(len(correct_ans)):
            if answers[i] == correct_ans[i]:
                score += 1
        print(f'You scored {score}/5')
        if score == 5:
            print('Congratulations! You got all the answers correct')
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print('Try Again')
            else:
                print("You've used all your attempts")

    print(f'The correct answers were: {correct_ans}')


medtrivia()
