from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)


@app.route('/add')
def do_add():
    """ add a and b params"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route('/sub')
def do_sub():
    """subtract b from a"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)

@app.route('/mult')
def do_mult():
    """multiply a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)

@app.route('/div')
def do_div():
    """divide a by b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

