import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='selecione uma pasta')

listaArquivos = os.listdir(caminho)
print(listaArquivos)
locais ={
    'imagens': ['.png','.jpg','.jpeg'],
    'planilhas' : ['.docx','.doc#','.pdf','.xlsx',''],
    'executaveis':['.exe','.zip','.msi'],
    'texto': ['.txt']

}

for arquivo in listaArquivos:
    nome,extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.makedirs(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}',f'{caminho}/{pasta}/{arquivo}') 