from fasthtml.common import *
from monsterui.all import *


app, rt = fast_app(hdrs=(Theme.blue.headers()))


@app.get("/")
def index():
    return H1("Hello World!!!")


serve()
