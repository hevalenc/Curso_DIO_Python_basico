#trabalhando com APIs. a biblioteca 'request' é: Requests is an elegant and simple HTTP library for Python
#o commando '.get' é usado para obter os dados do local citado entre ( )
import requests

def retorna_dados_cep(cep):
    response = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    #o resultado 200 significa que teve sucesso no requerimento
    print(response.json())
    #o comando '.json' estabelece um formato para troca de dados entre programas, traz os dados em uma lista
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://globallab.org/en/#.XwCPOudv_IU')
    print(response)
    #este exemplo acima mostra toda a programação de uma página de internet sem renderização
    # retorna_dados_cep('01001000')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])
