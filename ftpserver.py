from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
#authorizer.add_user("Your User ID", "Your Password", "Location for Storage", perm="elradfmw")
authorizer.add_user("user1", "rudra@kiranm", "F:\Share", perm="elradfmw")
authorizer.add_user("user2", "rudra@suryad", "F:\Share", perm="elradfmw")
authorizer.add_user("user3", "rudra@saim", "F:\Share", perm="elradfmw")
authorizer.add_user("user4", "rudra@rexlinp", "F:\Share", perm="elradfmw")
authorizer.add_user("user5", "rudra@phanip", "F:\Share", perm="elradfmw")
authorizer.add_user("user6", "rudra@yamunak", "F:\Share", perm="elradfmw")
authorizer.add_user("user7", "rudra@chaituk", "F:\Share", perm="elradfmw")
authorizer.add_user("user8", "rudra@chaitukv", "F:\BackUp", perm="elradfmw")


handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 2121), handler)
server.serve_forever()
