def valida_cpf_inserido(cpf_solicitado):
	return [int(cpf_solicitado[digito]) for digito in range(len(cpf_solicitado)) if isinstance(digito, int)]

def calcula_dv(cpf_lista, c):
	lista_validacao_dv = []
	for i in range(0, c-1):
		lista_validacao_dv.append(cpf_lista[i] * c)
		c -= 1
	soma_validacao_dv = sum(lista_validacao_dv)

	calculo_dv = soma_validacao_dv - ((soma_validacao_dv // 11) * 11)

	return 0 if calculo_dv < 2 else 11 - calculo_dv

def converte_cpf(cpf_solicitado):
	cpf_convertido = ""
	for i in range(len(cpf_solicitado)):
		if i == 3 or i == 6:
			cpf_convertido += "." + cpf_solicitado[i]
		elif i == 9:
			cpf_convertido += "-" + cpf_solicitado[i]
		else:
			cpf_convertido += cpf_solicitado[i]
	return cpf_convertido

def principal(cpf_solicitado):
	#cpf_solicitado = input("Por gentileza, insira o CPF para validação (apenas números): ")
	
	cpf_lista = valida_cpf_inserido(cpf_solicitado)

	primeiro_dv = calcula_dv(cpf_lista, 10)
	segundo_dv = calcula_dv(cpf_lista, 11)

	'''if primeiro_dv == cpf_lista[9] and segundo_dv == cpf_lista[10]:
		validacao = "válido"
	else:
		validacao = "inválido"
	
	print("%s é um CPF %s." %(converte_cpf(cpf_solicitado), validacao))'''

	if primeiro_dv == cpf_lista[9] and segundo_dv == cpf_lista[10]:
		return "válido"
	else:
		return "inválido"

def testa_cpf(obtido, esperado):
	if obtido == esperado:
		prefixo = "PASSOU"
	else:
		prefixo = "FALHOU"
	print ("%s - obtido: %s - esperado: %s" % (prefixo, obtido, esperado))

def main():
	testa_cpf(principal("08601078419"), "válido")
	testa_cpf(principal("11144477754"), "inválido")
	testa_cpf(principal("26758121453"), "válido")

if __name__ == "__main__":
	main()