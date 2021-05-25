import Laboratory as lb

def main():
    
    print('\nВыберите номер нужного вам алгоритма:\n',
    '1 - Алгоритм Конечный автомат\n',
    '2 - Алгоритм Боера-Мура\n',
    '3 - Алгоритм Кнута-Мориса-Прата\n',
    '4 - Алгоритм Рабина-Карпа\n',    
    '5 - Выход')
    nomer = int(input())
    sub = lb.Laboratory()

    if nomer == 1:
        print(sub.getSuffixTable_Automat('abbcaba'))
        main()
    
    elif nomer == 2:
        text = 'aaabaaabababaaabaababaaaabab'
        substring = 'aba'
        print(sub.boera_mura(text, substring))
        main()

    elif nomer == 3:
        text = 'aaabaaabababaaabaababaaaabab'
        substring = 'aba'
        print(sub.kmp(text, substring))
        main()

    elif nomer == 4:
        text = 'aaabaaabababaaabaababaaaabab'
        substring = 'aba'
        print(sub.rabin_karp(text,substring))
        main()
        
    elif nomer == 5:
        pass

    else:
        main()

if __name__ == "__main__":
    main()