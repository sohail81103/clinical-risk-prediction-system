from utils.database import engine, Base
from utils import models

def init_db():
    Base.metadata.create_all(bind=engine)
