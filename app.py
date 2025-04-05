from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Word lists
adjectives = ["Cool", "Fast", "Happy", "Lazy", "Smart", "Clever", "Brave", "Witty"]
nouns = ["Tiger", "Eagle", "Shark", "Panda", "Lion", "Wolf", "Falcon", "Bear"]

def generate_username(include_number, include_special, max_length):
    username = random.choice(adjectives) + random.choice(nouns)

    if include_number:
        username += str(random.randint(0, 999))
    if include_special:
        username += random.choice("!@#$%^&*")

    if max_length and max_length.isdigit():
        username = username[:int(max_length)]

    return username

@app.route("/", methods=["GET", "POST"])
def index():
    username = ""
    if request.method == "POST":
        include_number = 'include_number' in request.form
        include_special = 'include_special' in request.form
        max_length = request.form.get("length", "")

        username = generate_username(include_number, include_special, max_length)

        if 'save' in request.form:
            with open("usernames.txt", "a") as file:
                file.write(username + "\n")

    return render_template("index.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
