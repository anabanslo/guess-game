import random
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    secret_number = request.cookies.get("secret_number")

    response = make_response(render_template("index.html"))
    if not secret_number:
        new_secret = random.randint(1, 10)
        response.set_cookie("secret_number", str(new_secret))

    return response

@app.route("/result", methods=["POST"])
def result():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        message = "Correct!".format(secret_number)
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 10)))
        return response
    elif guess > secret_number:
        message = "Wrong! Smaller!"
        return render_template("result.html", message=message)
    elif guess < secret_number:
        message = "Wrong! Bigger!"
        return render_template("result.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)