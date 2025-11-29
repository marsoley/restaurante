from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime
from datetime import datetime


DATABASE_URL = "sqlite:///./res.db"
import os
print(">>> BASE DE DATOS USADA:", os.path.abspath("restaurante.db"))


engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ---------- MODELOS BD -------------

class ProductoDB(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    precio = Column(Integer, nullable=False)
    categoria = Column(String, nullable=True)
    stock = Column(Integer, nullable=False)



class InsumoDB(Base):
    __tablename__ = "insumos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    categoria = Column(String, nullable=True)
    cantidad = Column(Float, nullable=False)
    unidad = Column(String, nullable=False)

class VentaDB(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, nullable=False)
    cantidad = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)
