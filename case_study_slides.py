
import streamlit as st

def show_case_study_slides():
    st.title("📽️ Case Study Slides: E-commerce Revenue Optimization")

    slides = {
        "Slide 1: Title": [
            "**E-commerce Revenue Optimization Project**",
            "*Unlocking Growth with Data-Driven Strategy*",
            "Tools Used: Excel, SQL (BigQuery), Python, Streamlit, Power BI"
        ],
        "Slide 2: Objective": [
            "Boost revenue by 15%+ without increasing ad spend",
            "Optimize conversion rate, AOV, return rate, cart abandonment, loyalty",
            "Simulate impact of business interventions"
        ],
        "Slide 3: Workflow Overview": [
            "Excel → SQL → Python → Simulations → Streamlit Dashboard"
        ],
        "Slide 4: Excel Phase Highlights": [
            "- Tier 3 had highest return rate (14.2%)",
            "- Fashion category showed highest cart abandonment (65%+)",
            "- Loyal customers had significantly higher AOV",
            "- Strong seasonal trends in Nov–Jan"
        ],
        "Slide 5: SQL Analysis Highlights": [
            "- Fashion, Electronics = highest cart abandonment losses",
            "- Tier 3 + Fashion → 70%+ abandonment",
            "- Loyalty drops abandonment by 40%",
            "- Top subcategories: Curtains, Spices, Rice, Sofa"
        ],
        "Slide 6: Python Analytics": [
            "- 608 'Champions' with highest CLV",
            "- 8800+ At Risk / Hibernating users",
            "- Tier 3 returns heavily cut profit",
            "- Email & Google had best ROI"
        ],
        "Slide 7: Hypothesis Testing": [
            "- AOV difference not significant (Z-test)",
            "- Tier 3 return rate very high (ANOVA)",
            "- Abandonment varies by category (Chi-square)"
        ],
        "Slide 8: Streamlit Dashboard": [
            "- KPI cards, forecasts, slicers",
            "- Revenue gain chart",
            "- Simulation data table",
            "- Clean UI for business review"
        ],
        "Slide 9: Simulation Summary": [
            "- Funnel Conversion +5% → ₹6.53L",
            "- Loyalty Conversion +10% → ₹1.75Cr",
            "- AOV ↑₹100 (Top 30%) → ₹8.67L",
            "- Cart Abandonment ↓10% → ₹12.74L",
            "- Return Rate ↓5% → ₹10.21L",
            "- Marketing Shift → ₹6.14L",
            "- Logistics Optimization → ₹12.7K",
            "**Total Gain: ₹2.78Cr**"
        ],
        "Slide 10: Business Impact": [
            "- Achieved 15–20% simulated growth",
            "- ₹2.78 Cr gain without budget increase",
            "- Insight → Intervention → Uplift"
        ],
        "Slide 11: What Makes It Unique": [
            "- Full-stack from raw data to dashboard",
            "- Actionable simulations, not just visuals",
            "- Stats-backed & business-oriented"
        ],
        "Slide 12: Discussion": [
            "Ready for Q&A",
            "Deep dive into any simulation or insight"
        ],
        "Slide 13: Thank You": [
            "Name: [Your Name]",
            "Portfolio: [Your Link]",
            "Let’s talk data growth!"
        ]
    }

    for title, points in slides.items():
        with st.expander(title):
            for point in points:
                st.markdown(f"- {point}")
