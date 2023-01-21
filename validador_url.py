# Exemplos de URLs válidas:

# bytebank.com/cambio
# bytebank.com.br/cambio
# www.bytebank.com/cambio
# www.bytebank.com.br/cambio
# http://www.bytebank.com/cambio
# http://www.bytebank.com.br/cambio
# https://www.bytebank.com/cambio

# Exemplos de URLs inválidas:

# https://bytebank/cambio
# https://bytebank.naoexiste/cambio
# ht://bytebank.naoexiste/cambio

url = 'https://www.bytebank.com.br/cambio'

import re

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("URL invalida!!")

print("A URL é valida")

re.compile('DyL(0-9).(0-9){2}.(A-H)(0-9){4}')