from blogs import db,create_app
from blogs.models import Users
app = create_app()
app_cont = app.app_context()
app_cont.push()
db.drop_all()
db.create_all()