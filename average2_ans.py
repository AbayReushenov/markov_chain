# python3 average2_ans.py Программа расчета средней
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
#
Lmin = min(L) - 1
L1 = L
Lnew = []
i = 0
while i < len(L1):
        L1[i] == max(L1)
        Lmax = L1[i]
        Lnew += [L1[i]]
        L1[i] = Lmin
        i += 1
if len(Lnew)/2 > int (len(Lnew)/2):
        Medi = Lnew[(int(len(Lnew) / 2) + 1)]
else:
        Medi =  (Lnew[(int(len(Lnew) / 2) + 1)] +  Lnew[(int(len(Lnew) / 2) + 0)]) / 2

        
print("Вы ввели: ", L, 'или :', Lnew,
      "Сумма =", S,
      "  Наименьшее = ", min(L),
      "Наибольшее = ", max(L),
    'Среднее = ', S/Q,
      'Медиана = ', Medi)
