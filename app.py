from flask import Flask, render_template, request
from model import diagnose  # Import your diagnosis function from model.py

app = Flask(__name__)


# Route to render the HTML form
@app.route('/')
def home():
    return render_template('index.html')


# Route to handle form submission and display results
@app.route('/diagnose', methods=['GET'])
def diagnosis():
    # Get user input from the form
    symptoms = request.form['symptoms']  # Assuming "symptoms" is the input field name

    # Use your medical diagnosis system to predict based on the input
    result = diagnose(symptoms)  # Replace with your logic (from "model.py")

    # Return the diagnosis result to the user
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
def diagnose(symptoms):
    # Example logic for diagnosis based on symptoms
    symptoms = symptoms.lower()
    if "fever" in symptoms and "cough" in symptoms:
        return "You might have the flu."
    elif "chest pain" in symptoms:
        return "It could be a cardiac issue. Please consult a doctor."
    else:
        return "Symptoms unknown. More tests are recommended."
