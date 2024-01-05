from flask import Flask

app = Flask(__name__)
my_guess= 7

@app.route("/")
def hello_world():
    return "<h1>Hello, User!</h1>"\
            "<p>Guess my number!</p>" \

@app.route('/guess/<int:number>')
def guess(number):
    if number < my_guess:
        return "Your guess is too low!"
    elif number > my_guess:
        return "Your guess is too high!"
    elif number==my_guess:
        return "Congratulations!"
    else:
        return "Sorry, you entered false format."


if __name__ == "__main__":
    app.run(debug=True)
