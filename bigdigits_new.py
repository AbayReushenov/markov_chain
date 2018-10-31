import sys

zero = ['    ***    ',
        '   *   *   ',
        '  *     *  ',
        '  *     *  ',
        '  *     *  ',
        '   *   *   ',
        '    ***    ']
one  = ['     *     ','    **     ','   * *     ','  *  *     ','     *     ','     *     ','     *     ']
two  = ['    ***    ',
        '   *   *   ',
        '       *   ',
        '      *    ',
        '     *     ',
        '    *      ',
        '   *****   ']
three =[' ********* ',
        '*         *',
        '          *',
        '   ******* ',
        '          *',
        '*         *',
        ' ********* ']
four = ['     *  *  ',
        '    *   *  ',
        '   *    *  ',
        '  *     *  ',
        ' ********  ',
        '        *  ',
        '        *  ']
five = ['***********',
        '*          ',
        '********** ',
        '          *',
        '          *',
        '          *',
        '********** ']
six   =['********** ',
        '*          ',
        '*          ',
        '***********',
        '*         *',
        '*         *',
        '***********']
seven= ['*********  ',
        '*       *  ',
        '        *  ',
        '        *  ',
        '        *  ',
        '        *  ',
        '        *  ']
eight= [' ********* ',
        '*         *',
        '*         *',
        ' ********* ',
        '*         *',
        '*         *',
        ' ********* ']
nine  =[' **********',
        '*         *',
        '*         *',
        ' **********',
        '          *',
        '          *',
        '***********']

Digits = [zero,one,two,three,four,five,six,seven,eight, nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ''
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            
            Column = 0
            lineI= ''
            AAA = digit[row]
            while Column < len(AAA):
                if AAA[Column] != '*':
                    lineI += " "
                else:
                    lineI += str(number)
                Column += 1
                               
            line += lineI + "   "
            column += 1
        print(line)
        row += 1
except IndexError:
    print('используйте команду в следующем формате : ', sys.argv[0], "<Число>")
except ValueError as err:
    print(err, 'в ' , digits)
    
        
    
