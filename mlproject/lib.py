# mlproject/lib.py

def hello_world():
    return "Hello world from mlproject"

def try_me(year_of_birth, female):
    # function that returns the real age according to the sexe
    age=2022-year_of_birth
    if female ==True and age>29:
         return 28
    else:
        return 2022-year_of_birth
