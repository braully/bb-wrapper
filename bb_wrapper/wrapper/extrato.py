from .bb import BaseBBWrapper
from ..constants import AGENCIA, CONTA


# {
#     "openapi": "3.1.0",
#     "x-stoplight": {
#         "id": "pl3nscvkiz1vk"
#     },
#     "info": {
#         "title": "Extratos API",
#         "version": "1.0",
#         "description": "API para gerenciar os serviços de extrato de clientes do Banco do Brasil S.A.",
#         "contact": {
#             "name": "Banco do Brasil S.A. - BB for Developers",
#             "url": "https://developers.bb.com.br"
#         }
#     },
#     "servers": [
#         {
#             "url": "https://api.sandbox.bb.com.br/extratos/v1",
#             "description": "Homologação"
#         },
#         {
#             "url": "https://api.hm.bb.com.br/extratos/v1",
#             "description": "Homologação 2"
#         },
#         {
#             "url": "https://api-extratos.hm.bb.com.br/extratos/v1",
#             "description": "Homologação 3"
#         },
#         {
#             "url": "https://api-extratos.bb.com.br/extratos/v1",
#             "description": "Produção"
#         }
#     ],
#     "paths": {
#         "/conta-corrente/agencia/{agencia}/conta/{conta}": {
#             "parameters": [
#                 {
#                     "schema": {
#                         "type": "string",
#                         "example": "1505"
#                     },
#                     "name": "agencia",
#                     "in": "path",
#                     "required": true,
#                     "description": "Número da agência, sem dígito verificador"
#                 },
#                 {
#                     "schema": {
#                         "type": "string",
#                         "example": "1348"
#                     },
#                     "name": "conta",
#                     "in": "path",
#                     "required": true,
#                     "description": "Número da conta, sem dígito verificador"
#                 }
#             ],
#             "get": {
#                 "summary": "Consultar extrato de conta corrente",
#                 "responses": {
#                     "200": {
#                         "description": "SUCESSO. A requisição foi atendida pelo servidor.",
#                         "content": {
#                             "application/json": {
#                                 "schema": {
#                                     "type": "object",
#                                     "properties": {
#                                         "numeroPaginaAtual": {
#                                             "type": "integer",
#                                             "minimum": 0,
#                                             "maximum": 9999999,
#                                             "format": "int32",
#                                             "example": 1,
#                                             "description": "Número da página de resposta atual."
#                                         },
#                                         "quantidadeRegistroPaginaAtual": {
#                                             "type": "integer",
#                                             "description": "Quantidade de registros da página de resposta atual.",
#                                             "example": 100,
#                                             "format": "int32",
#                                             "maximum": 200
#                                         },
#                                         "numeroPaginaAnterior": {
#                                             "type": "integer",
#                                             "minimum": 0,
#                                             "maximum": 9999999,
#                                             "format": "int32",
#                                             "description": "Número da página de resposta anterior. Assume valor zero caso a página atual seja a página 1.",
#                                             "example": 0
#                                         },
#                                         "numeroPaginaProximo": {
#                                             "type": "integer",
#                                             "description": "Número da próxima página de resposta. Assume valor zero caso a página atual seja a última página de resposta do extrato solicitado.",
#                                             "format": "int32",
#                                             "example": 2
#                                         },
#                                         "quantidadeTotalPagina": {
#                                             "type": "integer",
#                                             "minimum": 0,
#                                             "maximum": 9999999,
#                                             "format": "int32",
#                                             "example": 5,
#                                             "description": "Quantidade total de páginas de resposta do extrato solicitado."
#                                         },
#                                         "quantidadeTotalRegistro": {
#                                             "type": "integer",
#                                             "description": "Quantidade total de registros de lançamentos do extrato solicitado.",
#                                             "minimum": 0,
#                                             "maximum": 99999,
#                                             "format": "int32",
#                                             "example": 1000
#                                         },
#                                         "listaLancamento": {
#                                             "type": "object",
#                                             "description": "Array com os registros de lançamentos da página de resposta atual. Os campos seguintes estão subordinados a este array. Quantidade máxima ocorrências do array:  200 registros.",
#                                             "properties": {
#                                                 "indicadorTipoLancamento": {
#                                                     "type": "string",
#                                                     "description": "Indica o tipo do lançamento. Domínio: \n1 -  Lançamentos efetivados \n2 - Lançamentos futuros",
#                                                     "enum": [
#                                                         "1",
#                                                         "2"
#                                                     ]
#                                                 },
#                                                 "dataLancamento": {
#                                                     "type": "integer",
#                                                     "description": "Data do lançamento no formato DDMMAAAA.",
#                                                     "maximum": 31129999,
#                                                     "format": "int64",
#                                                     "example": 11112022
#                                                 },
#                                                 "dataMovimento": {
#                                                     "type": "integer",
#                                                     "description": "Data do movimento no formato DDMMAAAA. Informação retornada em casos de lançamentos com data retroativa.",
#                                                     "maximum": 31129999,
#                                                     "format": "int64",
#                                                     "example": 10112022
#                                                 },
#                                                 "codigoAgenciaOrigem": {
#                                                     "type": "integer",
#                                                     "description": "Código da agência de origem do lançamento.",
#                                                     "minimum": 0,
#                                                     "maximum": 9999,
#                                                     "format": "int32",
#                                                     "example": 7988
#                                                 },
#                                                 "numeroLote": {
#                                                     "type": "integer",
#                                                     "description": "Número identificador do sistema de origem do lançamento.",
#                                                     "minimum": 0,
#                                                     "maximum": 99999,
#                                                     "format": "int32"
#                                                 },
#                                                 "numeroDocumento": {
#                                                     "type": "integer",
#                                                     "description": "Número identificador do lançamento.",
#                                                     "minimum": 0,
#                                                     "maximum": 100000000000000000,
#                                                     "format": "int64",
#                                                     "example": 607984000004010
#                                                 },
#                                                 "codigoHistorico": {
#                                                     "type": "integer",
#                                                     "minimum": 0,
#                                                     "maximum": 999,
#                                                     "format": "int32",
#                                                     "description": "Código para identificar a categoria/natureza do lançamento no Banco do Brasil.",
#                                                     "example": 470
#                                                 },
#                                                 "textoDescricaoHistorico": {
#                                                     "type": "string",
#                                                     "description": "Texto com a informação descritiva do lançamento.",
#                                                     "minLength": 0,
#                                                     "maxLength": 25,
#                                                     "example": "Transferência enviada"
#                                                 },
#                                                 "valorLancamento": {
#                                                     "type": "number",
#                                                     "description": "Valor monetário do lançamento expresso em Reais (BRL), com duas casas decimais.",
#                                                     "minimum": 0,
#                                                     "maximum": 1000000000000000,
#                                                     "example": 120.35
#                                                 },
#                                                 "indicadorSinalLancamento": {
#                                                     "type": "string",
#                                                     "description": "Indicador para informar o sinal do valor armazenado no campo \"valorLancamento\". Domínio: \nD - débito \nC - crédito",
#                                                     "enum": [
#                                                         "D",
#                                                         "C"
#                                                     ]
#                                                 },
#                                                 "textoInformacaoComplementar": {
#                                                     "type": "string",
#                                                     "description": "Texto com informações complementares acerca do lançamento.",
#                                                     "minLength": 0,
#                                                     "maxLength": 38,
#                                                     "example": "Tar. agrupadas - ocorrencia 10/11/2022"
#                                                 },
#                                                 "numeroCpfCnpjContrapartida": {
#                                                     "type": "integer",
#                                                     "description": "Número do CPF ou CNPJ da contrapartida do lançamento.",
#                                                     "minimum": 0,
#                                                     "maximum": 99999999999999,
#                                                     "format": "int64",
#                                                     "example": 35484829100
#                                                 },
#                                                 "indicadorTipoPessoaContrapartida": {
#                                                     "type": "string",
#                                                     "description": "Indicador para informar o tipo da pessoa da contrapartida do lançamento. Domínio: \nF - física \nJ - jurídica",
#                                                     "enum": [
#                                                         "F",
#                                                         "J"
#                                                     ]
#                                                 },
#                                                 "codigoBancoContrapartida": {
#                                                     "type": "integer",
#                                                     "description": "Código de compensação (COMPE) do banco da contrapartida do lançamento.",
#                                                     "minimum": 0,
#                                                     "maximum": 999,
#                                                     "format": "int32",
#                                                     "example": 341
#                                                 },
#                                                 "codigoAgenciaContrapartida": {
#                                                     "type": "integer",
#                                                     "description": "Código da agência da contrapartida do lançamento.",
#                                                     "minimum": 0,
#                                                     "maximum": 9999,
#                                                     "format": "int32",
#                                                     "example": 7894
#                                                 },
#                                                 "numeroContaContrapartida": {
#                                                     "type": "string",
#                                                     "description": "Número de conta da contrapartida do lançamento.",
#                                                     "minLength": 0,
#                                                     "maxLength": 20,
#                                                     "example": "4010"
#                                                 },
#                                                 "textoDvContaContrapartida": {
#                                                     "type": "string",
#                                                     "description": "Dígito verificador da conta da contrapartida do lançamento.",
#                                                     "minLength": 0,
#                                                     "maxLength": 1,
#                                                     "example": "X"
#                                                 }
#                                             }
#                                         }
#                                     }
#                                 }
#                             }
#                         }
#                     },
#                     "400": {
#                         "description": "REQUISIÇÃO INVÁLIDA. O servidor não pôde processar a requisição devido a uma sintaxe de requisição malformada, estrutura da mensagem da requisição inválida ou valores inválidos.",
#                         "content": {
#                             "application/json": {
#                                 "schema": {
#                                     "$ref": "#/components/schemas/Erro"
#                                 }
#                             }
#                         }
#                     },
#                     "401": {
#                         "description": "NEGADO. O servidor entendeu a requisição, porém não a autorizou.",
#                         "content": {
#                             "application/json": {
#                                 "schema": {
#                                     "$ref": "#/components/schemas/ErrorOAuthUnauthorized"
#                                 }
#                             }
#                         }
#                     },
#                     "403": {
#                         "description": "NEGADO. O servidor entendeu a requisição, porém não a autorizou.",
#                         "content": {
#                             "application/json": {
#                                 "schema": {
#                                     "$ref": "#/components/schemas/Erro"
#                                 }
#                             }
#                         }
#                     },
#                     "404": {
#                         "description": "NÃO ENCONTRADO. O servidor não conseguiu encontrar o recurso solicitado.",
#                         "content": {
#                             "application/json": {
#                                 "schema": {
#                                     "$ref": "#/components/schemas/Erro"
#                                 }
#                             }
#                         }
#                     },
#                     "500": {
#                         "description": "ERRO INTERNO. O servidor encontrou uma condição inesperada que o impediu de atender a requisição.",
#                         "content": {
#                             "application/json": {
#                                 "schema": {
#                                     "$ref": "#/components/schemas/Erro"
#                                 }
#                             }
#                         }
#                     },
#                     "503": {
#                         "description": "Serviço indisponivel",
#                         "content": {
#                             "application/json": {
#                                 "schema": {
#                                     "$ref": "#/components/schemas/Erro"
#                                 }
#                             }
#                         }
#                     }
#                 },
#                 "operationId": "get-extrato-conta-corrente-agencia-conta",
#                 "description": "Dado um código de agência e um número de conta corrente, retorna a listagem de transações efetivadas e de lançamentos futuros, no padrão definido para API BB.",
#                 "security": [
#                     {
#                         "OAuth2-ClientCredentials": [
#                             "extrato-info"
#                         ]
#                     }
#                 ],
#                 "parameters": [
#                     {
#                         "schema": {
#                             "type": "string"
#                         },
#                         "in": "query",
#                         "name": "gw-dev-app-key",
#                         "description": "É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.",
#                         "required": true
#                     },
#                     {
#                         "schema": {
#                             "type": "integer",
#                             "minimum": 1,
#                             "maximum": 9999999,
#                             "default": 1,
#                             "format": "int32"
#                         },
#                         "in": "query",
#                         "name": "numeroPaginaSolicitacao",
#                         "description": "Número da página solicitada. Opcionalmente, quando não informado, será atribuído página 1."
#                     },
#                     {
#                         "schema": {
#                             "type": "integer",
#                             "minimum": 50,
#                             "maximum": 200,
#                             "default": 200,
#                             "format": "int32"
#                         },
#                         "in": "query",
#                         "name": "quantidadeRegistroPaginaSolicitacao",
#                         "description": "Quantidade de registros da página solicitada (pagesize). Opcionalmente, quando não informado, será atribuído pagesize 200. Pagesize máximo: 200 registros. Pagesize mínimo: 50 registros. O pagesize informado na solicitação da primeira página deverá ser mantido nos pedidos das páginas subsequentes do extrato."
#                     },
#                     {
#                         "schema": {
#                             "type": "integer",
#                             "minimum": 1010001,
#                             "maximum": 31129999,
#                             "format": "int32"
#                         },
#                         "in": "query",
#                         "name": "dataInicioSolicitacao",
#                         "description": "Data inicial do período do extrato solicitado. Formato DDMMAAAA. Limite máximo para data inicial: 5 anos a partir da data atual. Para casos onde os campos data inicial e data final não estejam preenchidos, será retornado o extrato dos últimos 30 dias. Caso o campo data inicial seja preenchido, o preenchimento do campo data final será obrigatório."
#                     },
#                     {
#                         "schema": {
#                             "type": "integer",
#                             "minimum": 1010001,
#                             "maximum": 31129999,
#                             "format": "int32"
#                         },
#                         "in": "query",
#                         "name": "dataFimSolicitacao",
#                         "description": "Data final do período do extrato solicitado. Formato DDMMAAAA. Período máximo entre a data inicial e a data final: 31 dias. Para casos onde os campos data final e data inicial não estejam preenchidos, será retornado o extrato dos últimos 30 dias. Caso o campo data final seja preenchido, o preenchimento do campo data inicial será obrigatório."
#                     }
#                 ],
#                 "tags": [
#                     "ContaCorrente"
#                 ]
#             }
#         }
#     },
#     "components": {
#         "schemas": {
#             "Erro": {
#                 "title": "Erro",
#                 "x-stoplight": {
#                     "id": "olcscxrle8y1j"
#                 },
#                 "type": "object",
#                 "description": "Representa os campos de erro de resposta do acionamento de um recurso.",
#                 "properties": {
#                     "erros": {
#                         "type": "array",
#                         "items": {
#                             "type": "object",
#                             "properties": {
#                                 "codigo": {
#                                     "type": "string",
#                                     "description": "Código da mensagem de erro.",
#                                     "example": "9999999"
#                                 },
#                                 "versao": {
#                                     "type": "string",
#                                     "description": "Versão da mensagem de erro.",
#                                     "example": "1"
#                                 },
#                                 "mensagem": {
#                                     "type": "string",
#                                     "description": "Texto da mensagem de erro.",
#                                     "example": "O campo CPF não foi informado ou está inválido"
#                                 },
#                                 "ocorrencia": {
#                                     "type": "string",
#                                     "description": "Código da ocorrência que identifica o erro internamente no BB.",
#                                     "example": "bxds-cald-a1"
#                                 }
#                             },
#                             "required": [
#                                 "codigo",
#                                 "versao",
#                                 "mensagem",
#                                 "ocorrencia"
#                             ]
#                         }
#                     }
#                 }
#             },
#             "ErrorOAuthUnauthorized": {
#                 "title": "ErrorOAuthUnauthorized",
#                 "x-stoplight": {
#                     "id": "amzh8j5ldjtf7"
#                 },
#                 "type": "object",
#                 "properties": {
#                     "statusCode": {
#                         "type": "number",
#                         "description": "Código do estado do erro."
#                     },
#                     "error": {
#                         "type": "string",
#                         "description": "Tipo do erro."
#                     },
#                     "message": {
#                         "type": "string",
#                         "description": "Mensagem do erro."
#                     },
#                     "atributes": {
#                         "type": "object",
#                         "description": "Atributos do erro.",
#                         "properties": {
#                             "error": {
#                                 "type": "string",
#                                 "description": "Mensagem do erro."
#                             }
#                         }
#                     }
#                 }
#             },
#             "ErrorOAuth": {
#                 "title": "ErrorOAuth",
#                 "x-stoplight": {
#                     "id": "46p5wi4kilw6u"
#                 },
#                 "type": "object",
#                 "description": "Representação de um objeto de erro do OAuth 2.0.",
#                 "properties": {
#                     "statusCode": {
#                         "type": "number",
#                         "description": "Código do estado do erro."
#                     },
#                     "error": {
#                         "type": "string",
#                         "description": "Tipo do erro."
#                     },
#                     "message": {
#                         "type": "string",
#                         "description": "Mensagem do erro."
#                     }
#                 }
#             }
#         },
#         "securitySchemes": {
#             "OAuth2-ClientCredentials": {
#                 "type": "oauth2",
#                 "flows": {
#                     "clientCredentials": {
#                         "tokenUrl": "https://oauth.hm.bb.com.br/oauth/token",
#                         "scopes": {
#                             "extrato-info": "Permite acionar recursos de consultas relativas à extrato."
#                         }
#                     }
#                 },
#                 "description": "Com a proteção de credenciais de usuários, o OAuth 2.0 permite a recuperação segura de recursos seguros."
#             }
#         }
#     },
#     "tags": [
#         {
#             "name": "ContaCorrente"
#         }
#     ]
# }

class ExtratoContaCorrenteBBWrapper(BaseBBWrapper):
    SANDBOX_BASE_URL = "https://api.hm.bb.com.br/extratos/v1/conta-corrente"
    BASE_URL = "https://api-extratos.bb.com.br/extratos/v1/conta-corrente"
    SCOPE = "extrato-info"

    def __init__(
        self,
        *args,
        agencia=None,
        conta=None,
        basic_token=None,
        is_sandbox=None,
        gw_app_key=None,
        **kwargs,
    ):
        super().__init__(
            *args,
            basic_token=basic_token,
            is_sandbox=is_sandbox,
            gw_app_key=gw_app_key,
            **kwargs,
        )
        if agencia is None:
            agencia = AGENCIA

        if conta is None:
            conta = CONTA
        self.__agencia = agencia
        self.__conta = conta

    # https://api.hm.bb.com.br/extratos/v1/swagger?gw-dev-app-key=b82315c0c31e0135776b005056891bef

    def consultar_extrato_conta_corrente(self, numero_pagina_solicitacao=1,
                                         quantidade_registro_pagina_solicitacao=200,
                                         data_inicio_solicitacao=None,
                                         data_fim_solicitacao=None):

        search_params = {
            "numeroPaginaSolicitacao": numero_pagina_solicitacao,
            "quantidadeRegistroPaginaSolicitacao": quantidade_registro_pagina_solicitacao,
        }
        if data_inicio_solicitacao:
            search_params["dataInicioSolicitacao"] = data_inicio_solicitacao
        if data_fim_solicitacao:
            search_params["dataFimSolicitacao"] = data_fim_solicitacao

        url = self._construct_url("agencia", self.__agencia,
                                  "conta", self.__conta, search=search_params)

        response = self._get(url)
        return response
