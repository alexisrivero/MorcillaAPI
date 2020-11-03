from django import forms
from django.core.exceptions import ValidationError


class GeneradorImagenForm(forms.Form):
    numero_maximo = forms.NumberInput()
    rotacion_contrareloj = forms.BooleanField(
        help_text="rotacion contra reloj")
    SERIES_DISPONIBLES = (
        ("PI", "DIGITOS DEL NUMERO PI"),
        ("FI", "NUMERO FIBONACCI"),
        ("PR", "NUMEROS PRIMOS"),
    )
    serie_numeros = forms.ChoiceField(
        choices=SERIES_DISPONIBLES, help_text="serie de numeros")

    def clean_numero_maximo(self):
        data = self.cleaned_data["numero_maximo"]

        if type(data) != int and type(data) != float:
            raise ValidationError("este chorizo no es un numero")
        if data > 100000:
            raise ValidationError("muchos numeros bro")
        return data
