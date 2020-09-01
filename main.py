from Documento import Documento
from acesso_cep import Busca_Endereco
import requests

'''cpf = '80391617000114'
#cnpf = Cnpj('80391617000114')

doc = Documento.cria_documento(cpf)
print(doc)'''

cep = '61635035'

obj = Busca_Endereco(cep)

r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

bairro, cidade, uf = obj.acessa_via_api_cep()

print(bairro, cidade, uf)