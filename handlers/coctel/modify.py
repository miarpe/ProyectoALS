from time import sleep

import webapp2
from webapp2_extras import jinja2


from model.coctel import Coctel
from model.coctel import Alcohol
from model.coctel import Dificultad

class ModificaCoctelHandler(webapp2.RequestHandler):
    def get(self):
        coctel = Coctel.recupera(self.request)

        valores_plantilla = {
            "coctel": coctel
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("modify_coctel.html", **valores_plantilla))

    def post(self):
        self.response.write("Formulario recibido, modificando coctel")
        nombre = self.request.get("modifyNombre", "falta nombre")
        ingredientes = self.request.get("modifyIngredientes", "falta ingredientes")
        pasos = self.request.get("modifyPasos", "falta pasos")

        str_alcohol = self.request.get("modifyAlcohol", "falta alcohol")
        str_dificultad = self.request.get("modifyDificultad", "falta dificultad")

        alcohol = Alcohol.get(str_alcohol)
        dificultad = Dificultad.get(str_dificultad)


        if not(nombre) or not(ingredientes) or not(pasos) or not(dificultad) or not(alcohol):
            return self.redirect("/")
        else:
            coctel = Coctel.recupera(self.request)
            coctel.nombre = nombre
            coctel.ingredientes = ingredientes
            coctel.pasos = pasos
            coctel.alcohol = alcohol
            coctel.dificultad = dificultad

            coctel.put()
            sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/coctel/modifica', ModificaCoctelHandler)
], debug=True)