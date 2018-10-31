# python3 average1_ans.py Программа расчета средней
S = 0
Q = 0
L = []
while True:
    n = input(" Введите число или нажмите Enter: ")
    if n:
        try:
            N = int(n)
        except ValueError as err:
            print (err, "Только  целые числа!")
            continue
        S += N
        Q += 1
        L += [N]
    else:
        break
if L:
    print("Вы ввели: ", L, "Сумма =", S, "  Наименьшее = ",min(L[:]), "Наибольшее = ", max(L[:]),
          'Среднее = ', S/Q)
    
    
    
