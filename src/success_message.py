from enum import Enum

class SuccessMessage(Enum):
    new_user = "Usuário criado com sucesso"
    login = "Login feito com sucesso"
    valid_token = "Token é valido"
    new_community = "Comunidade Criada com sucesso"
    new_identified_post ="Post criado com sucesso"
    new_community_post ="Post criado com sucesso"
    new_interaction = "Interação criado com sucesso"
    