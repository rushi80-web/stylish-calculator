from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form.get("num2", 0))
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = "❌ Cannot divide by zero" if num2 == 0 else num1 / num2
            elif operation == "modulus":
                result = num1 % num2
            elif operation == "power":
                result = math.pow(num1, num2)
            elif operation == "sqrt":
                result = "❌ Invalid input for √" if num1 < 0 else math.sqrt(num1)
        except ValueError:
            result = "❌ Invalid input. Please enter numbers."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
