from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import Integer, String, Numeric


DATABASE_URL = "mysql+pymysql://root:@127.0.0.1:3306/inven_db"

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Numeric(10, 2))


with Session(engine) as session:

    # CREATE
    product = Product(
        name="Keyboard",
        quantity=30,
        price=1200
    )

    session.add(product)
    session.commit()

    print("Product inserted!")

    # READ
    products = session.query(Product).all()

    for product in products:
        print(
            product.id,
            product.name,
            product.quantity,
            product.price
        )
