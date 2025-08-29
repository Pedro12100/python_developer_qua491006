from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import arquivo as ar

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "pessoa"
    id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    data_nascimento = Column(Date, nullable=False)

def criar_tb_pessoa(engine):
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f"Não foi possível conectar ao banco. {e}")

def main():
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    criar_tb_pessoa(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print(f"{'-'*20} CRUD {'-'*20}")
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas")
        print("3 - Alterar dados de uma pessoa")
        print("4 - Excluir uma pessoa")
        print("5 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        ar.limpar()

        match opcao:
            case "1":
                ar.cadastrar_pessoa(session, Pessoa)
            case "2":
                ar.listar_pessoas(session, Pessoa)
            case "3":
                ar.pesquisar_pessoa(session, Pessoa)
            case "4":
                print("Funcionalidade ainda não implementada.")
            case "5":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue

    session.close()

if __name__ == "__main__":
    main()
