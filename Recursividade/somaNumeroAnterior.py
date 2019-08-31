def somaNumeroAnterior(numMaximo):
	if(numMaximo == 0):
		return 0
	soma = numMaximo + somaNumeroAnterior(numMaximo - 1)
	return soma

def gerarFibonacci(numero):
		if(numero == 0):
			return 0
		if(numero == 1 or numero == 2):
			return 1
		return gerarFibonacci(numero - 1) + gerarFibonacci(numero - 2)
		
	
valorUsuario = int(input("Digite um número para somar seus anteriores: "))
print(somaNumeroAnterior(valorUsuario))
print("Gerando a sequência de Fibonacci...\n")
for x in range(valorUsuario):
	print(gerarFibonacci(x), end = ' ')