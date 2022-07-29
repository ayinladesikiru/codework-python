extroversion_introversion_test = ["A. expend energy, enjoy groups. B. conserve energy, enjoy one-on-one: ",
                                  "A. more outgoing, think out loud. B. more reserved, think to yourself:",
                                  "A. seek many tasks, public activities, interaction with others. " +
                                  "B. seek private, solitary activities with quiet to concentrate,: ",
                                  "A.external, communicative, express yourself. B. internal, reticent, keep to "
                                  "yourself: ",
                                  "A. active, initiate. B. reflective, deliberate: "]

sensing_intuition_test = ["A. interpret literally. B. look for meaning and possibilities",
                          "A. practical, realistic, experiential. B. imaginative, innovative, theoretical",
                          "A. standard, usual, conventional. B. different, novel, unique",
                          "A. focus on here-and-now\" .B.look to the future, global perspective, \"big picture\"",
                          "A. facts, things, \"what is\". B. ideas, dreams, \"what could be,\" philosophical"]

thinking_feeling_test = ["A. logical, thinking, questioning. B. empathetic, feeling, accommodating",
                         "B. candid, straight forward, frank. B.tactful, kind, encouraging",
                         "A. firm, tend to criticize, hold the line. B. gentle, tend to appreciate, conciliate",
                         "A. tough-minded, just B.tender-hearted, merciful",
                         "A. matter of fact, issue-oriented B. sensitive, people-oriented, compassionate"]

judging_perceiving_test = ["A. organized, orderly. B. flexible, adaptable",
                           "A. plan, schedule B. unplanned, spontaneous",
                           "A. regulated, structured B. easygoing, \"live\" and \"let live\"",
                           "A. preparation, plan ahead. B. go with the flow, adapt as you go",
                           "A. control, govern B. latitude, freedom"]
test_result = []
extroversion_introversion = []
valid_option = ["a", "b"]
number_of_question = 1

extroversion_introversion_counter = 0
while extroversion_introversion_counter < 5:
    user_input = input(extroversion_introversion_test[extroversion_introversion_counter]).lower()
    if user_input not in valid_option:
        print("invalid input")
    else:
        extroversion_introversion.append(user_input)
        extroversion_introversion_counter += 1
        number_of_question += 1

sensing_intuition = []
sensing_intuition_counter = 0
while sensing_intuition_counter < 5:
    user_input = input(sensing_intuition_test[sensing_intuition_counter]).lower()
    if user_input not in valid_option:
        print("invalid input")
    else:
        sensing_intuition.append(user_input)
        sensing_intuition_counter += 1

thinking_feeling = []
thinking_feeling_counter = 0
while thinking_feeling_counter < 5:
    user_input = input(thinking_feeling_test[thinking_feeling_counter]).lower()
    if user_input not in valid_option:
        print("invalid input")
    else:
        thinking_feeling.append(user_input)
        thinking_feeling_counter += 1

judging_perceiving = []
judging_perceiving_counter = 0
while judging_perceiving_counter < 5:
    user_input = input(judging_perceiving_test[judging_perceiving_counter]).lower()
    if user_input not in valid_option:
        print("invalid input")
    else:
        judging_perceiving.append(user_input)
        judging_perceiving_counter += 1


def personality_check(lst, x, y):
    count_a = 0
    count_b = 0
    for i in lst:
        if i == "a":
            count_a += 1
        else:
            count_b += 1
    if count_a > count_b:
        answer = x
    else:
        answer = y
    return test_result.append(answer)


personality_check(extroversion_introversion, "E", "I")
personality_check(sensing_intuition, "S", "N")
personality_check(thinking_feeling, "T", "F")
personality_check(judging_perceiving, "J", "P")
print(test_result)
