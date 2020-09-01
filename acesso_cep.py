import requests
class Busca_Endereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("Cep Invalido!!")

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def __str__(self):
        return self.format_cep()

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_via_api_cep(self):
        url_base = f"https://viacep.com.br/ws/{self.cep}/json"
        r = requests.get(url_base)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )