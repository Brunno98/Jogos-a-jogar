import sqlite3
import cores
from datetime import date


conn = sqlite3.connect("jogos.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS jogo(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    dataInicio TEXT NOT NULL,
    dataConclusao TEXT NULL,
    finalizado INTEGER NULL)"""
)


def inserirJogo(nome, dataInicio, dataConclusao, finalizado):
    try:
        cursor.execute("""
        INSERT INTO jogo(nome, dataInicio, dataConclusao, finalizado)
        VALUES (?, ?, ?, ?)""", (nome, dataInicio, dataConclusao, finalizado)
        )
        conn.commit()
    except sqlite3.Error as erro:
        print(cores.erro("Erro ao inserir informações do jogo. erro: "), erro)
    else:
        print(cores.sucesso("Informações do jogo inserida com sucesso."))


def lerJogo(jogo_id):
    try:
        dados = cursor.execute("""
        SELECT nome, dataInicio, dataConclusao, finalizado
        FROM jogo WHERE id = ?""", (jogo_id, ))
    except sqlite3.Error as erro:
        print(cores.erro("Erro ao ler registro do jogo. Erro: "), erro)
    else:
        return dados.fetchone()


def atualizarJogo(jogo_id, nome, dataInicio, dataConclusao, finalizado):
    try:
        cursor.execute("""
        UPDATE jogo SET nome = ?, dataInicio = ?, dataConclusao = ?,
        finalizado = ? WHERE id = ?""",
        (nome, dataInicio, dataConclusao, finalizado, jogo_id)
        )
        conn.commit()
    except sqlite3.Error as erro:
        print(cores.erro("Erro ao atualizar registro do jogo. Erro: "), erro)
    else:
        print(cores.sucesso("Registro atualizado com sucesso."))


def excluirJogo(jogo_id):
    try:
        cursor.execute("""
        DELETE FROM jogo where id = ?""", (jogo_id, ))
        conn.commit()
    except sqlite3.Error as erro:
        print(cores.erro("Erro ao excluir registro. erro: "), erro)
    else:
        print(cores.sucesso("Exclusao realizada com sucesso."))


def listarJogos(criterio="todos"):
    sql = {
        "todos": "SELECT * FROM jogo",
        "finalizado": "SELECT * FROM jogo WHERE finalizado = '1'",
        "jogando": "SELECT * FROM jogo WHERE finalizado = '0'",
        "nome": "SELECT * FROM jogo ORDER BY UPPER(nome)",
        "data": "SELECT * FROM jogo ORDER BY dataInicio"
    }
    try:
        dados = cursor.execute(sql[criterio])
    except sqlite3.Error as erro:
        print(cores.erro("Erro ao ler registro do jogo. Erro: "), erro)
    else:
        return dados.fetchall()


def idExiste(id):
    try:
        cursor.execute(
            "SELECT id FROM jogo WHERE id = ?", (str(id), )
        )
    except sqlite3.Error as erro:
        print("Erro ao buscar existencia do id. erro:", erro)
    else:
        if cursor.fetchone():
            return True
        return False
