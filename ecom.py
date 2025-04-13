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

# KPIs Section
st.markdown("<h3 style='margin-top: 40px;'>📌 Key Performance Indicators</h3>", unsafe_allow_html=True)
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Gross Revenue", "₹9.43 Cr")
kpi2.metric("Net Revenue", "₹8.24 Cr")
kpi3.metric("Profit Margin", "85.7%")

kpi4, kpi5, kpi6 = st.columns(3)
kpi4.metric("Return Rate", "14.2%")
kpi5.metric("Cart Abandonment Rate", "62.1%")
kpi6.metric("Avg. Order Value (AOV)", "₹3,270")

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
