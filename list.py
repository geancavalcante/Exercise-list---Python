
class List():
    def __init__(self):
        self.lista = []


    def append_in_list(self):
        exercise  = str(input('Digite a matéria e a Página:'))
        self.lista.append(exercise)
        print('')
        print(f"'{exercise}', adiconada com sucesso!")


    def remove_in_list(self):
            exercise_remove = input('Qual tarefa quer remover?')
            try:
                self.lista.remove(exercise_remove)
                print(f"'{exercise_remove}', Exercício removido com suscesso!")
            except:
                print('')
                print(f"Não possue o item '{exercise_remove}' na lista")
                
    def see_list(self):
        return self.lista
    
    def size_list(self):
        return len(self.lista)
    

