#importando módulos
import sys
import argparse
import os
import virtualenv

#recebendo comando do cmd
command = sys.argv[1:]
#criando parser
parser = argparse.ArgumentParser(add_help=False,prog="CLI-Python",
                                description="Interface de linha de comando que permite a automatização de criação de projetos.")



#definindo argumentos 
parser.add_argument("-t","--title",dest="title", type=str, help="Título da Pasta em que será criado o programa.", required=True)
parser.add_argument("-output",dest="output",type=str,help="Onde o projeto será salvo, por padrão é colocado no Disco C", default="C:/")
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Mostra essa mensagem e sai do programa.')


#acessando argumentos
args = parser.parse_args()

# criando função para corrigir o caminho se necessário
def corrigir_path(input_path):
    output_path = input_path.replace('\\\\', '//')
    return output_path

#definindo caminho final da pasta
final_dir = os.path.join(args.output, args.title)
print("Projeto criado no endereço: ",final_dir)

#verificando se a pasta já existe antes de criá-la
if not os.path.exists(final_dir):
    os.mkdir(final_dir)
else:
    print("Pasta já existente no caminho especificado.")


# criando arquivo template
def criar_arquivo(nome_arquivo, conteudo):
    os.chdir(final_dir)
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(conteudo)

conteudo = """
Olá! Tenho 21 anos e sou um aspirante a programador apaixonado por tecnologia.
Estudo na UFMA, onde mergulho no mundo da programação.
Minhas habilidades incluem Python, HTML, CSS e estou começando com JavaScript.
Adoro transformar ideias em soluções digitais criativas.
Fico feliz que um de meus códigos foi útil para você!

Atenciosamente,
Ziz
contato: zizcoder@gmail.com


"""

criar_arquivo('hello.txt',conteudo)