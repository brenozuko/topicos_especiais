import json
import requests
import os

navegador = {
    "User-Agent": "Chrome"
}
base_url = "https://parallelum.com.br/fipe/api/v1/carros/marcas"


def get_marcas():
    data = requests.get(url=base_url, headers=navegador)
    return data.json()


def print_marcas(marcas):
    print('Marcas: \n\n')
    for marca in marcas:
        print(f'Marca: {marca["nome"]} - Código: {marca["codigo"]}')
    print('\n\n\n')


def get_modelos(marca_codigo):
    url = base_url + "/" + marca_codigo + "/modelos"
    data = requests.get(url=url, headers=navegador)
    return data.json()


def print_modelos(modelos):
    print('Modelos da marca: \n\n')
    for modelo in modelos["modelos"]:
        print(f'Modelo: {modelo["nome"]} - Código: {modelo["codigo"]}')
    print('\n\n\n')


def get_anos(marca_codigo, modelo_codigo):
    url = base_url + "/" + marca_codigo + "/modelos/" + modelo_codigo + "/anos"
    data = requests.get(url=url, headers=navegador)
    return data.json()

def print_anos(anos):
    print('Anos do modelo: \n\n')
    for ano in anos:
        print(f'Ano: {ano["nome"]} - Código: {ano["codigo"]}')
    print('\n\n\n')

def get_veiculo(marca_codigo, modelo_codigo, ano_codigo):
    url = base_url + "/" + marca_codigo + "/modelos/" + modelo_codigo + "/anos/" + ano_codigo
    data = requests.get(url=url, headers=navegador)
    return data.json()

def print_veiculo(veiculo):
    print('Veículo: \n\n')
    print(f'Marca: {veiculo["Marca"]}')
    print(f'Modelo: {veiculo["Modelo"]}')
    print(f'Ano: {veiculo["AnoModelo"]}')
    print(f'Combustível: {veiculo["Combustivel"]}')
    print(f'Preço: {veiculo["Valor"]}')
    print(f'Código Fipe: {veiculo["CodigoFipe"]}')
    print(f'Mês de referência: {veiculo["MesReferencia"]}')
    print(f'Tipo de veículo: {veiculo["TipoVeiculo"]}')
    print(f'Sigla do combustível: {veiculo["SiglaCombustivel"]}')
    print('\n\n\n')

print_marcas(get_marcas())

marca_codigo = input("Digite o código da marca: ")

os.system('clear')

print_modelos(get_modelos(marca_codigo))

modelo_codigo = input("Digite o código do modelo: ")

os.system('clear')

print_anos(get_anos(marca_codigo, modelo_codigo))

ano_codigo = input("Digite o código do ano: ")

os.system('clear')

print_veiculo(get_veiculo(marca_codigo, modelo_codigo, ano_codigo))