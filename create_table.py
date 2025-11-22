# create_tables.py
from app.database import Base, engine
from app.repository.user_repository import User
from app.repository.product_repository import Product

Base.metadata.create_all(bind=engine)
