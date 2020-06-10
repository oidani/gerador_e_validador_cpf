def verifica_cpf_inserido(cpf_solicitado):	
	return len(cpf_solicitado) == 11 and cpf_solicitado.isdigit()

def calcula_dv(cpf_lista, c):
	lista_validacao_dv = []
	for i in range(0, c-1):
		lista_validacao_dv.append(cpf_lista[i] * c)
		c -= 1
	soma_validacao_dv = sum(lista_validacao_dv)

	calculo_dv = soma_validacao_dv % 11

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

def compara_dv(cpf_lista, primeiro_dv, segundo_dv):		
	if primeiro_dv == cpf_lista[9] and segundo_dv == cpf_lista[10]:
		return "válido"
	return "inválido"

def verifica_uf(digito_uf):
	dict_uf = {"0": "RS",
				"1": "DF, GO, MS, TO",
				"2": "PA, AM, AC, AM, RO, RR",
				"3": "CE, MA, PI",
				"4": "PE, RN, PA, AL",
				"5": "BA, SE",
				"6": "MG",
				"7": "RJ, ES",
				"8": "SP",
				"9": "PR, SC"}
	return dict_uf[digito_uf]

def main():
	print()
	cpf_solicitado = input("Por gentileza, insira o CPF para validação (apenas números): ")
	
	cpf_lista = []
	primeiro_dv = segundo_dv = 0

	print()
	if verifica_cpf_inserido(cpf_solicitado):
		cpf_lista = [int(cpf_solicitado[digito]) for digito in range(len(cpf_solicitado))]
		
		primeiro_dv = calcula_dv(cpf_lista, 10)
		segundo_dv = calcula_dv(cpf_lista, 11)

		print("----------------------------------")
		print(f"CPF      : { converte_cpf(cpf_solicitado) }")
		print("----------------------------------")
		print(f"SITUAÇÃO : { compara_dv(cpf_lista, primeiro_dv, segundo_dv) }")
		if compara_dv(cpf_lista, primeiro_dv, segundo_dv) == "válido":
			print("----------------------------------")
			print(f"UF       : { verifica_uf(cpf_solicitado[8]) }")
			print("----------------------------------")
	else:
		print("----------------------------")
		print(f"CPF  : { cpf_solicitado }")
		print("----------------------------")
		print("ERRO : valor fora do padrão")
		print("----------------------------")
		#return "inválido"
	print()

if __name__ == "__main__":
	main()