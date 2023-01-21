endereco = 'Rua Itaguaçu 701, apartamento 604, Bela Vista, São José, SC, 88110-790'

import re

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)
else: 
    raise ValueError("Não foi encontrado o cep")
