from google.appengine.ext import ndb
from coctel import Coctel


class Favorito(ndb.Model):
    usr_email = ndb.StringProperty(indexed=True)
    coctel = ndb.KeyProperty(kind=Coctel, required=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id=""

        return ndb.Key(urlsafe=id).get()


def favorito(favorito):
    query = Favorito.query(Favorito.usr_email == favorito.usr_email, Favorito.coctel == favorito.coctel).get()
    if query is None:
        favorito.put()
        return True
    else:
        return False


def no_favorito(favorito):
    query = Favorito.query(Favorito.usr_email == favorito.usr_email, Favorito.coctel == favorito.coctel).get()
    if query is not None:
        query.key.delete()
        return True
    else:
        return False


def get_favoritos(email):
    return Favorito.query(Favorito.usr_email == email)
