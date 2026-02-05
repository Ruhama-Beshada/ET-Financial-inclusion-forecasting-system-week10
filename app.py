# app.py - Streamlit Dashboard for Financial Inclusion

import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Step 1: Load your data
# -----------------------------
observations = pd.read_csv("observations.csv")  # Historical data
events = pd.read_csv("events.csv")              # Event-impact dataevents.csv
forecasts = pd.read_csv("forecasts.csv")        # Forecasted values from Task 4

# -----------------------------
# Step 2: Sidebar navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Trends", "Forecasts", "Inclusion Projections"])

# -----------------------------
# Step 3: Overview Page
# -----------------------------
if page == "Overview":
    st.title("Financial Inclusion Dashboard - Overview")

    # Key metrics
    latest_year = observations['Year'].max()
    acc_ownership_latest = observations.loc[observations['Year']==latest_year, 'ACC_OWNERSHIP'].values[0]
    mm_accounts_latest = observations.loc[observations['Year']==latest_year, 'ACC_MM_ACCOUNT'].values[0]
    active_rate_latest = observations.loc[observations['Year']==latest_year, 'USG_ACTIVE_RATE'].values[0]

    st.metric("Account Ownership (%)", f"{acc_ownership_latest:.1f}")
    st.metric("Mobile Money Accounts (%)", f"{mm_accounts_latest:.1f}")
    st.metric("Active Usage Rate (%)", f"{active_rate_latest:.1f}")

# -----------------------------
# Step 4: Trends Page
# -----------------------------
elif page == "Trends":
    st.title("Financial Inclusion Trends")

    # Date range selector
    min_year = int(observations['Year'].min())
    max_year = int(observations['Year'].max())
    year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))

    # Filter data
    obs_filtered = observations[(observations['Year'] >= year_range[0]) & (observations['Year'] <= year_range[1])]

    # Plot trend
    fig = px.line(
        obs_filtered,
        x="Year",
        y=["ACC_OWNERSHIP", "ACC_MM_ACCOUNT", "USG_ACTIVE_RATE"],
        labels={"value": "Percentage", "variable": "Indicator"},
        title="Financial Inclusion Trends"
    )
    st.plotly_chart(fig)

# -----------------------------
# Step 5: Forecasts Page
# -----------------------------
elif page == "Forecasts":
    st.title("Financial Inclusion Forecasts (2025-2027)")

    scenario = st.selectbox("Select Scenario", ["Base", "Optimistic", "Pessimistic"])

    # Select columns based on scenario
    if scenario == "Base":
        y_cols = ["ACC_OWNERSHIP", "ACC_MM_ACCOUNT", "USG_ACTIVE_RATE"]
    elif scenario == "Optimistic":
        y_cols = ["ACC_OWNERSHIP_optimistic", "ACC_MM_ACCOUNT_optimistic", "USG_ACTIVE_RATE_optimistic"]
    else:
        y_cols = ["ACC_OWNERSHIP_pessimistic", "ACC_MM_ACCOUNT_pessimistic", "USG_ACTIVE_RATE_pessimistic"]

    fig = px.line(
        forecasts,
        x="Year",
        y=y_cols,
        labels={"value": "Percentage", "variable": "Indicator"},
        title=f"Forecasts: {scenario} Scenario"
    )
    st.plotly_chart(fig)

# -----------------------------
# Step 6: Inclusion Projections Page
# -----------------------------
elif page == "Inclusion Projections":
    st.title("Financial Inclusion Projections")

    # Progress toward 60% target
    latest_forecast = forecasts[forecasts['Year'] == 2027]['ACC_OWNERSHIP'].values[0]
    st.progress(min(int(latest_forecast), 100))
    st.write(f"Projected Account Ownership in 2027: {latest_forecast:.1f}%")
