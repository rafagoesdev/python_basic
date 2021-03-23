import shutil

def escrever(nome,texto):
    arquivo = open(nome, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualiza(nome,texto):
    arquivo = open(nome, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler(nome):
    arquivo = open(nome, "r")
    texto = arquivo.read()
    print(texto)

def media_notas(nome):
    arquivo = open(nome,"r")
    aluno = arquivo.read()
    print(aluno)
    aluno = aluno.split('\n')
    # print(aluno)
    lista_media = []

    for x in aluno:
        lista = x.split(',')
        aluno = lista[0]
        lista.pop(0)
        print(aluno)
        print(lista)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista))
        lista_media.append({aluno:media(lista)})
    return lista_media

def copia_arq(nome):
    shutil.copy(nome,'C:/Users/x/PycharmProjects/pythonProject/copia/notas_alunos.txt')

def move_arq(nome):
    shutil.move(nome, 'C:/Users/x/PycharmProjects/pythonProject/copia/notas_alunos1.txt')

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)
    move_arq("notas.txt")
    # escrever('notas,txt','Primeira linha. \n')
    # atualiza('notas,txt','Segunda linha.\n')
    # aluno = 'Rafael,10,10,5,5'
    # escrever("notas.txt",aluno)
    # atualiza('notas.txt','\nJJonas,4,7,6,8')
    # atualiza('notas.txt','\nNezes,6,8,9,8')
    # ler('notas.txt')