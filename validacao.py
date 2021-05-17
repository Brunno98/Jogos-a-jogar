import datetime
import banco
from cores import erro


def dataValida(date):
    try:
        datetime.datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
        return False
    else:
        return True


def inputDataConclusao(inicialDate):
    date = inputData("Quando terminou de jogar? ")
    if date and not compareDates(date, '<', inicialDate):
        return date
    if date:
        print(erro("Data que terminou o jogo não pode ser anterior à data " +
        "que começou a jogar."))


def inputData(text):
    date = input(text)
    if dataValida(date):
        return date


def compareDates(date1, operator, date2):
    if not (dataValida(date1) and dataValida(date2)):
        return None
    date1 = datetime.datetime.strptime(date1, "%d/%m/%Y")
    date2 = datetime.datetime.strptime(date2, "%d/%m/%Y")
    if operator == "=":
        return date1 == date2
    elif operator == "<":
        return date1 < date2
    elif operator == ">":
        return date1 > date2
    print(erro("Sinal inválido"))
    return None
