from time import sleep

import webapp2
from webapp2_extras.users import users
from webapp2_extras import jinja2


from model.coctel import Coctel
from model.coctel import Alcohol
from model.coctel import Dificultad
import model.user as user_model


class NuevoCoctelHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("add_coctel.html"))




    def post(self):
        self.response.write("Formulario recibido, anhadiendo coctel")
        nombre = self.request.get("addNombre", "falta nombre")
        ingredientes = self.request.get("addIngredientes", "falta ingredientes")
        pasos = self.request.get("addPasos", "falta pasos")

        str_alcohol = self.request.get("addAlcohol", "falta alcohol")
        str_dificultad = self.request.get("addDificultad", "falta dificultad")
        usr = users.get_current_user()
        user = user_model.retrieve(usr)

        alcohol = Alcohol.get(str_alcohol)
        dificultad = Dificultad.get(str_dificultad)

        #If comprobaciones, redirigir si algo va mal
        if not(nombre) or not(ingredientes) or not(pasos) or not(dificultad) or not(alcohol) or not(user):
            return self.redirect("/")
        else:
            coctel = Coctel(nombre=nombre, ingredientes=ingredientes, pasos=pasos, dificultad=dificultad, alcohol=alcohol, usr_email=user.email)
            coctel.put()
            sleep(1)
            return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/coctel/nuevo', NuevoCoctelHandler)
], debug=True)