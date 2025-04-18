import streamlit as st
import pandas as pd
import plotly.express as px

# Set page layout
st.set_page_config(page_title="E-commerce Strategy Dashboard", layout="wide")

# Light background
st.markdown("""
    <style>
        body, .stApp {
            background-color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <h1 style='text-align: center; color: black;'>📊 E-commerce Revenue Optimization Dashboard</h1>
    <p style='text-align: center; color: black;'>Track KPIs, Analyze Strategic Simulations, and Forecast Revenue Growth</p>
""", unsafe_allow_html=True)

# Finalized simulations
data = {
    "Strategy": [
        "Reduce Tier 3 Return Rate by 5%",
        "₹100 AOV Increase in Top 30%",
        "10% Drop in Fashion Cart Abandonment",
        "Improve Funnel Conversion by 5%",
        "Reallocate 10% Marketing Budget",
        "Logistics Optimization",
        "10% Loyalty Conversion (Non-loyal → loyal)"
    ],
    "Estimated Gain (INR)": [
        1021408,
        867400,
        1274230,
        6534513,
        614244,
        12750,
        17560205
    ]
}
df_sim = pd.DataFrame(data)

# KPI Cards
st.markdown("""
    <style>
        .kpi-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 15px;
            margin-bottom: 40px;
        }
        .kpi-card {
            flex: 1;
            min-width: 200px;
            padding: 20px;
            border-radius: 12px;
            background-color: #1c1c1c;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: center;
        }
        .kpi-title {
            font-size: 15px;
            color: #ffffff;
            margin-bottom: 5px;
        }
        .kpi-value {
            font-size: 24px;
            color: #ffffff;
            font-weight: bold;
        }
    </style>
    <div class='kpi-container'>
        <div class='kpi-card'><div class='kpi-title'>Gross Revenue</div><div class='kpi-value'>₹9.43 Cr</div></div>
        <div class='kpi-card'><div class='kpi-title'>Net Revenue</div><div class='kpi-value'>₹8.24 Cr</div></div>
        <div class='kpi-card'><div class='kpi-title'>Profit Margin</div><div class='kpi-value'>85.7%</div></div>
        <div class='kpi-card'><div class='kpi-title'>Return Rate</div><div class='kpi-value'>14.2%</div></div>
        <div class='kpi-card'><div class='kpi-title'>Cart Abandonment</div><div class='kpi-value'>62.1%</div></div>
        <div class='kpi-card'><div class='kpi-title'>AOV</div><div class='kpi-value'>₹3,270</div></div>
    </div>
""", unsafe_allow_html=True)

# Bar Chart
st.markdown("<h3 style='margin-top: 40px; color: black;'>📈 Revenue Gain by Strategy</h3>", unsafe_allow_html=True)
bar_fig = px.bar(
    df_sim.sort_values("Estimated Gain (INR)", ascending=False),
    x="Estimated Gain (INR)",
    y="Strategy",
    orientation="h",
    text="Estimated Gain (INR)",
    color_discrete_sequence=["#4B8BBE"] * len(df_sim)
)
bar_fig.update_layout(
    xaxis_title="Estimated Gain (INR)",
    yaxis_title="",
    height=500,
    template="plotly_white"
)
st.plotly_chart(bar_fig, use_container_width=True)

# Data Table
with st.expander("📋 View Simulation Data Table"):
    df_display = df_sim.copy()
    df_display["Estimated Gain (INR)"] = df_display["Estimated Gain (INR)"].apply(lambda x: f"₹{x:,.0f}")
    st.dataframe(df_display, use_container_width=True)

# Final Total
total_gain = sum(data['Estimated Gain (INR)'])
st.markdown(f"<p style='color:black; font-weight:1000;'>✅ Total Simulated Revenue Gain: ₹{total_gain:,.0f} (~15–20% Growth)</p>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>Dashboard built with ❤️ using Streamlit | Full-Stack Data Strategy Showcase</p>
""", unsafe_allow_html=True)
