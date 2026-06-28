print('************ Welcome To Quiz Game***************')
questions=['What Is BanaNa 🍌 color',
           'What Is Apple 🍎 Color',
           'What is Guva 🍈 Color',
           'What Is Grape 🍇 color']
options=[['a).🟡Yellow','b).🟢Greeen','c).🟠Orange','d).🔴red'],
        ['a).🔴Red','b).🟢Greeen','c).🟠Orange','d).🟡Yellow'],
        ['a).🟢Greeen','b).🔴Red','c).🟠Orange','d).🟡Yellow'],
        ['a).🌑dark blue','b).🔴Red','c).🟠Orange','d).🟡Yellow']]
answer=['a','a','a','a']
score=0
want_to_continue= ' '
while  want_to_continue!='n':
 for i in range(len(questions)):
    print(questions[i])
    for j in range(len(options)):
            print(options[i][j])
    guess=input("Enter Your Answer:")
    if (guess==answer[i]):
          print("correct")
          score+=1
    else:
           print(f'wrong answer answer is {answer[i]}')
 print(f'correct Answers ={score} score is {score}')
 want_to_continue=input('want to continue (y/n):')
 if want_to_continue=='y':
      print('hurray you are in level 2')
      questions_1=['What Is Car 🚗',
           'What Is Horse 🐎',
           'What is water glass 🥛',
           'What is burger 🍔']
      options_1=[['a).🗞️ Vehicle','b).🗞️ Object','c).🗞️ Animal','d).🗞️ Food'],
        ['a).🗞️ Animal','b).🗞️ Object','c).🗞️ Vehicle','d).🗞️ Food'],
        ['a).🗞️ Object','b).🗞️ Animal','c).🗞️ Vehicle','d).🗞️ Food'],
        ['a).🗞️ Food','b).🗞️ Animal','c).🗞️ Vehicle','d).🗞️ Object']]
      answer_1=['a','a','a','a']
 for i in range(len(questions_1)):
    print(questions_1[i])
    for j in range(len(options_1)):
            print(options_1[i][j])
    guess=input("Enter Your Answer:")
    if (guess==answer_1[i]):
          print("correct")
          score+=1
    else:
           print(f'wrong answer answer is {answer_1[i]}')
 break
print("Thanks  For Playing Quiz ")
print(f'correct Answers ={score} score is {score}')
print("********************************************************8")