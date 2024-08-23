from list import List

lista = List()

while True:
    print('')
    print('='*60)
    print("1.Adicionar Exercício","2.Remover Exercício", "3.Ver Lista", "4.Ver número de Exercício", sep=' | ')
    print()
    try:
        exercise  = int(input('Oque deseja fazer?'))
        if exercise == 1:
            print('')
            lista.append_in_list()
        elif exercise == 2:
            print('')
            lista.remove_in_list()
        elif exercise == 3:
            print('')
            print("Sua lista de Exercício:",lista.see_list())
        elif exercise == 4 :
            print('')
            numero_itens_tarefas = lista.size_list()
            print(f"Sua lista possue: {numero_itens_tarefas} Exercícios")
            print('Tente Novamente!')
    except:
        print('Error')



