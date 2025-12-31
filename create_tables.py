from database import engine, Base
from models import User  # import all models here

# This will create all tables defined in your models
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
