
import streamlit as st
import pandas as pd

from validator import validate_inputs
from scoring import (
    calculate_factor_scores,
    calculate_credit_score,
    classify_score
)
from explanations import generate_explanation
from simulator import simulate_utilisation
from database import create_table, save_score, get_score_history


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="CreditPulse | Pulse Lab",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

create_table()

# ==========================================
# CUSTOM DESIGN SYSTEM
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

.stApp {
    background: #0b1016;
    color: #edf3f1;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

[data-testid="stSidebar"] {
    background: #111a21;
    border-right: 1px solid #24343b;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #f1f7f4 !important;
}

p, label, span {
    font-family: 'DM Sans', sans-serif;
}

.pulse-brand {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 27px;
    font-weight: 800;
    color: #b5f36d;
    letter-spacing: -1px;
}

.pulse-subtitle {
    color: #82969a;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero {
    background: linear-gradient(120deg, #17252b, #142d2a);
    border: 1px solid #29443d;
    border-radius: 22px;
    padding: 30px;
    margin: 15px 0 25px 0;
}

.hero-label {
    color: #b5f36d;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: 700;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    color: #f4f8f4;
    font-size: 36px;
    font-weight: 700;
    margin: 12px 0 8px 0;
}

.hero-description {
    color: #a9bdb6;
    font-size: 14px;
    max-width: 650px;
    line-height: 1.7;
}

.section-label {
    color: #b5f36d;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: 700;
    margin-bottom: 5px;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 23px;
    font-weight: 700;
    color: #f1f7f4;
    margin-bottom: 15px;
}

.panel {
    background: #131e25;
    border: 1px solid #263941;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 15px;
}

.metric-card {
    background: #142129;
    border: 1px solid #2a4145;
    border-radius: 17px;
    padding: 20px;
    min-height: 125px;
}

.metric-label {
    color: #91a5a6;
    font-size: 12px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.metric-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 30px;
    font-weight: 700;
    color: #f3f8f4;
    margin-top: 12px;
}

.metric-accent {
    color: #b5f36d;
}

.score-ring {
    width: 205px;
    height: 205px;
    border-radius: 50%;
    background: conic-gradient(
        #b5f36d 0% var(--score-progress),
        #263b3c var(--score-progress) 100%
    );
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 20px auto;
}

.score-ring-inner {
    width: 175px;
    height: 175px;
    border-radius: 50%;
    background: #131e25;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.score-number {
    color: #f3f8f4;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 43px;
    font-weight: 700;
}

.score-caption {
    color: #91a5a6;
    font-size: 12px;
}

.category-pill {
    display: inline-block;
    padding: 7px 18px;
    border-radius: 30px;
    background: #263a2c;
    color: #b5f36d;
    font-weight: 700;
    font-size: 13px;
    margin-top: 8px;
}

.factor-card {
    background: #142129;
    border: 1px solid #293d44;
    border-radius: 13px;
    padding: 16px;
    margin-bottom: 10px;
}

.factor-name {
    color: #e8f0eb;
    font-weight: 600;
    font-size: 14px;
}

.factor-score {
    color: #b5f36d;
    font-weight: 700;
    float: right;
}

.explanation-card {
    background: #19251f;
    border-left: 3px solid #b5f36d;
    border-radius: 10px;
    padding: 17px;
    margin-bottom: 12px;
    color: #dce8df;
    line-height: 1.6;
}

.explanation-card strong {
    color: #b5f36d;
}

.stButton > button,
.stFormSubmitButton > button {
    background: #b5f36d !important;
    color: #101810 !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 800 !important;
    min-height: 45px;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #c8ff83 !important;
    color: #101810 !important;
}

.stTextInput input,
.stNumberInput input {
    background: #17252b !important;
    color: white !important;
}

[data-testid="stMetric"] {
    background: #142129;
    border: 1px solid #293d44;
    padding: 15px;
    border-radius: 13px;
}

[data-testid="stMetricValue"] {
    color: #b5f36d !important;
}

hr {
    border-color: #263941;
}

.stCaption {
    color: #82969a;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown(
        '<div class="pulse-brand">◈ CreditPulse</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="pulse-subtitle">Your personal credit lab</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### ◉ Credit Profile")

    st.caption("Enter sample profile details below.")

    with st.form("credit_profile_form"):

        payment = st.slider(
            "On-time payments (%)",
            0, 100, 90
        )

        utilisation = st.slider(
            "Credit utilisation (%)",
            0, 100, 30
        )

        account_age = st.number_input(
            "Oldest account age (years)",
            min_value=0.0,
            max_value=100.0,
            value=5.0,
            step=0.5
        )

        enquiries = st.number_input(
            "Recent loan enquiries",
            min_value=0,
            max_value=50,
            value=1,
            step=1
        )

        credit_types = st.number_input(
            "Number of credit types",
            min_value=0,
            max_value=20,
            value=3,
            step=1
        )

        submitted = st.form_submit_button(
            "⚡ Analyse My Credit",
            use_container_width=True
        )

    st.divider()

    st.caption("MODEL INFORMATION")
    st.write("Score range: 300–900")
    st.write("Model: Weighted scoring")
    st.write("Version: CP-005")


# ==========================================
# PROCESS INPUTS
# ==========================================

if submitted:

    errors = validate_inputs(
        payment,
        utilisation,
        account_age,
        enquiries,
        credit_types
    )

    if errors:
        for error in errors:
            st.error(error)

    else:

        factors = calculate_factor_scores(
            payment,
            utilisation,
            account_age,
            enquiries,
            credit_types
        )

        score = calculate_credit_score(factors)
        category = classify_score(score)

        st.session_state["profile"] = {
            "payment": payment,
            "utilisation": utilisation,
            "account_age": account_age,
            "enquiries": enquiries,
            "credit_types": credit_types
        }

        st.session_state["factors"] = factors
        st.session_state["score"] = score
        st.session_state["category"] = category

        save_score(
            payment,
            utilisation,
            account_age,
            enquiries,
            credit_types,
            score,
            category
        )


# ==========================================
# MAIN HERO
# ==========================================

st.markdown("""
<div class="hero">
    <div class="hero-label">CREDIT INTELLIGENCE / CP-005</div>
    <div class="hero-title">Know your score.<br>Understand your power.</div>
    <div class="hero-description">
        A transparent credit scoring experience.
        Explore the factors behind your estimated score,
        discover improvement opportunities and test
        different financial scenarios.
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# DASHBOARD
# ==========================================

if "score" not in st.session_state:

    st.markdown("""
    <div class="panel">
        <div class="section-label">WELCOME TO PULSE LAB</div>
        <div class="section-title">Your financial snapshot starts here.</div>
        <p style="color:#9db0ad; line-height:1.8;">
            Enter your credit profile in the left panel and click
            <b style="color:#b5f36d;">Analyse My Credit</b>
            to generate your estimated score, factor analysis
            and personalised explanations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Your dashboard is waiting for its first credit profile.")

else:

    score = st.session_state["score"]
    category = st.session_state["category"]
    factors = st.session_state["factors"]
    profile = st.session_state["profile"]

    # --------------------------------------
    # SCORE OVERVIEW
    # --------------------------------------

    st.markdown(
        '<div class="section-label">01 / SCORE OVERVIEW</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Your credit health</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1, 1.5])

    progress = ((score - 300) / 600) * 100

    with left:

        st.markdown(f"""
        <div class="panel" style="text-align:center;">
            <div class="section-label">YOUR ESTIMATED SCORE</div>

            <div class="score-ring"
                 style="--score-progress:{progress:.2f}%;">
                <div class="score-ring-inner">
                    <div class="score-number">{score}</div>
                    <div class="score-caption">OUT OF 900</div>
                </div>
            </div>

            <div class="category-pill">{category}</div>
            <p style="color:#91a5a6; font-size:12px; margin-top:15px;">
                CreditPulse model estimate
            </p>
        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown('<div class="panel">', unsafe_allow_html=True)

        st.markdown("### Profile summary")

        st.metric(
            "On-time payment rate",
            f"{profile['payment']}%"
        )

        st.metric(
            "Credit utilisation",
            f"{profile['utilisation']}%"
        )

        st.metric(
            "Oldest credit account",
            f"{profile['account_age']} years"
        )

        st.metric(
            "Recent enquiries",
            profile["enquiries"]
        )

        st.markdown('</div>', unsafe_allow_html=True)


    # --------------------------------------
    # FACTOR ANALYSIS
    # --------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-label">02 / BREAKDOWN</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">What drives your score?</div>',
        unsafe_allow_html=True
    )

    factor_names = {
        "payment_history": "Payment History",
        "credit_utilisation": "Credit Utilisation",
        "account_age": "Account Age",
        "loan_enquiries": "Loan Enquiries",
        "credit_mix": "Credit Mix"
    }

    weights = {
        "payment_history": "35%",
        "credit_utilisation": "30%",
        "account_age": "15%",
        "loan_enquiries": "10%",
        "credit_mix": "10%"
    }

    factor_columns = st.columns(5)

    for column, (key, value) in zip(
        factor_columns, factors.items()
    ):

        with column:

            st.markdown(f"""
            <div class="factor-card">
                <div class="factor-name">
                    {factor_names[key]}
                </div>
                <div style="color:#b5f36d; font-size:25px;
                            font-weight:800; margin-top:12px;">
                    {value:.0f}
                </div>
                <div style="color:#91a5a6; font-size:11px;">
                    Weight: {weights[key]}
                </div>
            </div>
            """, unsafe_allow_html=True)

    chart_data = pd.DataFrame({
        "Factor": [
            factor_names[key] for key in factors
        ],
        "Score": list(factors.values())
    })

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.bar_chart(
        chart_data,
        x="Factor",
        y="Score",
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)


    # --------------------------------------
    # EXPLANATIONS
    # --------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-label">03 / EXPLAINABLE AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Your two biggest improvement areas</div>',
        unsafe_allow_html=True
    )

    explanations = generate_explanation(factors)

    for index, item in enumerate(explanations, start=1):

        st.markdown(f"""
        <div class="explanation-card">
            <strong>0{index} &nbsp; {item['factor']}</strong>
            <div style="margin-top:8px;">
                Factor score: {item['factor_score']}/100
            </div>
            <div style="margin-top:8px;">
                {item['explanation']}
            </div>
        </div>
        """, unsafe_allow_html=True)


    # --------------------------------------
    # WHAT-IF SIMULATOR
    # --------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-label">04 / PULSE SIMULATOR</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">What if you changed your utilisation?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="panel">',
        unsafe_allow_html=True
    )

    new_utilisation = st.slider(
        "Adjust your simulated credit utilisation",
        min_value=0,
        max_value=100,
        value=int(profile["utilisation"]),
        key="simulation_utilisation"
    )

    simulation = simulate_utilisation(
        payment=profile["payment"],
        current_utilisation=profile["utilisation"],
        account_age=profile["account_age"],
        enquiries=profile["enquiries"],
        credit_types=profile["credit_types"],
        new_utilisation=new_utilisation
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Current score",
        simulation["original_score"]
    )

    c2.metric(
        "Simulated score",
        simulation["simulated_score"]
    )

    c3.metric(
        "Score difference",
        f"{simulation['score_change']:+d}"
    )

    st.caption(
        "Only utilisation changes in this simulation. "
        "The other four inputs remain constant."
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # --------------------------------------
    # SCORE HISTORY
    # --------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-label">05 / PROGRESS TRACKER</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Your score journey</div>',
        unsafe_allow_html=True
    )

    history = get_score_history()

    if history:

        history_df = pd.DataFrame(history)

        history_df["recorded_at"] = pd.to_datetime(
            history_df["recorded_at"]
        )

        history_df = history_df.set_index("recorded_at")

        st.markdown('<div class="panel">', unsafe_allow_html=True)

        st.line_chart(
            history_df["estimated_score"]
        )

        st.dataframe(
            history_df[
                ["payment", "utilisation",
                 "estimated_score", "category"]
            ],
            use_container_width=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

    else:

        st.info("Your score history will appear here.")


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown("""
<div style="text-align:center; padding:15px;">
    <div style="color:#b5f36d; font-weight:800;
                font-family:'Space Grotesk';">
        ◈ CREDITPULSE
    </div>
    <div style="color:#718588; font-size:11px; margin-top:6px;">
        CP-005 | Explainable Credit Score Estimation Engine
    </div>
    <div style="color:#718588; font-size:10px; margin-top:5px;">
        Educational prototype. Not an official credit score.
    </div>
</div>
""", unsafe_allow_html=True)
