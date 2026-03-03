import asyncio

async def primeira_funcao():
    print('Estou entrando na 1ª Função...')
    await asyncio.sleep(3)
    print('Estou saindo da 1ª Função...')

async def segunda_funcao():
    print('Estou entrando na 2ª Função...')
    await asyncio.sleep(9)
    print('Estou saindo da 2ª Função...')

async def terceiro_funcao():
    print('Estou entrando na 3ª Função...')
    await asyncio.sleep(5)
    print('Estou saindo da 3ª Função...')


async def executar_funcoes():
    await asyncio.gather(
        primeira_funcao(),
        segunda_funcao(),
        terceiro_funcao()
    )


asyncio.run(executar_funcoes())