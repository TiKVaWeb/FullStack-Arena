from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

# Укажите URL вашей базы данных
# DATABASE_URL = "postgresql+asyncpg://user:password@localhost/skins_trade"  # Для PostgreSQL
DATABASE_URL = "sqlite+aiosqlite:///./skins_trade.db"

# Создаем асинхронный движок
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем асинхронную сессию
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Базовый класс для моделей
Base = declarative_base()

# Функция для получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session