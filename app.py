import pymongo

from classes import Estudiante, DbMongo
from classes import Estudiante
from dotenv import load_dotenv

def main():
    db = DbMongo.getDB()
    estudiante = Estudiante("Uayeb 3","Caballero","31487539")
    estudiante.save(db)

    estudiante.save()

if __name__ == "__main__":
    load_dotenv()
    main()
