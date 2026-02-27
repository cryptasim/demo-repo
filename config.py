DEBUG=True
DATABASE_URL="sqlite:///test.db"
SECRET_KEY=   "supersecret"


def get_config():
 return {
 "debug":DEBUG,
 "database":DATABASE_URL,
 }
