import os

base_dir = os.path.abspath(os.path.dirname(__file__))
print(base_dir)
print("sqlite:///" + os.path.join(base_dir, "app.db"))


class Config:

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "app.db")
