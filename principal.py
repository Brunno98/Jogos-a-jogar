import banco
import validacao
import datetime
from cores import cor, erro, aviso


def menu():
    while True:
        print(cor("\n\tMenu Principal", "azul"))
        print("[1] Adicionar novo jogo.")
        print("[2] Detalhes do jogo.")
        print("[3] Alterar jogo.")
        print("[4] Excluir jogo.")
        print("[5] Listar jogos.")
        print("[0] Sair.")
        escolha = input("O que deseja fazer? ")
        
        if escolha == '0':
            break
        
        elif escolha == '1':
            dados = solicitarDados()
            if dados:
                banco.inserirJogo(*dados)
            else:
                print(erro("Inserção de novo jogo cancelada."))

        elif escolha == '2':
            jogo_id = input("Informe o id do jogo desejado: ")
            if banco.idExiste(jogo_id):
                apresentarJogo(banco.lerJogo(jogo_id))
            else:
                print(erro("Não há registros com esse id."))

        elif escolha == '3':
            jogo_id = input("Informe o id do jogo desejado: ")
            if banco.idExiste(jogo_id):
                dados = solicitarDados()
                if dados:
                    banco.atualizarJogo(jogo_id, *dados)
                else:
                    print(erro("Alteração de dados cancelada."))
            else:
                print(erro("Não há registros com esse id."))

        elif escolha == '4':
            jogo_id = input("Informe o id do jogo desejado: ")
            if banco.idExiste(jogo_id):
                if confirmarExclusao():
                    banco.excluirJogo(jogo_id)
                else:
                    print(aviso("Exclusão cancelada"))
            else:
                print(erro("Não há registros com esse id."))

        elif escolha == '5':
            menu_listar()

        else:
            print(erro("Escolha inválida! tente novamente ou insira 0 para sair."))


def menu_listar():
    print(cor("\n\tOpções de listagem:", "magenta"))
    print("[1] Todos os jogos.")
    print("[2] Ordem de data de início.")
    print("[3] Ordem alfabética.")
    print("[4] Apenas jogos finalizados.")
    print("[5] Apenas jogos não finalizados.")
    print("[0] Sair.")
    escolha = input("O que deseja fazer? ")

    if escolha == '0':
        return
    elif escolha == '1':
        listarJogos(banco.listarJogos())
    elif escolha == '2':
        listarJogos(banco.listarJogos("data"))
    elif escolha == '3':
        listarJogos(banco.listarJogos("nome"))
    elif escolha == '4':
        listarJogos(banco.listarJogos("finalizado"))
    elif escolha == '5':
        listarJogos(banco.listarJogos("jogando"))
    else:
        print(erro("opção inválida."))


def listarJogos(jogos):
    print()
    print(f"{'id':>4} | {'Nome':^30} | {'Data Iniciado':13} | {'Data Finalizado':15} | {'Finalizado?'}")
    print()
    for conteudo in jogos:
        id = conteudo[0]
        nome = conteudo[1]
        dataInicio = formatarDataParaUsuario(conteudo[2])
        dataConclusao = formatarDataParaUsuario(conteudo[3])
        finalizado = "sim" if conteudo[4] == 1 else "não"
        print(f"{id:>4} | {nome:<30} | {dataInicio:^13} | {dataConclusao:^15} | {finalizado}")


def solicitarDados():
    nome = input("Qual o nome do jogo? ").strip()
    if not nome:
        print(erro("Nome inválido."))
        return None

    dataInicio = validacao.inputData("Quando começou a jogar? ")
    if not dataInicio:
        print(erro("Data de início inválida."))
        return None

    if jogoFinalizado():
        dataConclusao = validacao.inputDataConclusao(dataInicio)
        if not dataConclusao:
            print(erro("Data de conclusão inválida."))
            return None
        dataConclusao = formataDataParaBanco(dataConclusao)
        finalizado = '1'
    else:
        dataConclusao = None
        finalizado = '0'

    return (
        nome,
        formataDataParaBanco(dataInicio),
        dataConclusao,
        finalizado
    )


def jogoFinalizado():
    while True:
        fim = input("Já terminou o jogo? ").strip().lower()
        if fim in ["s", "sim"]:
            return True
        elif fim in ["n", "nao", "não"]:
            return False
        print(erro("Resposta inválida. responda apenas sim ou não."))


def apresentarJogo(conteudo):
    finalizado = conteudo[3]
    print()
    print("Nome: ", conteudo[0])
    print("Data iniciado: ", conteudo[1])
    if finalizado:
        print("Data Finalizado: ", conteudo[2])
    print()


def confirmarExclusao():
    resposta = input("Digite 'sim' para confirmar a exclusão: ")
    return resposta == "sim"


def formataDataParaBanco(data):
    dia, mes, ano = data.split('/')
    return datetime.date(int(ano), int(mes), int(dia))


def formatarDataParaUsuario(data):
    if not data:
        return ''
    ano, mes, dia = data.split('-')
    return '/'.join((dia, mes, ano))


if __name__ == "__main__":
    menu()