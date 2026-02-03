# Ethiopia Financial Inclusion Forecast – Task 2: Exploratory Data Analysis

## Overview
This notebook analyzes financial inclusion in Ethiopia using the `ethiopia_fi_unified_data` dataset. The goal is to identify patterns, trends, and factors affecting access and usage of financial services, and to provide insights for forecasting models.

## Dataset Summary
| Record Type | Count | Description |
|------------|-------|-------------|
| observation | 30 | Measured values from surveys, reports, operators |
| event       | 10 | Policies, product launches, market entries, milestones |
| impact_link | 14 | Modeled relationships between events and indicators |
| target      | 3  | Official policy goals (e.g., NFIS-II targets) |

### Pillars Covered
- **ACCESS:** 16 records  
- **USAGE:** 11 records  
- **GENDER:** 5 records  
- **AFFORDABILITY:** 1 record  

### Source Types
- **Operator:** 15  
- **Survey:** 10  
- **Regulator:** 7  
- **Research:** 4  
- **Policy:** 3  
- **Calculated:** 2  
- **News:** 2  

**Observation Date Range:** 2014–2025  

**Indicators:** 19 unique codes including account ownership, mobile money usage, 4G coverage, ATM counts, gender gap measures, and digital payment volumes.

## Key Analyses

### 1. Access Analysis
- **Account Ownership Trend (2011–2024):** Growth slowed post-2021, only +3pp despite massive mobile money expansion.  
- **Gender Gap:** Persistent gap between male and female account ownership.  
- **Urban vs. Rural:** Rural access remains lower due to limited infrastructure.  

### 2. Usage Analysis
- **Mobile Money Penetration:** Rapid growth in digital payments post-Telebirr (May 2021) and M-Pesa entry (Aug 2023).  
- **Payment Patterns:** P2P payments dominate, while merchant/bill payments are less common.  
- **Registered vs Active Accounts:** Significant gap, indicating many registered users are inactive.  

### 3. Infrastructure & Enablers
- 4G coverage, mobile penetration, and ATM density positively correlate with account ownership and usage.  
- Infrastructure improvements precede inclusion growth, often with a 6–12 month lag.  

### 4. Event Timeline Analysis
- Telebirr launch (May 2021) → Increase in account ownership  
- M-Pesa entry (Aug 2023) → Surge in mobile money usage  
- Safaricom market entry (Aug 2022) → Boost in 4G coverage and digital payments  

### 5. Correlation Insights
- Access is strongly associated with infrastructure (4G coverage, mobile penetration).  
- Usage is associated with policy events and mobile money platform entries.  
- Impact_links suggest that events like Telebirr and M-Pesa drive indicator improvements over time.  

## Data Quality Assessment
- Confidence levels: 40 high, 3 medium  
- Sparse coverage for some indicators (e.g., `AFF_DATA_INCOME`, `GEN_MM_SHARE`)  
- Missing disaggregations for rural vs urban in some years  
- Gaps limit modeling for certain demographic or geographic subgroups  

## Key Insights
- Account ownership growth slowed post-2021 despite a surge in mobile money registrations.  
- Digital payment usage grew faster than access, indicating uptake is driven by active users rather than new account creation.  
- Infrastructure leads inclusion with a lag; improvements in 4G coverage and ATM density precede increased account ownership and usage.  
- Gender gap remains persistent, with women underrepresented in account ownership and mobile money usage.  
- Data gaps limit rural and income-based analysis, reducing the ability to fully capture disparities in financial inclusion.  

### Ethiopia-Specific Dynamics
- P2P payments dominate usage, unlike in other countries where merchant payments are larger.  
- Mobile money-only users are rare (~0.5%).  
- Bank accounts are generally accessible, but credit penetration is very low.  
- Policy and market events (e.g., Telebirr, M-Pesa) have significant short- and medium-term impacts.  

## Next Steps
- Use insights to inform impact modeling in Task 3  
- Address sparse indicators by integrating additional data sources  
- Explore hypothesis testing for event-to-indicator relationships using impact_links  

## References
- `ethiopia_fi_unified_data.csv`  
- `reference_codes.csv`  
- Additional Data Points Guide (Sheets A–D)  
- Findex surveys, operator reports, regulator data
