# Ethiopia Financial Inclusion Project

This repository contains a comprehensive analysis and forecasting of financial inclusion in Ethiopia. It includes historical data exploration, event impact modeling, forecasting, and an interactive dashboard for stakeholders.

---

## Project Overview

The project is structured into five main tasks:

---

## Task 1: Data Exploration and Enrichment

**Objective:** Understand the starter dataset and enrich it with additional data useful for forecasting.

### Key Steps:
- Loaded and explored ethiopia_fi_unified_data.csv.
- Examined observations, events, and target records.
- Reviewed impact_links for modeled relationships.
- Added new observations, events, and impact_links where needed (with source documentation, confidence levels, and collection notes).

### Outputs:
- Enriched dataset ready for analysis.
- data_enrichment_log.md documenting all additions and changes.

---

## Task 2: Exploratory Data Analysis (EDA)

**Objective:** Analyze patterns and factors influencing financial inclusion.

### Key Steps:
- Summarized dataset by record_type, pillar, and source_type.
- Visualized temporal coverage of indicators.
- Assessed data quality and identified gaps.
- Analyzed account ownership, mobile money adoption, and active usage trends.
- Explored infrastructure and enabling factors.
- Visualized events timeline and correlated events with indicator trends.
- Investigated Ethiopia-specific dynamics (gender, urban-rural gap, slowdown 2021-2024).

### Outputs:
- EDA notebook with visualizations.
- Summary of key insights (≥5 insights with supporting evidence).
- Data quality assessment documenting limitations.

---

## Task 3: Event Impact Modeling

**Objective:** Model how events (policies, product launches, infrastructure investments) affect indicators.

### Key Steps:
- Built Event-Indicator Impact Matrix linking events to indicators.
- Estimated effect magnitude, direction, and lag for each event.
- Validated against historical data (e.g., Telebirr launch impact on mobile money accounts).
- Refined estimates using comparable country evidence where data was insufficient.
- Documented assumptions, methodology, and uncertainties.

### Outputs:
- Impact modeling notebook.
- Event-indicator association matrix (table or heatmap).
- Documentation of methodology, sources, validation, and assumptions.

---

## Task 4: Forecasting Access and Usage

**Objective:** Forecast Account Ownership and Digital Payment Usage for 2025-2027.

### Key Steps:
- Defined targets:
  - Account Ownership (% of adults with financial accounts)
  - Digital Payment Usage (% of adults using digital payments)
- Selected forecasting approaches:
  - Trend regression (linear/log)
  - Event-augmented model (trend + expected event impacts)
  - Scenario analysis (Base, Optimistic, Pessimistic)
- Generated forecasts with confidence intervals.
- Produced visualizations and scenario comparisons.
- Interpreted results and identified key uncertainties and impactful events.

### Outputs:
- Forecasting notebook.
- Forecast tables with confidence intervals.
- Scenario visualizations and written interpretation.

---

## Task 5: Dashboard Development

**Objective:** Create an interactive dashboard for stakeholders to explore data, event impacts, and forecasts.

### Key Features:
- Overview Page: Key metrics, P2P/ATM ratio, growth highlights.
- Trends Page: Interactive time series plots, date range selector, channel comparison.
- Forecasts Page: Forecast visualizations with scenario selection.
- Inclusion Projections Page: Progress toward 60% account ownership target.

### Technical Details:
- Built with Streamlit.
- Includes ≥4 interactive visualizations.
- Provides data download functionality.
- Clear labels, explanations, and scenario selection.

**Live Dashboard Link:** Open Dashboard

---

## Installation & Setup (Local)

### Clone the repository:
```bash
git clone <YOUR_REPO_LINK>
cd ethiopia-fi-forecast
