import sys
import math

def complexSum(a1,b1,a2,b2):
    return complex((a1 + a2),(b1 + b2))

def resta(a1,b1,a2,b2):
    return complex((a1 - a2),(b1 - b2))

def multiplicacion (a1,b1,a2,b2):
    return complex((a1*a2-b1*b2),(a1*b2+a2*b1));

def conjugado(z1,z2):
    return complex(z1,-z2);

def division(a1,b1,a2,b2):
    numerador = multiplicacion(a1,b1,a2,-b2);
    denominador = multiplicacion(a2,b2,a2,-b2);
    return complex(numerador/denominador);

def modulo (z1,z2):
    return (z1**2 + z2**2)**0.5

def polar (z1,z2):
    mod = modulo(z1,z2);
    angulo = math.atan(z2/z1);
    lista = []
    lista.append(mod)
    lista.append(angulo)
    tupla = tuple(lista)
    return tupla;

def cartesiana(z1,z2):
    return complex(z1*math.cos(z2),math.sen(z2))

def main():
    print("ingrese primer numero a sumar");
    tupla1 = list(map(int,sys.stdin.readline().strip().split(",")));
    tupla2 = list(map(int,sys.stdin.readline().strip().split(",")));
    tupla1 = tuple(tupla1);
    tupla2 = tuple(tupla2);
    a1 = tupla1[0];
    b1 = tupla1[1];
    a2 = tupla2[0];
    b2 = tupla2[1];
    print("la suma es:");
    print(complexSum(a1,b1,a2,b2));
    print("la resta es:");
    print(resta(a1,b1,a2,b2));
    print("la multiplicacion es:");
    print(multiplicacion(a1,b1,a2,b2));
    print("la division es:");
    print(division(a1,b1,a2,b2));
    print("el modulo del primer numero complejo es:")
    print(modulo(a1,b1));
    print("el modulo del segundo numero complejo es:")
    print(modulo(a2,b2));
    print("el conjugado del primer numero es:")
    print(conjugado(a1,b1));
    print("el conjugado del segundo numero es:")
    print(conjugado(a2,b2));
    print("las coordenadas polares del primer numeros son:")
    print(polar(a1,b1));
    print("las coordenadas polares del segundo numero son:")
    print(polar(a2,b2));
main();
