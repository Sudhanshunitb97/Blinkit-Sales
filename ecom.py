import streamlit as st
import pandas as pd

# Title
st.title("📊 E-commerce Revenue Growth Dashboard")
st.subheader("Business KPIs, Strategy Simulations, and Impact Summary")

# Load or simulate summary data
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

# KPIs Summary Section
st.header("📌 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Gross Revenue", "₹9.43 Cr")
col2.metric("Net Revenue", "₹8.24 Cr")
col3.metric("Profit Margin", "85.7%")

col4, col5, col6 = st.columns(3)
col4.metric("Return Rate", "14.2%")
col5.metric("Cart Abandonment Rate", "62.1%")
col6.metric("Average Order Value (AOV)", "₹3,270")

# Simulation Table
st.header("📈 Strategy Simulation Outcomes")
df_sim = pd.DataFrame(data)
df_sim["Estimated Gain (INR)"] = df_sim["Estimated Gain (INR)"].apply(lambda x: f"₹{x:,.0f}")
st.dataframe(df_sim, use_container_width=True)

# Revenue Uplift Summary
total_gain = sum(data["Estimated Gain (INR)"])
st.success(f"✅ Total Revenue Gain Simulated: ₹{total_gain:,.0f} (15.03% Growth Achieved)")

# Footer
st.markdown("---")
st.caption("Built using Streamlit | Full-stack Business Analytics Project")
