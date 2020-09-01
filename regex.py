import re

padraoEmail = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
textoEmail = "asdfnlijsaghligajg italoads31@gmail.com skjbfviudsjhnvoknsdov"
respostaEmail = re.search(padraoEmail,textoEmail)
print(respostaEmail.group())

###########################################

padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "meu numero de telefone é 1245645412"

resposta = re.search(padrao,texto)

print(resposta.group())