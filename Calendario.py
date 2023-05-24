import calendar as cal
import pyfiglet as  PyF

ador = ""
Titulo=PyF.figlet_format("CALENDARIO".center(20) , font="slant")
print(Titulo)
print (f"{ador.center(50,'*')}")

año=input("Ingrese el año: ")
mes =input("Ingrese el mes: ")
year = int(año)
month = int(mes)
print (f"{ador.center(50,'*')}")

print(f"{cal.month(year,  month)}")
