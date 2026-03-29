import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuration
STUDENTS = [
    ("S001", "Ali", "Improving"),
    ("S002", "Sara", "Consistently Weak"),
    ("S003", "Ahmed", "Inconsistent"),
    ("S004", "Zoya", "Disengaged"),
    ("S005", "Omar", "Improving"),
    ("S006", "Hiba", "Consistently Weak"),
    ("S007", "Bilal", "Improving"),
    ("S008", "Noor", "Inconsistent"),
    ("S009", "Mustafa", "Disengaged"),
    ("S010", "Ayesha", "Improving"),
]

SUBJECTS = ["English", "Math", "Science"]
TOPICS = {
    "English": ["Reading", "Writing", "Speaking"],
    "Math": ["Fractions", "Algebra", "Geometry"],
    "Science": ["Physics", "Biology", "Chemistry"]
}

START_DATE = datetime(2026, 1, 1)

def generate_score(behavior, week):
    if behavior == "Improving":
        # Start low (needs intervention), then improve (action loop)
        if week < 3:
            return random.randint(40, 55)
        else:
            base = 60 + ((week - 3) * 5)
            return min(100, int(base + random.randint(-5, 5)))
    elif behavior == "Consistently Weak":
        # Always low, triggers "Immediate Attention"
        return random.randint(35, 48)
    elif behavior == "Inconsistent":
        # High variance
        return random.randint(40, 95)
    elif behavior == "Disengaged":
        # Generally low, low effort
        return random.randint(20, 50)
    return 70

def generate_attempts(behavior, score):
    if behavior == "Consistently Weak":
        return random.randint(4, 6) # High effort, still weak -> Immediate Attention
    elif behavior == "Disengaged":
        return random.randint(1, 2) # Low effort
    return random.randint(1, 3)

def generate_data():
    data = []
    for student_id, name, behavior in STUDENTS:
        for week in range(12):
            subject = random.choice(SUBJECTS)
            topic = random.choice(TOPICS[subject])
            score = generate_score(behavior, week)
            attempts = generate_attempts(behavior, score)
            time_spent = attempts * random.randint(15, 30)
            date = (START_DATE + timedelta(weeks=week)).strftime("%Y-%m-%d")
            
            data.append([
                student_id, name, 10, 5, subject, topic, score, attempts, time_spent, date
            ])
            
    df = pd.DataFrame(data, columns=[
        "Student_ID", "Name", "Age", "Grade", "Subject", "Topic", "Score", "Attempts", "Time_Spent", "Date"
    ])
    df.to_csv("data.csv", index=False)
    print(f"Generated data.csv with {len(df)} rows.")

if __name__ == "__main__":
    generate_data()
