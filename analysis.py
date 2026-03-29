import pandas as pd
import numpy as np
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI Client (Graceful handling for missing key)
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None

def calculate_priority(df):
    """Calculates a weighted priority score: (60 - Score) * 0.6 + Attempts * 0.4"""
    df = df.copy()
    df["priority_score"] = (60 - df["Score"]) * 0.6 + df["Attempts"] * 0.4
    # Sort by priority, then by score (descending priority)
    return df.sort_values(by="priority_score", ascending=False)

def calculate_urgency(row):
    """Flags 'Immediate Attention' if Score < 50 and Attempts > 3"""
    if row["Score"] < 50 and row["Attempts"] > 3:
        return "🚨 Immediate Attention"
    return "Normal"

def predict_risk(row):
    """Predicts 'At Risk' status before total failure (Score < 60 and Attempts >= 2)"""
    if row["Score"] < 60 and row["Attempts"] >= 2:
        return "At Risk"
    return "Stable"

def calculate_improvement_rate(df):
    """Measures the percentage of learning paths (Student+Topic) showing improvement over time."""
    improved = 0
    total = 0
    
    # Sort by date for chronological comparison
    df_sorted = df.sort_values("Date")
    grouped = df_sorted.groupby(["Student_ID", "Topic"])
    
    for _, group in grouped:
        scores = group["Score"].values
        if len(scores) > 1:
            total += 1
            if scores[-1] > scores[0]:
                improved += 1
                
    return (improved / total) * 100 if total > 0 else 0

def calculate_consistency(df):
    """Calculates score stability via Standard Deviation. High SD = Unstable."""
    # Group by student and calculate std
    stability = df.groupby("Name")["Score"].std().reset_index()
    stability.columns = ["Name", "Score_Std"]
    return stability

def track_intervention_impact(student_df):
    """Checks if the most recent score improved compared to the first recorded score in the same topic."""
    results = []
    for topic in student_df["Topic"].unique():
        topic_data = student_df[student_df["Topic"] == topic].sort_values("Date")
        scores = topic_data["Score"].values
        if len(scores) > 1:
            status = "Improving" if scores[-1] > scores[0] else "No Progress"
            results.append({"Topic": topic, "Result": status})
    return pd.DataFrame(results)

def get_cohort_insights(df):
    """Identifies system-level bottlenecks: the weakest subject overall."""
    subject_avg = df.groupby("Subject")["Score"].mean()
    weakest_subject = subject_avg.idxmin()
    weak_score = subject_avg.min()
    return weakest_subject, weak_score

def generate_insights(df):
    """Aggregates high-level summaries for the 'Insights Engine'."""
    insights = []
    
    # Subject-level weakness
    weak_subjects = df[df["Score"] < 60]["Subject"].value_counts()
    for subject, count in weak_subjects.items():
        insights.append(f"High weakness detected in {subject} ({count} cases tracked)")
        
    return insights

def get_ai_recommendation(student_data):
    """Structured AI prompt for a technical improvement plan."""
    if not client or not os.getenv("OPENAI_API_KEY"):
        return "Mock AI: Focus on topic-specific practice sets and increase study time by 20%."
        
    prompt = f"""
    You are an academic coach. Analyze this data:
    Subject: {student_data['Subject']}
    Topic: {student_data['Topic']}
    Score: {student_data['Score']}%
    Attempts: {student_data['Attempts']}
    
    Classify the issue:
    1. Knowledge gap OR
    2. Lack of engagement
    
    Then provide:
    - Root cause
    - 2 actionable interventions
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error: {str(e)}"

def get_coaching_script(student_data):
    """Friendly AI simulation for a live coaching call."""
    if not client or not os.getenv("OPENAI_API_KEY"):
        return "Hey there! I noticed you're working hard on Fractions. Let's try breaking the problems down into smaller steps together. You've got this!"

    prompt = f"""
    You are a friendly academic coach speaking directly to a student named {student_data['Name']}.
    
    Student scored {student_data['Score']}% in {student_data['Topic']}.
    They used {student_data['Attempts']} attempts.
    
    Explain the issue in a simple, motivating way and guide them on what to do next. Be encouraging and human-like.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Coaching Script Error: {str(e)}"
