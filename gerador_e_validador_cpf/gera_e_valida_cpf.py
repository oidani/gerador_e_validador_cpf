import random

def verifica_cpf_inserido(cpf):
	return len(cpf) == 11 and cpf.isdigit() and cpf.count(cpf[0]) != 11

def calcula_dv(cpf_lista, c):
	lista_validacao_dv = []
	for i in range(0, c-1):
		lista_validacao_dv.append(cpf_lista[i] * c)
		c -= 1
	soma_validacao_dv = sum(lista_validacao_dv)

	calculo_dv = soma_validacao_dv % 11

	return 0 if calculo_dv < 2 else 11 - calculo_dv

def converte_cpf(cpf):
	cpf_convertido = ""
	for i in range(len(cpf)):
		if i == 3 or i == 6:
			cpf_convertido += "." + str(cpf[i])
		elif i == 9:
			cpf_convertido += "-" + str(cpf[i])
		else:
			cpf_convertido += str(cpf[i])
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
				"4": "PE, RN, PB, AL",
				"5": "BA, SE",
				"6": "MG",
				"7": "RJ, ES",
				"8": "SP",
				"9": "PR, SC"}
	return dict_uf[digito_uf]

def valida_cpf(cpf):
    primeiro_dv = segundo_dv = 0

    cpf_lista = [int(cpf[digito]) for digito in range(len(cpf))]

    primeiro_dv = calcula_dv(cpf_lista, 10)
    segundo_dv = calcula_dv(cpf_lista, 11)

    return cpf_lista, compara_dv(cpf_lista, primeiro_dv, segundo_dv)

def gera_cpf():
    cpf_lista = []

    for i in range(9):
        cpf_lista.append(random.randint(0, 9))

    cpf_lista.append(calcula_dv(cpf_lista, 10))
    cpf_lista.append(calcula_dv(cpf_lista, 11))

    return cpf_lista

def main():
    print()
    print("GERADOR E VALIDADOR DE CPF")
    print()
    print("O que você deseja:")
    print("1. Gerar um CPF válido")
    print("2. Validar um CPF")
    print()
    escolha = input("Escolha: ")

    print()

    if escolha.isdigit() and escolha =="1":
        cpf_lista = gera_cpf()

        print(f"CPF      : { converte_cpf(cpf_lista) }")
        print(f"SITUAÇÃO : válido")
        print(f"UF       : { verifica_uf(str(cpf_lista[8])) }")

    elif escolha.isdigit() and escolha =="2":
        cpf = input("Por gentileza, insira o CPF para validação (apenas números): ")

        print()
        if verifica_cpf_inserido(cpf):
            cpf_lista, situacao = valida_cpf(cpf)

            print(f"CPF      : { converte_cpf(cpf_lista) }")
            print(f"SITUAÇÃO : { situacao }")
            if situacao == "válido":
                print(f"UF       : { verifica_uf(str(cpf_lista[8])) }")

        else:
            print(f"CPF      : { cpf }")
            print(f"SITUAÇÃO : inválido")

    else:
        print("Valor inserido é incorreto.")
    print()

if __name__ == "__main__":
	main()
