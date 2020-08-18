from validate_docbr import CNPJ

class Cnpj:
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
