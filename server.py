from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    order = request.form
    print(f"Charging { order['first_name'] } { order['last_name'] } for { int(order['strawberry']) + int(order['raspberry']) + int(order['apple']) } fruits.")
    print(order)
    return render_template("checkout.html", order = order)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    