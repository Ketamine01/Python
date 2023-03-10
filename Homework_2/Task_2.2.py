# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3
# Примечание.
# Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
# Кто не помнит, как решать квадратное уравнение - посмотрите в сети. Обойдите дополнительной проверкой возможность комплексных решений. Можно игнорировать то, что получаться рациональные решения вместо натуральных.

# Для вычисления квадратного корня используйте возведение в степень 0.5 или (*) Усложнение. найдите самостоятельно в сети какая функция стандартной библиотеки вычисляет квадратный корень и как до нее добраться.

import math

s = int(input('Введите сумму '))
p = int(input('Введите произведение '))

d = pow(s, 2) - 4*p

if d == 0:
    y = (s + math.sqrt(d)) // 2
    x = s - y
    print(int(x), int(y))
elif d < 0:
    print('нет решений')
else:
    y1 = (s + math.sqrt(d)) // 2
    y2 = (s - math.sqrt(d)) // 2
    x1 = s - y1
    x2 = s - y2
    if x1 < 0 or x2 < 0:
        print(int(x1), int(y1), int(x2), int(y2))
    else:
        print(int(x1), int(y1))