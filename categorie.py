import test
# uk
uk_list = ['Привіт', 'До побачення', 'Як справи', 'Погода', 'Дім', 'Місто', 'Телефон', 'Кнопка', 'Число', 'Рядок'] # 10
uk_answer = ['Привет', 'Досвидания', 'Как дела', 'Погода', 'Дом', 'Город', 'Телефон', 'Кнопка', 'Число', 'Строка'] # 10
# math
math_list = ['1 + 1', '1 + 2', '1 + 3', '1 + 4', '1 + 5', '5 * 5', '2 * 0', '10000 * 0', '500 * 1', '10 / 2'] # 10
math_answer = [2, 3, 4, 5, 6, 25, 0, 0, 500, 5] # 10
# en
en_list = ['Hello', 'Goodbye', 'My name is', 'I am from', 'City', 'Telephon', 'Tablet', 'Laptop', 'Amount', 'Negative'] # 10
en_answer = ['Привет', 'Досвидания', 'Мое имя', 'Я из', 'Город', 'Телефон', 'Планшет', 'Ноутбук', 'Сумма', 'Отрицательное'] # 10

bals = 0

for question in test.uk_test:
    print(uk_list[test.uk_test.index(question)])
    answer = input(question + ':  ')
    if answer.capitalize() in uk_answer:
        bals += test.bal
        print('Поздравляем вы получили', test.bal, 'бал')
    print('Количество ваших баллов', bals)

for question in test.math_test:
    print(math_list[test.math_test.index(question)])
    answer = input(question + ':  ')
    if int(answer) in math_answer:
        bals += test.bal
        print('Поздравляем вы получили', test.bal, 'бал')
    print('Количество ваших баллов', bals)


for question in test.eng_test:
    print(en_list[test.eng_test.index(question)])
    answer = input(question + ':  ')
    if answer.capitalize() in en_answer:
        bals += test.bal
        print('Поздравляем вы получили', test.bal, 'бал')
    print('Количество ваших баллов', bals)

file = open('user.txt', 'w', encoding='utf-8')
file.write('Баллов  ' + str(30))
file.close()

print(bals)