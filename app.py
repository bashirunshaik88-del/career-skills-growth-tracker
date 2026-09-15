import streamlit as st

st.set_page_config(
    page_title="AI Career & Skills Growth Tracker", layout="centered"
)

# --- HEADER ---
st.title("🚀 AI Career & Skills Growth Tracker")
st.caption("Track your skills. Improve your career. Grow every day.")

# Initialize Session State
if "skills" not in st.session_state:
    st.session_state.skills = []

# --- 1. DASHBOARD SECTION ---
st.header("📊 Dashboard")

total_skills = len(st.session_state.skills)
completed_skills = sum(
    1 for s in st.session_state.skills if s.get("progress") == 100
)
avg_progress = (
    round(
        sum(s.get("progress", 0) for s in st.session_state.skills)
        / total_skills,
        1,
    )
    if total_skills > 0
    else 0.0
)

col1, col2, col3 = st.columns(3)
col1.metric("Total Skills", total_skills)
col2.metric("Completed Skills", completed_skills)
col3.metric("Average Progress", f"{avg_progress}%")

st.divider()

# --- 2. SKILL & GOAL TRACKER ---
st.header("🎯 Skill & Goal Tracker")

with st.form("add_skill_form", clear_on_submit=True):
    col_a, col_b = st.columns(2)
    with col_a:
        skill_name = st.text_input("Skill Name", placeholder="e.g. Python")
        level = st.selectbox(
            "Level", ["Beginner", "Intermediate", "Advanced"]
        )
    with col_b:
        category = st.text_input("Category", placeholder="e.g. Data Science")
        progress = st.number_input(
            "Progress %", min_value=0, max_value=100, value=0
        )

    submit_skill = st.form_submit_button("Add Skill")

if submit_skill and skill_name and category:
    st.session_state.skills.append(
        {
            "skill": skill_name,
            "category": category,
            "level": level,
            "progress": int(progress),
        }
    )
    st.rerun()

st.subheader("My Skills")
if st.session_state.skills:
    for item in st.session_state.skills:
        st.write(
            f"**{item['skill']}** ({item['level']}) - Category: {item['category']}"
        )
        st.progress(item["progress"] / 100)
else:
    st.write("No skills added yet.")

st.divider()

# --- 3. DECISION SUPPORT ---
st.header("⚖️ Job / Course Decision Support")
st.write("Enter two technologies, courses, or career options to compare.")

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
    "azure": 8.5,
}

col_opt1, col_opt2 = st.columns(2)
with col_opt1:
    option_a = st.text_input("Option A", placeholder="e.g. Java")
with col_opt2:
    option_b = st.text_input("Option B", placeholder="e.g. Python")

if st.button("🤖 Compare with AI"):
    if option_a and option_b:
        rating_a = ratings.get(option_a.lower(), 7.0)
        rating_b = ratings.get(option_b.lower(), 7.0)

        st.write(f"**{option_a}:** {rating_a}/10 ⭐")
        st.write(f"**{option_b}:** {rating_b}/10 ⭐")

        if rating_a > rating_b:
            st.success(f"🏆 {option_a} has a higher industry rating.")
        elif rating_b > rating_a:
            st.success(f"🏆 {option_b} has a higher industry rating.")
        else:
            st.info("🤝 Both options have the same industry rating.")

st.divider()

# --- 4. INTERVIEW PRACTICE ---
st.header("🎤 Interview Practice")
st.write("Select the role and technology you want to practice.")

role = st.selectbox(
    "Job Role",
    [
        "Select Role",
        "Python Developer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Web Developer",
        "Java Developer",
    ],
)
technology = st.selectbox(
    "Technology",
    [
        "Select Technology",
        "Python",
        "Java",
        "SQL",
        "HTML / CSS / JavaScript",
        "Machine Learning",
    ],
)

if st.button("Start Interview"):
    questions = []
    if role == "Python Developer" and technology == "Python":
        questions = [
            "What are the main features of Python?",
            "Explain the difference between a list and a tuple.",
            "What is Object-Oriented Programming in Python?",
        ]
    elif role == "Machine Learning Engineer" and technology == "Machine Learning":
        questions = [
            "What is Machine Learning?",
            "What is the difference between supervised and unsupervised learning?",
            "What is overfitting and how can you prevent it?",
        ]
    elif role == "Data Scientist" and technology == "SQL":
        questions = [
            "What is SQL?",
            "What is the difference between WHERE and HAVING?",
            "Explain INNER JOIN with an example.",
        ]
    elif role == "Web Developer" and technology == "HTML / CSS / JavaScript":
        questions = [
            "What is the DOM in JavaScript?",
            "What is the difference between let, var and const?",
            "What is responsive web design?",
        ]
    elif role == "Java Developer" and technology == "Java":
        questions = [
            "What are the main features of Java?",
            "Explain inheritance in Java.",
            "What is the difference between JDK, JRE and JVM?",
        ]
    else:
        questions = [
            "Tell me about yourself.",
            "Why are you interested in this technology?",
            "What projects have you worked on?",
        ]

    st.session_state.current_questions = questions

if "current_questions" in st.session_state:
    st.subheader("Interview Questions")
    for idx, q in enumerate(st.session_state.current_questions, start=1):
        st.write(f"**Question {idx}:** {q}")
        st.text_area(
            f"Your Answer for Question {idx}:",
            key=f"interview_ans_{idx}",
            height=80,
        )

st.divider()

# --- 5. TECH QUIZ ---
st.header("💻 Tech Literacy Quiz")

with st.form("quiz_form"):
    q0 = st.radio(
        "1. What does AI stand for?",
        [
            "Artificial Intelligence",
            "Automated Internet",
            "Advanced Information",
        ],
    )
    q1 = st.radio(
        "2. Which language is commonly used in Machine Learning?",
        ["Python", "HTML", "CSS"],
    )
    q2 = st.radio(
        "3. What is Cloud Computing?",
        [
            "Using remote servers over the internet",
            "Writing HTML",
            "Editing images",
        ],
    )

    quiz_submitted = st.form_submit_button("Submit Quiz")

    if quiz_submitted:
        score = 0
        if q0 == "Artificial Intelligence":
            score += 1
        if q1 == "Python":
            score += 1
        if q2 == "Using remote servers over the internet":
            score += 1

        total = 3
        percent = round((score / total) * 100, 1)

        st.success(f"🎉 Quiz Result: You scored **{score} / {total}** ({percent}%)")

# --- FOOTER ---
st.caption("AI-Powered Career & Skills Growth Tracker | CSE-AIML Mini Project")