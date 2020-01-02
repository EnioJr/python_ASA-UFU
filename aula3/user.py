class User:
    _id = None
    _none = None
    _idade = None
    _cidade = None

    def __init__(self, id, nome, idade, cidade):
        self._id = id
        self._nome = nome
        self._idade = idade
        self._cidade = cidade

    def getUserId(self):
        return self._id

    def getUserNome(self):
        return self._nome

    def getUserIdade(self):
        return self._idade

    def getUserCidade(self):
        return self._cidade
    
    def getUserName(self, id):
        retorno = ""
        if(self._id == id):
            retorno = self._nome
        else:
            retorno = "usuario nao encontrado"
        return (retorno)