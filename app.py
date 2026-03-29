import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from analysis import (
    calculate_priority, 
    calculate_urgency, 
    predict_risk, 
    calculate_improvement_rate, 
    calculate_consistency, 
    track_intervention_impact, 
    get_cohort_insights, 
    generate_insights, 
    get_ai_recommendation, 
    get_coaching_script
)

# Page configuration for a professional wide layout (MUST BE FIRST)
st.set_page_config(
    page_title="AI Student Insights | Elite Office", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# (Tour state removed - now using vanilla JS system)

# --- Elite Office Dark Theme (Properly Injected CSS) ---
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
    
    <style>
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        background-color: #0f172a !important; /* Deep Navy Dark */
        color: #f8fafc !important;
    }
    
    /* Premium Floating Hover Card (Tooltip Style) */
    .hint-bubble {
        position: relative;
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.95) 0%, rgba(147, 51, 234, 0.95) 100%);
        backdrop-filter: blur(12px);
        padding: 20px 24px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
        margin-bottom: 24px;
        z-index: 9999;
        animation: floatAnim 3s ease-in-out infinite;
    }
    
    /* The Pointer (Arrow) */
    .hint-bubble::after {
        content: "";
        position: absolute;
        bottom: -15px;
        left: 40px;
        border-width: 15px 15px 0;
        border-style: solid;
        border-color: rgba(147, 51, 234, 0.95) transparent transparent;
    }

    @keyframes floatAnim {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }
    
    .hint-title { font-weight: 700; color: white; font-size: 1.1rem; margin-bottom: 8px; font-family: 'Outfit'; }
    .hint-content { color: rgba(255, 255, 255, 0.95); font-size: 0.95rem; line-height: 1.5; }

    /* Layout Selection Style */
    .spotlight-active { border: 2px solid #6366f1; border-radius: 16px; padding: 10px; }

    /* Main App Container */
    .stApp { background: #0f172a !important; }
    .premium-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        padding: 24px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 24px;
    }

    h1, h2, h3 { font-family: 'Outfit', sans-serif !important; font-weight: 700 !important; color: #f8fafc !important; }

    .metric-box { background: rgba(51, 65, 85, 0.5); border-radius: 12px; padding: 20px; text-align: center; border: 1px solid rgba(255, 255, 255, 0.05); }
    .metric-title { font-size: 0.85rem; font-weight: 600; color: #94a3b8; text-transform: uppercase;}
    .metric-main { font-size: 2.2rem; font-weight: 700; color: #6366f1; }
    
    #MainMenu, footer, header {visibility: hidden;}

    </style>
""", unsafe_allow_html=True)

# (Legacy tour helper functions removed)

# Helper for loading data
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

# --- Main Layout ---

# Constant Header
st.markdown("""
<div id="step-header" class="premium-card">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div style="position: relative;">
            <h1 style="margin:0; font-size: 2.5rem;">🎓 Elite Student Insight Engine</h1>
            <p style="margin: 8px 0 0 0; color: #94a3b8; font-size: 1.1rem;">Predictive Analytics • Behavioral Mapping • Intervention Management</p>
        </div>
        <div style="background: rgba(99, 102, 241, 0.15); padding: 12px 24px; border-radius: 12px; border: 1px solid rgba(99, 102, 241, 0.3);">
            <span style="color: #818cf8; font-weight: 700; font-size: 0.9rem;">ENTERPRISE EDITION</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# (Old hint card logic removed)

# 1. Health Dashboard
st.markdown("""
<div style="margin-bottom: 24px;">
    <h2 style="margin: 0; font-size: 1.8rem;">🏢 System-Wide Learning Health</h2>
    <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 0.95rem;">High-level summary of proficiency and growth velocity across all learning cohorts.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div style="margin-bottom: 24px;">
    <h2 style="margin: 0; font-size: 1.8rem;">🏢 System-Wide Learning Health</h2>
    <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 0.95rem;">High-level summary of proficiency and growth velocity across all learning cohorts.</p>
</div>
""", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
avg_score = df["Score"].mean()
growth_rate = calculate_improvement_rate(df)
bottleneck_subj, bottleneck_score = get_cohort_insights(df)
weak_count = len(df[df["Score"] < 60])
with m1:
    st.markdown(f"""<div class="metric-box"><div class="metric-title">Mean Proficiency</div><div class="metric-main">{avg_score:.1f}%</div></div>""", unsafe_allow_html=True)
with m2:
    st.markdown(f"""<div class="metric-box"><div class="metric-title">Learning Velocity</div><div class="metric-main" style="color:#10b981">{growth_rate:.1f}%</div></div>""", unsafe_allow_html=True)
with m3:
    st.markdown(f"""<div class="metric-box"><div class="metric-title">System Bottleneck</div><div class="metric-main" style="color:#f59e0b; font-size: 1.6rem; padding-top: 10px;">{bottleneck_subj}</div></div>""", unsafe_allow_html=True)
with m4:
    st.markdown(f"""<div class="metric-box"><div class="metric-title">Active Discrepancies</div><div class="metric-main" style="color:#ef4444">{weak_count}</div></div>""", unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

# 2. Urgency & Risk Focus
st.markdown('<div class="premium-card" style="border-top: 4px solid #ef4444;">', unsafe_allow_html=True)
st.markdown('<div class="premium-card" style="border-top: 4px solid #ef4444;">', unsafe_allow_html=True)
st.markdown("""
<div style="margin-bottom: 20px;">
    <h3 style="margin: 0;">🚨 Immediate Priority Queue (48h Support)</h3>
    <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 0.9rem;">Students requiring pedagogical intervention within the next 48 hours based on automated priority scoring.</p>
</div>
""", unsafe_allow_html=True)
priority_df = calculate_priority(df)
priority_df["Urgency"] = priority_df.apply(calculate_urgency, axis=1)
urgent_cases = priority_df[priority_df["Urgency"] == "🚨 Immediate Attention"].head(5)
if not urgent_cases.empty:
    st.dataframe(urgent_cases[["Name", "Subject", "Topic", "Score", "Attempts"]], use_container_width=True, hide_index=True)
else:
    st.success("All critical interventions are clear.")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="premium-card" style="border-top: 4px solid #f59e0b;">', unsafe_allow_html=True)
st.markdown("""
<div style="margin-bottom: 20px;">
    <h3 style="margin: 0;">⚠️ Early Performance Alert System</h3>
    <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 0.9rem;">Detecting predictive decline based on student stability models before it impacts final grades.</p>
</div>
""", unsafe_allow_html=True)
priority_df = calculate_priority(df)
priority_df["Risk_Status"] = priority_df.apply(predict_risk, axis=1)
at_risk_cases = priority_df[priority_df["Risk_Status"] == "At Risk"].head(5)
if not at_risk_cases.empty:
    st.dataframe(at_risk_cases[["Name", "Subject", "Topic", "Score", "Attempts"]], use_container_width=True, hide_index=True)
else:
    st.success("Learning stability is normalized.")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 3. Behavioral Matrix
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.markdown("""
<div style="margin-bottom: 20px;">
    <h3 style="margin: 0;">📊 Student Effort Tracker</h3>
    <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 0.9rem;">Mapping Effort (Attempts) against Results (Score). Spot students who are working hard but struggling.</p>
</div>
""", unsafe_allow_html=True)
fig = px.scatter(
    df, x="Attempts", y="Score", color="Subject", hover_name="Name",
    size="Time_Spent", template="plotly_dark",
    color_discrete_sequence=px.colors.qualitative.Vivid
)
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_family="Inter", margin=dict(t=20, l=0, r=0, b=0))
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4. Individual Performance Audit
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.markdown("""
<div style="margin-bottom: 20px;">
    <h3 style="margin: 0;">🔍 Detailed Performance Archive</h3>
    <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 0.9rem;">Deep dive into a specific student's journey, including stability scores and history.</p>
</div>
""", unsafe_allow_html=True)
all_students = df["Name"].unique()
selected_name = st.selectbox("Search Archive", all_students)
student_data = df[df["Name"] == selected_name].sort_values("Date")
dl, dr = st.columns([2, 1])
with dl:
    fig_line = px.line(student_data, x="Date", y="Score", color="Subject", markers=True, line_shape='spline', template="plotly_dark", title=f"Arc: {selected_name}")
    fig_line.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_family="Inter")
    st.plotly_chart(fig_line, use_container_width=True)
with dr:
    st.markdown("<h4 style='margin-bottom:12px;'>Stability Index</h4>", unsafe_allow_html=True)
    consistency_df = calculate_consistency(df)
    std_val = consistency_df[consistency_df["Name"] == selected_name]["Score_Std"].values[0]
    if std_val > 15:
        st.markdown(f'<div style="background:rgba(239,68,68,0.1); color:#ef4444; border:1px solid #ef4444; border-radius:12px; padding:12px; text-align:center;">⚠️ UNSTABLE ARC (SD: {std_val:.1f})</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background:rgba(16,185,129,0.1); color:#10b981; border:1px solid #10b981; border-radius:12px; padding:12px; text-align:center;">✅ CONSISTENT ARC (SD: {std_val:.1f})</div>', unsafe_allow_html=True)
    st.markdown("<br><b>Intervention Impact</b>", unsafe_allow_html=True)
    impact_loop = track_intervention_impact(student_data)
    if not impact_loop.empty:
        st.dataframe(impact_loop, hide_index=True, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. AI Coaching Loop
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.markdown("""
<div style="margin-bottom: 20px;">
    <h3 style="margin: 0;">🤖 AI Root Cause & Script Generator</h3>
    <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 0.9rem;">Ask the AI to explain *why* a student is struggling and generate a coaching script for your next call.</p>
</div>
""", unsafe_allow_html=True)
student_names = df["Name"].unique()
sel_name = st.selectbox("Select Student for Simulation", student_names, key="sim_sel")
latest_rec = df[df["Name"] == sel_name].iloc[-1]
ac1, ac2 = st.columns(2)
with ac1:
    if st.button("Generate Root Cause Analysis"):
        with st.spinner("AI Analysis..."):
            st.markdown(f'<div class="premium-card" style="background:rgba(255,255,255,0.05); margin-top:16px;">{get_ai_recommendation(latest_rec)}</div>', unsafe_allow_html=True)
with ac2:
    if st.button("Generate Live Call Script"):
        with st.spinner("Human Sim..."):
            st.markdown(f'<div class="premium-card" style="background:rgba(255,255,255,0.05); margin-top:16px;">{get_coaching_script(latest_rec)}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Vanilla JS Walkthrough Injection ---
st.markdown("""
<div id="walkthrough" class="walkthrough hidden">
  <div class="walkthrough-card">
    <div class="walkthrough-header">
      <h4 id="walkthrough-title">Tour Step</h4>
      <span id="walkthrough-progress">1/7</span>
    </div>
    <div class="progress-bar-container"><div id="progress-indicator"></div></div>
    <p id="walkthrough-text"></p>
    <div class="walkthrough-buttons">
      <button id="skip-btn">Exit</button>
      <div style="display: flex; gap: 8px;">
        <button id="back-btn" class="hidden">Back</button>
        <button id="next-btn">Next Step</button>
      </div>
    </div>
  </div>
</div>

<style>
.walkthrough {
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  pointer-events: none;
  z-index: 10000;
}

.walkthrough-card {
  position: absolute;
  max-width: 360px;
  background: linear-gradient(135deg, rgba(30, 41, 59, 0.98) 0%, rgba(15, 23, 42, 0.98) 100%);
  backdrop-filter: blur(20px);
  color: #f8fafc;
  padding: 24px;
  border-radius: 20px;
  pointer-events: auto;
  box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.1), 0 25px 50px -12px rgba(0, 0, 0, 0.8);
  font-family: 'Inter', sans-serif;
  transition: all 0.6s cubic-bezier(0.19, 1, 0.22, 1);
  z-index: 10001;
}

.walkthrough-header {
  display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;
}

.walkthrough-header h4 { margin: 0; color: #818cf8; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.05em; }
#walkthrough-progress { font-size: 0.75rem; color: #94a3b8; }

.progress-bar-container { width: 100%; height: 4px; background: rgba(255, 255, 255, 0.1); border-radius: 2px; margin-bottom: 16px; overflow: hidden; }
#progress-indicator { height: 100%; width: 14%; background: #6366f1; transition: 0.4s ease; }

.walkthrough-card p { margin: 0 0 24px 0; line-height: 1.6; font-size: 0.95rem; color: #e2e8f0; }
.walkthrough-card strong { color: #f8fafc; }

.walkthrough-buttons {
  display: flex; justify-content: space-between; align-items: center; gap: 12px;
}

.walkthrough-buttons button {
  padding: 10px 16px; border: none; cursor: pointer; border-radius: 12px;
  font-weight: 600; font-family: 'Outfit', sans-serif; transition: 0.3s; font-size: 0.9rem;
}

#next-btn { background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; }
#next-btn:hover { transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.5); }

#back-btn { background: rgba(255, 255, 255, 0.05); color: #94a3b8; border: 1px solid rgba(255, 255, 255, 0.1); }
#back-btn:hover { background: rgba(255, 255, 255, 0.1); color: #f8fafc; }

#skip-btn { background: transparent; color: #64748b; font-weight: 400; padding: 0; }
#skip-btn:hover { color: #ef4444; }

.highlight {
  outline: 4px solid #6366f1 !important; outline-offset: 4px; border-radius: 16px !important;
  box-shadow: 0 0 0 9999px rgba(0, 0, 0, 0.75) !important;
  z-index: 9998 !important; position: relative !important; transition: all 0.4s ease;
}

.hidden { display: none !important; }
</style>

<script>
// Target Streamlit elements by searching for headers and identifying their parent blocks
const steps = [
  {
    targetText: "Elite Student Insight Engine",
    title: "Welcome Overview",
    text: "<strong>What is this?</strong> This is your Central Command for monitor student learning patterns.<br><br><strong>Why it matters:</strong> It uses AI to predict failures before they happen."
  },
  {
    targetText: "System-Wide Learning Health",
    title: "System Metrics",
    text: "<strong>What is this?</strong> The 'Big Picture' overview of every student in your cohort.<br><br><strong>Why it matters:</strong> Spot subject-wide bottlenecks or overall performance drops instantly."
  },
  {
    targetText: "Immediate Priority Queue",
    title: "Priority Queue",
    text: "<strong>What is this?</strong> A critical list of students who need help right now (within 48h).<br><br><strong>Why it matters:</strong> Don't waste time—focus on the students with the highest urgency first."
  },
  {
    targetText: "Early Performance Alert System",
    title: "Early Warning",
    text: "<strong>What is this?</strong> A 'stability detector' that finds students falling behind early.<br><br><strong>Why it matters:</strong> Intervene weeks before a final exam to turn things around."
  },
  {
    targetText: "Student Effort Tracker",
    title: "Effort Tracker",
    text: "<strong>What is this?</strong> A map of how many attempts a student makes vs. their score.<br><br><strong>Why it matters:</strong> Identify 'high-effort' students who aren't seeing results."
  },
  {
    targetText: "Detailed Performance Archive",
    title: "Deep Dive",
    text: "<strong>What is this?</strong> A detailed historical archive for individual students.<br><br><strong>Why it matters:</strong> Zoom in on a single student to see if their performance is stable or erratic."
  },
  {
    targetText: "AI Root Cause",
    title: "AI Action",
    text: "<strong>What is this?</strong> Your AI Coaching partner that explains the data.<br><br><strong>Why it matters:</strong> Get the exactly reasoning for a drop and a script for your next call."
  }
];

let currentStep = 0;

function findElementByText(text) {
    // Search the whole parent document for a header containing the text
    const elements = Array.from(document.querySelectorAll('h1, h2, h3, div'));
    const target = elements.find(el => el.innerText && el.innerText.includes(text));
    
    if (target) {
        // Find the nearest Streamlit container if possible, otherwise use target
        return target.closest('.stVerticalBlock') || target;
    }
    return null;
}

function startWalkthrough() {
  const walkthrough = document.getElementById("walkthrough");
  if (!walkthrough) {
      console.log("Walkthrough container not found yet...");
      return;
  }
  walkthrough.classList.remove("hidden");
  showStep();
}

function showStep() {
  const step = steps[currentStep];
  const el = findElementByText(step.targetText);

  if (!el) {
    console.error("Target element not found for text:", step.targetText);
    setTimeout(showStep, 500); // Polling until found
    return;
  }

  document.querySelectorAll(".highlight").forEach(e => e.classList.remove("highlight"));
  el.classList.add("highlight");
  el.scrollIntoView({ behavior: "smooth", block: "center" });

  const rect = el.getBoundingClientRect();
  const card = document.querySelector(".walkthrough-card");
  
  let top = rect.bottom + 24;
  let left = rect.left;
  
  if (top + card.offsetHeight > window.innerHeight) {
    top = rect.top - card.offsetHeight - 24;
  }
  
  card.style.top = `${top + window.scrollY}px`;
  card.style.left = `${Math.max(24, Math.min(left, window.innerWidth - card.offsetWidth - 24))}px`;

  document.getElementById("walkthrough-title").innerText = step.title;
  document.getElementById("walkthrough-text").innerHTML = step.text;
  document.getElementById("walkthrough-progress").innerText = `${currentStep + 1}/${steps.length}`;
  document.getElementById("progress-indicator").style.width = `${((currentStep + 1) / steps.length) * 100}%`;
  
  const nextBtn = document.getElementById("next-btn");
  const backBtn = document.getElementById("back-btn");
  nextBtn.innerText = currentStep === steps.length - 1 ? "Finish Tour" : "Next Step";
  if (currentStep === 0) backBtn.classList.add("hidden");
  else backBtn.classList.remove("hidden");
}

document.getElementById("next-btn").addEventListener("click", () => {
  if (currentStep < steps.length - 1) {
    currentStep++;
    showStep();
  } else endWalkthrough();
});

document.getElementById("back-btn").addEventListener("click", () => {
  if (currentStep > 0) {
    currentStep--;
    showStep();
  }
});

document.getElementById("skip-btn").addEventListener("click", endWalkthrough);

function endWalkthrough() {
  document.getElementById("walkthrough").classList.add("hidden");
  document.querySelectorAll(".highlight").forEach(e => e.classList.remove("highlight"));
  localStorage.setItem("walkthroughSeen", "true");
}

// Initial delay to ensure everything is settled
setTimeout(() => {
    if (!localStorage.getItem("walkthroughSeen")) {
        startWalkthrough();
    }
}, 1500);

</script>
""", unsafe_allow_html=True)

# Methodology Footer
st.markdown("""
<div style="text-align: center; color: #475569; padding: 40px;">
    <p style="font-size: 0.8rem;">Pedagogical Engine: WCF Prioritization • Stability Indexing • AI Root Cause Mapping.</p>
</div>
""", unsafe_allow_html=True)
