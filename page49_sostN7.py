print('Введите целое число, после ввода нажмите "Enter"; Чтобы закончить наберите ^Z или ^D')

total = 0
count = 0

while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
            print(err)
            continue
    except EOFError:
        break
    
if count:
        print("Количество вводов =", count, "Сумма всего =", total,"Среднее = ", total / count)
        
