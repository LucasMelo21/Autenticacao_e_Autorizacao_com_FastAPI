from core.configs import settings
from core.database import engine

async def criar_tabelas():
    print('Criando tabelas...')

    from models import __all_models

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criada com sucesso!')

if __name__ == '__main__':
    import asyncio

    asyncio.run(criar_tabelas())