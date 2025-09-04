import jsonlines
import random

# diff_dict = {'Easy': None, "Medium": None, 'Hard': None}
# with jsonlines.open('leetcode-solutions.jsonl') as reader:
#     easy = []
#     med = []
#     hard = []
#     for obj in reader:
#         print(obj['id'])
        
        
#         if(obj['difficulty'] == 'Easy'):
#             easy.append(obj)
#         elif(obj['difficulty'] == 'Medium'):
#             med.append(obj)
#         elif(obj['difficulty'] == 'Hard'):
#             hard.append(obj)
            
#         diff_dict['Easy'] = easy
#         diff_dict['Medium'] = med
#         diff_dict['Hard'] = hard
        
print("hello")  
leet_list = []
curr_idx = None
curr_obj = None
# difficulty - Random, Easy, Medium, Hard
def reset(difficulty):
    
    with jsonlines.open('leetcode-solutions.jsonl') as reader:
        if(difficulty == 'Random'):
            for line in reader:
                leet_list.append(line)
        else:
            for line in reader:
                if(line['difficulty'] == difficulty):
                    leet_list.append(line)
                    
    # print(leet_list)
    random.shuffle(leet_list)
    curr_idx = 0
    curr_obj = leet_list[0]
    
    print(curr_obj['slug'], curr_obj['difficulty'])
    # print(curr_obj)
    
reset("Medium")

leet_answer = []

def return_answer(lang):
    languageStr = str(lang)    
    with jsonlines.open('leetcode-solutions.jsonl') as reader:
        for line in reader:
            answerReturn = line
            leet_answer.append(answerReturn["answer"][languageStr])

    return leet_answer 

print(return_answer('c++'))

        
