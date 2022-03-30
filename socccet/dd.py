
from cgi import print_arguments
import numbers
import sqlite3
import random
from matplotlib.pyplot import connect

def quest(query):
    answers = []
    cursor.execute(query)
    stroka = cursor.fetchall()
    question = (stroka[0])[0]
    right_answer = (stroka[0])[-2]
    answers = list((stroka[0])[1:-2])

    return question ,answers,right_answer

for database_Title in range(1,5+1):
    connection = sqlite3.connect(database=str(database_Title))
    cursor = connection.cursor()
    cursor.execute('select count (*)  from questions')
    count = cursor.fetchall()
    count = count[0] 
    number_of_questions  = int(count[0]) - 1 
    print(f'на этом уровне уже будет {number_of_questions} вы точно готовы?')
    print('{0:*^50}'.format('yes/no'))
    exit = input()
    if exit == 'no':
        break
    query = f'select * from questions where id={random.randint(1,number_of_questions)};'
    q,ans,r_ans = quest(query)
    print('{0:*^50}'.format(q))
    print('{0:*<50}'.format('теперь вам нужно выбрать номер правильного ответа'))
    print(ans)
    b = int(input())
    if b == r_ans:
        if i == 5:
            print('ну эт самое, мои поздравления')
        else: 
            print('{0:*^50}'.format('красавчик'))
            print('{0:*^50}'.format('идем на следующий уровень'))
            #loading()
    else:
        print('{0:*^50}'.format('упсссс'))
        break


cursor.close()
connection.close()

