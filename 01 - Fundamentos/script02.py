from typing import Optional

'''
python -m venv venv
python venv\Script\Activate
pip install mypy
''' 

# Type Hints: Sugestão de Tipo
nome: str = 'João'
idade: int = 10
altura: float = 1.67
status: bool = True
minha_lista: list[str | int] = ['Pedro', 'Arthur', 'Ana', 'Claudia', 10]
dados: dict[str,str | int] = {'nome': 'Francisco', 'email': 'francisco@gmail.com', 'idade': 30}


def somar(valor1: int, valor2: int) -> int:
    '''
        Entrada: valor1 (int) e valor2 (int)
        Retorno: int
    '''
    return valor1 + valor2


class Aluno:
    nome: str
    idade: int
    email: Optional[str] = None


def exibir_dados(nome: str, idade: int, email: Optional[str] = None):
    dados = {
        'nome': nome,
        'idade': idade
    }
    # Verificar se foi passado um valor para email no argumento da função...
    if email:  # email is not None
        dados['email'] = email

    return dados


print(exibir_dados('Maria', 20, 'maria@gmail.com'))