def citynameto_list(input_file):
    #city_checklist = ['seattle','denver','washington','georgia','dallas']
    for line in input_file:
        changed_line = line.split(',')
        for word in changed_line:
            word.strip('\n')
            print(word)
            # if '\n' in word:
            #      for i in word:
            #         if(i == '\n'):
            #             i = ""
            #      print(word)
        #for word in changed_line:
        seattle, denver, washington, georgia, dallas = ([] for i in range(5))
        print(seattle)
        print(dallas)
        #print(city_checklist)
            #if word not in city_checklist:
        #print(changed_line)





# main function
input_file = open("F:\\python_scripts\\network programming\\city_assignment.txt",'r')
citynameto_list(input_file)