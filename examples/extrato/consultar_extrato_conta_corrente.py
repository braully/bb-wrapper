import os
from datetime import date, timedelta

from examples.utils import dump_response

from bb_wrapper.wrapper import ExtratoContaCorrenteBBWrapper


lote_data = {
    "agencia": 1505,
    "conta": 1348,
}

c = ExtratoContaCorrenteBBWrapper(agencia=1505, conta=1348, cert=("./certs/cert.pem", "./certs/key.pem"))

today = date.today()
bb_fmt = "%d%m%Y"




consulta_data = {
    "numero_pagina_solicitacao": 1,
    "quantidade_registro_pagina_solicitacao": 200,
    "data_inicio_solicitacao": (today - timedelta(days=30)).strftime(bb_fmt),
    "data_fim_solicitacao": today.strftime(bb_fmt)
}

# consultar_extrato_conta_corrente(self, numero_pagina_solicitacao=1,
#                                     quantidade_registro_pagina_solicitacao=200,
#                                     data_inicio_solicitacao=None,
#                                     data_fim_solicitacao=None):


response = c.consultar_extrato_conta_corrente(**consulta_data)

print(response.data)

dump_response(response, os.path.realpath(__file__))


