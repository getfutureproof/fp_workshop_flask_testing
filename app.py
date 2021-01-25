from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

gifs = [
    "http://i.stack.imgur.com/SBv4T.gif",
    "http://i.stack.imgur.com/SBv4T.gif",
    "http://i.stack.imgur.com/SBv4T.gif",
    "http://i.stack.imgur.com/SBv4T.gif",
]


@app.route("/")
def homepage():
    return "You are successfully connected to the server."


@app.route("/gifs/html", methods=["GET"])
def gifs_html_index():
    return render_template(
        "gifs_index.ejs",
        gifs=gifs,
        date="19th Jan",
        temperature="20 celcius"
    )


@app.route("/gifs/json", methods=["GET"])
def gifs_json_index():
    return jsonify({"gifs": gifs})


@app.route("/like", methods=['POST', 'PATCH', 'DELETE', 'PUT'])
def like_gif():
    post_data = request.get_json()
    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True)
