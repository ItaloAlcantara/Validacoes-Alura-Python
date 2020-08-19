from validate_docbr import CPF,CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos invalida!")


class DocCpf(object):

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf invalido!")

    def __str__(self):
        return self.formata_cpf()

    def cpf_eh_valido(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj(object):

    def __init__(self, documento):
        documento = str(documento)
        if self.cnpj_eh_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ invalido!")

    def __str__(self):
        return self.formata_cnpj()

    def cnpj_eh_valido(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


