import uvicorn
from src.settings import settings

if __name__ == '__main__':
    uvicorn.run('src.main:app', reload=True, port=settings.port, host=settings.host)
