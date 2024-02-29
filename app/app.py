from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def load_users():

  users = {}
  with open("registros.txt", "r") as f:
    for line in f:
      username, password = line.strip().split(",")
      users[username] = password
  return users

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        contrasena = request.form["contrasena"]

        with open("registros.txt", "a") as f:
            f.write(f"{nombre},{contrasena}\n")

        return render_template("exito.html")
    else:
        return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
  users = load_users()  
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username] == password:
      return render_template("bienvenido.html", nombre=username)
    else:
      return render_template("login.html", error="Usuario o contraseña incorrectos")
  else:
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
