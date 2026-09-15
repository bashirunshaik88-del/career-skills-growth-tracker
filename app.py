import streamlit as st

st.title("Career Skills Growth Tracker")
st.write("Welcome to the app!")
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

skills = []


@app.route("/")
def home():
    return render_template("index.html", skills=skills)


@app.route("/add_skill", methods=["POST"])
def add_skill():

    skill = request.form["skill"]
    category = request.form["category"]
    level = request.form["level"]
    progress = int(request.form["progress"])

    skills.append({
        "skill": skill,
        "category": category,
        "level": level,
        "progress": progress
    })

    return redirect("/")


@app.route("/decision", methods=["POST"])
def decision():

    option_a = request.form["option_a"]
    option_b = request.form["option_b"]

    ratings = {
        "python": 9.0,
        "java": 8.5,
        "c": 7.5,
        "c++": 8.0,
        "javascript": 9.0,
        "html": 8.5,
        "css": 8.0,
        "machine learning": 9.5,
        "sql": 9.0,
        "aws": 9.0,
        "azure": 8.5
    }

    rating_a = ratings.get(option_a.lower(), 7.0)
    rating_b = ratings.get(option_b.lower(), 7.0)

    if rating_a > rating_b:
        result = f"🏆 {option_a} has a higher industry rating."

    elif rating_b > rating_a:
        result = f"🏆 {option_b} has a higher industry rating."

    else:
        result = "🤝 Both options have the same industry rating."

    return render_template(
        "index.html",
        skills=skills,
        decision_result=f"""
        {option_a}: {rating_a}/10 ⭐
        <br>
        {option_b}: {rating_b}/10 ⭐
        <br><br>
        {result}
        """
    )

@app.route("/quiz", methods=["POST"])
def quiz():

    answers = {
        "q0": "Artificial Intelligence",
        "q1": "Python",
        "q2": "Using remote servers over the internet"
    }

    score = 0

    for question, correct_answer in answers.items():

        if request.form.get(question) == correct_answer:
            score += 1

    return render_template(
        "index.html",
        skills=skills,
        quiz_score=score,
        quiz_total=len(answers)
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8501, debug=False, use_reloader=False)
