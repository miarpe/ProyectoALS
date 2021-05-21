from google.appengine.ext import ndb
from google.appengine.api import users



class User(ndb.Model):

    added = ndb.DateProperty(auto_now_add=True, indexed=True)
    email = ndb.TextProperty(indexed=True)
    nick = ndb.TextProperty(indexed=True)

    def __str__(self):
        return " (" + self.email + ")"

    def __unicode__(self):
        return ": " + self.nick + " (" + self.email + ")"


def create(usr):
    toret = User()

    toret.email = usr.email()
    toret.nick = usr.nickname()

    return toret


def create_empty_user():
    return User(email="", nick="")


@ndb.transactional
def update(user):
    return user.put()


def retrieve(usr):
    toret = None

    if usr:
        usr_email = usr.email()
        found_users = User.query(User.email == usr_email).order(-User.added)

        if found_users.count() == 0:
            toret = create(usr)
            update(toret)
        else:
            toret = found_users.iter().next()
            toret.usr = usr

    return toret