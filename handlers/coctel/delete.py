from time import sleep

import webapp2


from model.coctel import Coctel


class EliminaCoctelHandler(webapp2.RequestHandler):
    def get(self):
        coctel = Coctel.recupera(self.request)
        coctel.key.delete()
        sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/coctel/elimina', EliminaCoctelHandler)
], debug=True)