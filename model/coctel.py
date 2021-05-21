from google.appengine.ext import ndb
import inspect

class Alcohol:
    GINEBRA = "GINEBRA"
    VODKA = "VODKA"
    RON = "RON"
    WHISKEY = "WHISKEY"
    OTRO = "OTRO"

    @staticmethod
    def get(str_alcohol):
        if str_alcohol == "GINEBRA":
            return Alcohol.GINEBRA
        elif str_alcohol == "VODKA":
            return Alcohol.VODKA
        elif str_alcohol == "RON":
            return Alcohol.RON
        elif str_alcohol == "WHISKEY":
            return Alcohol.WHISKEY
        else:
            return Alcohol.OTRO


class Dificultad:
    FACIL = "FACIL"
    MEDIO = "MEDIO"
    DIFICIL = "DIFICIL"

    @staticmethod
    def get(dificultad):
        if dificultad=="FACIL":
            return Dificultad.FACIL
        elif dificultad=="MEDIO":
            return Dificultad.MEDIO
        else:
            return Dificultad.DIFICIL


class Coctel(ndb.Model):
    nombre = ndb.StringProperty(indexed=True)
    ingredientes = ndb.TextProperty(required=True)
    pasos = ndb.TextProperty(required=True)
    alcohol = ndb.StringProperty(required=True)
    dificultad = ndb.StringProperty(required=True)
    usr_email = ndb.StringProperty(required=True)

    @staticmethod
    def recupera(req):

        try:
            id = req.GET["id"]
        except KeyError:
            id=""

        return ndb.Key(urlsafe=id).get()
