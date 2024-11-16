from flask import Flask, request

app = Flask(__name__)

calculate_area = lambda base, height : (base * height) / 2

@app.route("/")
def index():
    return '''
    <form action="/submit" method="POST">

        <label for="base">Enter the base:</label>
        <input type="text" id="base" name="base">

        <label for="height">Enter the height:</label>
        <input type="text" id="height" name="height">

        <button type="submit">Submit</button>
    </form>
    '''

@app.route("/submit", methods=["POST"])
def submit():
    base = float(request.form.get("base"))
    height = float(request.form.get("height"))
    area = calculate_area(base, height)
    return f"<p>You entered: {area}</p>"
app.run()
