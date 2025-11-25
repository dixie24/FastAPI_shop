from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    slug = Column(String, unique=True, index=True, nullable=False)
    prices = Column(Integer, unique=True, index=True, nullable=False)
    
    
    products = relationship("Product", back_populates="category")
    tags = relationship("Tag", secondary="category_tags", back_populates="categories")
    sales = relationship("Sale", back_populates="category")
    
    sales2 = relationship("Sale2", back_populates="category")
    purchases = relationship("Purchase", back_populates="category")
    purchases2 = relationship("Purchase2", back_populates="category")df
    stock_entries = relationship("StockEntry", back_populates="category")
    stock_exits = relationship("StockExit", back_populates="category")
    stock_exits2 = relationship("StockExit2", back_populates="category")
    prices = relationship("prices", back_populates="category") 
    prices2 = Column(Integer, unique=True, index=True, nullable=False)
    discounts = Column(Integer, unique=True, index=True, nullable=False)
    discounts2 = Column(Integer, unique=True, index=True, nullable=False)
    discounts3 = Column(Integer, unique=True, index=True, nullable=False)
    available = Column(Integer, unique=True, index=True, nullable=False)
              
    
    def models.AutoField(_("rt"))
    
    
    
    def __reapr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
    
    
    
    models.DecimalField(_(""), max_digits=5, decimal_places=2)