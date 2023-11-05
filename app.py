import pickle
from flask import Flask, request, render_template

app = Flask(__name__) #Create a flask app

model = pickle.load(open("svc.pkl", 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        try:
            length_s = float(request.form.get("length_s"))
            width_s = float(request.form.get("width_s"))
            length_p = float(request.form.get("length_p"))
            width_p = float(request.form.get("width_p"))

            pred = model.predict([[length_s, width_s, length_p, width_p]])[0]

            if pred == 1:
                prediction = "Iris-sertosa"
            elif pred == 2:
                prediction = "Iris-versicolor"
            else:
                prediction = "Iris-virginica"
            return render_template("index.html", pred=prediction)

        except:
            return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)