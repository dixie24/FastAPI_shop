from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    slug = Column(String, unique=True, index=True, nullable=False)
    
    products = relationship("Product", back_populates="category")
    tags = relationship("Tag", secondary="category_tags", back_populates="categories")
    sales = relationship("Sale", back_populates="category")
    
    def __reapr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
    
    
    models.DecimalField(_(""), max_digits=5, decimal_places=2)