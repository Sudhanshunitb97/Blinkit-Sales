import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="E-commerce Strategy Dashboard", layout="wide")

# Title Section
st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>📊 E-commerce Revenue Optimization Dashboard</h1>
    <p style='text-align: center; color: gray;'>Track KPIs, Analyze Strategic Simulations, and Forecast Revenue Growth</p>
""", unsafe_allow_html=True)

# Load summary data
data = {
    "Strategy": [
        "Reduce Tier 3 Return Rate by 5%",
        "Increase AOV by ₹100 in Top 30%",
        "Reduce Fashion Abandonment by 10%",
        "+1 Order from Champions",
        "Improve Funnel Conversion by 5%",
        "Bundle Skincare + Fragrance",
        "Reallocate Marketing Budget",
        "Logistics Optimization",
        "Loyalty Program (5% Conversion)"
    ],
    "Estimated Gain (INR)": [
        882944,
        867400,
        1274230,
        2591354,
        6534513,
        39900,
        436876,
        12750,
        1539314
    ]
}
df_sim = pd.DataFrame(data)

# KPI Cards - Custom HTML/CSS Layout
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
            background-color: #f0f4fa;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            text-align: center;
        }
        .kpi-title {
            font-size: 15px;
            color: #6c757d;
            margin-bottom: 5px;
        }
        .kpi-value {
            font-size: 24px;
            color: #4B8BBE;
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

# Bar Chart Visualization
st.markdown("<h3 style='margin-top: 40px;'>📈 Revenue Gain by Strategy</h3>", unsafe_allow_html=True)
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
    template="simple_white"
)
st.plotly_chart(bar_fig, use_container_width=True)

# Simulation Table
with st.expander("📋 View Simulation Data Table"):
    df_display = df_sim.copy()
    df_display["Estimated Gain (INR)"] = df_display["Estimated Gain (INR)"].apply(lambda x: f"₹{x:,.0f}")
    st.dataframe(df_display, use_container_width=True)

# Total Uplift Summary
total_gain = sum(data["Estimated Gain (INR)"])
st.success(f"✅ Total Revenue Gain Simulated: ₹{total_gain:,.0f} (15.03% Growth Achieved)")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>Dashboard built with ❤️ using Streamlit | A Full-Stack Data Strategy Showcase</p>
""", unsafe_allow_html=True)
