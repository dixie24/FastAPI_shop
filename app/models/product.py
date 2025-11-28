from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime
import decimal
import models

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    sales2 = relationship("Sale2", back_populates="category")
    purchases = relationship("Purchase", back_populates="category")
    purchases2 = relationship("Purchase2", back_populates="category")
    stock_entries = relationship("StockEntry", back_populates="category")
    stock_exits = relationship("StockExit", back_populates="category")
    category = relationship("Category", back_populates="products")  
    category2 = Column(Integer, unique=True, index=True, nullable=False)
    category3 = Column(Integer, unique=True, index=True, nullable=False)
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
    
class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    products = relationship("Product", back_populates="category")
    tags = relationship("Tag", secondary="category_tags", back_populates="categories")
    sales = relationship("Sale", back_populates="category")
    prices = relationship("price", back_populates="prices")
    prices2 = Column(Integer, unique=True, index=True, nullable=False)
    discounts = Column(Integer, unique=True, index=True, nullable=False)
    discounts2 = Column(Integer, unique=True, index=True, nullable=False)
    discounts3 = Column(Integer, unique=True, index=True, nullable=False)
    available = Column(Integer, unique=True, index=True, nullable=False)
    not_available = Column(Integer, unique=True, index=True, nullable=False)
    
    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
    models.DecimalField(_(""), max_digits=5, decimal_places=2)
    models.DecimalField(_(""), max_digits=5, decimal_places=3)
    models.DecimalField(_(""), max_digits=5, decimal_places=4)
    models.AutoField(_("rt"))
    models.AutoField(_("rt"))
    models.AutoField(_("rt"))   
    models.AutoField(_("rt"))