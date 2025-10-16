from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

from core.configs import settings

engine = create_async_engine(settings.DB_URL, echo=True)

Session = async_sessionmaker(autoflush=False,
                                     expire_on_commit=False,
                                     class_=AsyncSession,
                                     autocommit=False,
                                     bind=engine)