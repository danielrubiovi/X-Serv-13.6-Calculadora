#!/usr/bin/python
#Daniel Rubio Villegas, grado en Sistemas
#Ejercicio 13.6

import sys

len_parametros = len(sys.argv)
operaciones_val = ['suma', 'resta', 'multiplicacion', 'division']

def bien_argnum():
	if len_parametros != 4:
		return False
	else:
		return True

def comprob_opera (op_argv):
	if op_argv in operaciones_val:
		return True
	else:
		return False

def comprob_param (bien_argnum,bien_op):
	if not bien_argnum or not bien_op:
		if not bien_op:
			print ("\nError en la operacion introducida. Valido:|suma|resta|multiplicacion|division|")
		sys.exit ("\nUsage Error! \nCompruebe los parametros 'python3 calculadora.py operacion operando1 operando2'\n")

def suma (num1,num2):
	return print (num1, "+", num2, "=", num1 + num2)

def resta (num1,num2):
	return print (num1, "-", num2, "=", num1 - num2)

def multi (num1,num2):
	return print (num1, "*", num2, "=", num1 * num2)

def div (num1,num2):
	try:
		return print (num1, "/", num2, "=", num1 / num2)
	except ZeroDivisionError:
		print ("\nNo se puede dividir entre cero :Sorry\n")

def operaciones (num1,num2):
	if op_argv == operaciones_val[0]:
	 	return suma(num1, num2)
	if op_argv == operaciones_val[1]:
		return resta(num1,num2)
	if op_argv == operaciones_val[2]:
		return multi(num1,num2)
	if op_argv == operaciones_val[3]:
		return div(num1,num2)


if __name__ == "__main__":

	bien_argnum = bien_argnum()
	op_argv = sys.argv[1]
	bien_op = comprob_opera(op_argv)

	try:
		try:
			num1 = float(sys.argv[2])
			num2 = float(sys.argv[3])
		except IndexError:
			print ("\nFalta algun operando, revise los parametros introducidos.")
	except ValueError:
		print ("\nLos operando solo pueden ser enteros o float.")

	comprob_param (bien_argnum,bien_op)
	operaciones(num1,num2)
