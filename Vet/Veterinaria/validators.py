from django.core.exceptions import ValidationError

def validate_chilean_cellphone(value: str):
    if len(value) != 12:
        raise ValidationError(
            "%s es muy corto para ser número de teléfono" % (value)
        )

    if not value.startswith("+"): # o también dicho if value[0] != "+"
        raise ValidationError(
            "%s no comienza con un signo +" % (value)
        )

    codigo_de_pais = value[1:4] # desde el segundo char hasta el cuarto
    if codigo_de_pais != "569":
        raise ValidationError(
            "%s no corresponde a un celular chileno porque no parte con +569" % (value)
        )

    el_otro_digito = value[4] # el quinto char
    if el_otro_digito not in ["9", "8", "7", "6"]:
        raise ValidationError(
            "lo que viene después del +569 debe ser un 6, un 7, un 8 o un 9, y me pasaste: %s" % (el_otro_digito)
        )

    el_resto_del_numero = value[5:] # del quinto caracter hasta el final
    lista_de_digitos = range(10)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista_de_char_de_los_digitos = [str(digito) for digito in lista_de_digitos]  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for digito in el_resto_del_numero:
        if digito not in lista_de_char_de_los_digitos:
            raise ValidationError(
                "El número parte en +569X, ok, pero el resto: %s, tiene algún caracter que no es dígito." % (el_resto_del_numero)
            )