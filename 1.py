def read_candidate_answers():
    outfile=open('answers.txt','r')
    answer_list=outfile.read().split()
    return answer_list

def correct_answers():
    correct_list= ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B', 'B','D','A']
    return correct_list

def result(answer_list,correct_list):
    count=0
    wrong_answers=[]
    for i in range(20):
        if answer_list[i]==correct_list[i]:
            count+=1
        else:
            count+=0
            wrong_answers.append(i)
    if count<15:
        print("Failed")
    else:
        print("Passed")
    print("Number of Correct answers: ", count)
    print("Number of Incorrect answers: ",20-count)
    print("Incorrect answers list is: ", wrong_answers)

answers=read_candidate_answers()
correct=correct_answers()
output=result(answers,correct)