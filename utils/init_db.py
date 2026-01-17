from utils.database import engine
from utils.models import Base

def init_db():
    Base.metadata.create_all(bind=engine)
