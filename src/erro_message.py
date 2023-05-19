from enum import Enum

class ErrorMessage(Enum):
    user_not_exist = "Usuário Inexistente"
    public_id_not_exist = "ID publico não exite"
    there_not_existent_users = "Não a nenhum usuário cadastrado"
    email_already_exist = "Email ja utilizado"
    pseudonym_already_exist = "Pseudoanônimo ja utilizado"
    internal_error = "Erro do servidor"
    failed_login = "Email ou senha Incorreto"
    invalid_token = "Token  não é valido"
