from flask import Flask, render_template
from models import MenuItem
from inventory import get_low_stock

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/menu")
def menu():
    return render_template("menu.html", menu_items=MenuItem.get_all())


@app.route("/inventory")
def inventory():
    return render_template("inventory.html", low_stock=get_low_stock())


@app.route("/reports")
def reports():
    return render_template("reports.html")


if __name__ == "__main__":
    app.run(debug=True)