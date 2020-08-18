from validate_docbr import CPF

class Cpf:
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