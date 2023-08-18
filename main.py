#importando módulos
import sys
import argparse
import os

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
    os.mkdir(f"{final_dir}01")