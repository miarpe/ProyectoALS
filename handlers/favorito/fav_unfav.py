import webapp2
import time
from webapp2_extras.users import users


from model.coctel import Coctel
from model.favorito import Favorito
import model.user as user_model
import model.favorito as favorito_model

class FavUnfavHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        user = user_model.retrieve(usr)

        if usr and user:
            fav = Favorito()
            fav.usr_email = user.email
            fav.coctel = Coctel.recupera(self.request).key

            if favorito_model.favorito(fav):
                time.sleep(1)
                return self.redirect("/")
            elif favorito_model.no_favorito(fav):
                time.sleep(1)
                return self.redirect("/")
            else:
                time.sleep(1)
                return self.redirect("/")
        else:
            time.sleep(1)
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/fav/fav_unfav', FavUnfavHandler)
], debug=True)
