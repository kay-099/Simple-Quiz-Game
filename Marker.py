import AnswerandQuestion

# the below variables are used to keep track of question and answers
score = 0
totalQestionList = len(AnswerandQuestion.Questionlist)

def Marker(index):
    answers = AnswerandQuestion.Answerlist[index]
    print("Answer:")
    userinput = input()
    
    # return the score if correct.
    if userinput.lower() == answers.lower():
        return 1
    else :
        return 0
    

# iterates over the question and calls the marker function for the answers
for i in AnswerandQuestion.Questionlist:
    print(i)
    score += Marker(score)

print(f"\n{score} out of {totalQestionList} is your mark")
