from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open("model.sav", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            age = int(request.form["age"])
            gender = int(request.form["gender"])  # 0=Female, 1=Male
            height = float(request.form["height"])
            weight = float(request.form["weight"])
            cholesterol = float(request.form["cholesterol"])
            glucose = float(request.form["glucose"])
            smoker = int(request.form["smoker"])  # 0=No, 1=Yes
            exercise = float(request.form["exercise"])
            systolic = float(request.form["systolic"])
            diastolic = float(request.form["diastolic"])

            input_data = np.array([[age, gender, height, weight, cholesterol,
                                    glucose, smoker, exercise, systolic, diastolic]])

            prediction = model.predict(input_data)[0]

            result = "⚠️ High Risk of Heart Disease" if prediction == 1 else "✅ Low Risk of Heart Disease"

        except Exception as e:
            result = f"Error: {str(e)}"

        return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run()

