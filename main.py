import uuid

#Função para gerar id.
#Optei usar o UUID selecionando apenas os cinco primeiros caracteres.
def id_generator():
    return str(uuid.uuid4())[0:5]

#Função para cadastrar novo estudante
def register_student():
    student['Id'] = id_generator()
    student['Name'] = input('Nome: ')
    student['Email'] = input('Email: ')
    student['Telefone'] = input('Telefone: ')
    student['Curso'] = input('Curso: ')
    students.append(student.copy())

#Função para mostrar estudantes cadastrados
def show_subs():
        print('-' * 26 + '-' * 25)
        print('-' * 20 + ' Inscritos ' + '-' * 20)
        print('-' * 26 + '-' * 25)
        for e in students:
            for i, j in e.items():
                print('{}: {}'.format(i, j))
            print('-' * 51)

#Programa Principal
#Area apresentando menu
print('-' * 51)
print('-'*23 + ' Menu ' + '-'*22)
print('-' * 51)
print(' 1 - Nova inscrição')
print(' 2 - Visualizar inscrição')
print(' 0 - Encerrar')
print('-' * 51)

#Declarando dicionário e lista como vazio
student = {}
students = []

#Estrutura de repetição para programa selecionar opção escolhida pelo usuário
while True:
    res = int(input('Escolha uma opção: '))
    if res == 1:
        register_student()
        continue
    elif res == 2:
        if not students:
            print('Nenhuma inscrição cadastrada!')
        else:
            show_subs()
        continue
    elif res == 0:
        print('Encerrando programa...')
        break
    else:
        print('Opção inválida. Tente outra vez!')
        continue
