

def create_outline():
    print("Course Topics:")
    topics = set(["* Introduction to Python","* Tools of the Trade","* How to make decisions","* How to repeat code","* How to structure data","* Functions","* Modules"]) 
    #b = ["* How to repeat code","* How to structure data","* Functions","* Modules"]
    #topics = a + b
    topics = list(set(topics))
    topic = topics.sort()
    #for i in topics:
        #print(words)
    i = 0
    while i != len(topics):
        print(topics[i])
        i += 1
    topic_dict = {}
    problems = ["Problem 1", "Problem 2", "Problem 3"]
    print("Problems: ")


    #for i in topics:
        #topic_dict[i] = problems
    topic_dict = topic_dict.fromkeys(topics,problems)#mapping done here
    #print(topic_dict.keys())
    topic_dict = topic_dict.items()
    #topic_dict.sort()

    for i in topic_dict:
        #print(i)
        topic_name, problem_ = i
        problem1, problem2, problem3 = problem_
    
        print("{} : {}, {}, {}".format(i[0], i[1][0], i[1][1], i[1][2]))

#step 3:
    print("Student Progress:")
    student_name = ["Nyari","Madam","Priss"]
    student_name = list(set(student_name))
    status = ["GRADED","COMPLETED", "STARTED"]
    status.sort(reverse = True)
    student = dict.fromkeys(student_name,topic_name)
    #print(student)

    i = 0
    #x = random.randint(0,2)
    
    student_progress_1 = ("1. {} -{} - {} [{}]".format(student_name[0], topic_name.strip("*"), problem_[0], status[0]))
    student_progress_2 = ("2. {} -{} - {} [{}]".format(student_name[1], topic_name.strip("*"), problem_[1], status[1]))
    student_progress_3 = ("3. {} -{} - {} [{}]".format(student_name[2], topic_name.strip("*"), problem_[2], status[2]))

        
    for i in student_name:
        if i == student_name[0]:
            print(student_progress_1)
        elif i == student_name[1]:
            print(student_progress_2)
        elif i == student_name[2]:
            print(student_progress_3)

        



    

    
    
if __name__ == "__main__":
    create_outline()

