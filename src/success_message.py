from enum import Enum

class SuccessMessage(Enum):
    new_user = "Usuário criado com sucesso"
    login = "Login feito com sucesso"
    valid_token = "Token é valido"
    