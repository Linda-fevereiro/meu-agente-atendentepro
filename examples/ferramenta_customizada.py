
# Exemplo: Como criar uma ferramenta (Tool) customizada
# Salve isso em client_templates/standard/tools.py se quiser usar.

from agents import tool

@tool
def consultar_status_pedido(id_pedido: str) -> str:
    '''
    Verifica onde está o pedido do cliente.
    Args:
        id_pedido: O código do pedido (ex: PED-123).
    '''
    # Simulação de banco de dados
    if id_pedido == "123":
        return "Seu pedido saiu para entrega hoje!"
    return "Pedido não encontrado."
