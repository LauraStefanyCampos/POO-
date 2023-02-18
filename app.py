from classes import Estudiante
from dotenv import load_dotenv

def main():
    estudiante = Estudiante("Laura","Campos","93012013")
    estudiante.save()
    
    estudiante.apellido = "Campos Gonzales"
    estudiante.Update()
    
if __name__ == "__main__":
    load_dotenv()
    main()


