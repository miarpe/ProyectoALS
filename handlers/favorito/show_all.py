import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.coctel import Coctel
import model.user as user_model
import model.favorito as favorito_model


class ShowAllHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        user = user_model.retrieve(usr)

        if usr and user:
            usr_url = users.create_logout_url("/")

            cocteles = Coctel.query().order()

            coctelesfav = favorito_model.get_favoritos(user.email)
            favlist = []
            for bebida in coctelesfav:
                favlist.append(bebida.coctel.urlsafe())

            valores_plantilla = {
                "cocteles": cocteles,
                "usr": usr,
                "user": user,
                "usr_url": usr_url,
                "favlist": favlist
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("show_all_fav.html", **valores_plantilla))
        else:
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/fav/show_all', ShowAllHandler)
], debug=True)
