D2C Customer Profitability & LTV Analysis

📊 An end-to-end analytics project identifying which acquisition channels actually drive profitable customers for a D2C skincare brand — using Python for data processing and Power BI for visualization.

🎯 Objective

A D2C skincare brand was acquiring customers across 5 channels with no clarity on which ones were actually profitable. High discount spend and early churn were quietly eroding margins.

This project analyzes 10,000 customer records to:


Identify high-LTV vs. low-LTV acquisition channels
Understand cohort churn patterns across the first 6 months
Segment customers by purchasing behavior
Deliver data-backed recommendations to improve marketing ROI


🗂️ Dataset

Records -- 10,000 customers
Channels -- organic, instagram, referral, google, coupon_site
Segments -- True Loyalist, Occasional, Discount Hunter, One-Timer
Cohort window -- 7 months (month_0 → month_6)
Key fields -- Revenue, CAC, Discounts, Orders, LTV, Segment

🛠️ Tools & Stack


Python (Pandas, NumPy) — data cleaning, LTV calculation, customer segmentation
Excel — raw data inspection and initial structuring
Power BI + DAX — dashboard build, calculated measures
Tableau — alternate dashboard visualization


🔁 Pipeline

Raw CSV (10K records)
   │
   ▼
1. Data Cleaning (Python/Pandas)
   - Handle nulls, duplicates, type fixes
   - Standardize channel & segment labels
   │
   ▼
2. LTV & Metric Calculation (Python)
   - Net LTV = Revenue − Discounts − CAC
   - Aggregate by channel & segment
   │
   ▼
3. Customer Segmentation (Python)
   - Rule-based tagging: True Loyalist / Occasional /
     Discount Hunter / One-Timer
   │
   ▼
4. Cohort Retention Calc (Python)
   - Month-on-month retention % per channel
   │
   ▼
5. Power BI Dashboard
   - Channel cards, LTV by channel, retention curves,
     channel performance (CAC/revenue/discount), segment mix

📈 Key Findings

Best channel LTV-- Organic — ₹4,187 LTV at just ₹200 CAC
Worst channel LTV -- Coupon site — ₹741 LTV
True Loyalists -- 57.3% of all customers (5,730 of 10,000)
Discount Hunters -- 9.4% of customers, ₹718 avg discount each


~ Organic delivers 5.6× higher LTV than coupon site, with near-zero CAC — the brand's most profitable cohort.
~ Instagram returns 2.2× LTV-to-CAC and produces the highest volume of True Loyalists (1,817).
~ Coupon-site customers churn fast — retention falls to 23.6% by Month 1 and is nearly gone by Month 2 (10.9% at 60 days), vs. 40–70% retention on every other channel.
~ 89% of all discount hunters came from coupon site (837 of 941), averaging ₹478 in discounts each — net-negative once CAC and discounts are factored in.
~ True Loyalists are concentrated in 4 channels (Instagram, Google, Organic, Referral) — 95% of all loyalists came from these, confirming channel quality drives long-term value.


💡 Recommendations

Immediate


Cap coupon-site ad spend — est. ₹964K/yr saved in discount leakage across 2,017 customers
Reallocate budget to Instagram retargeting — 2.2× LTV:CAC, 76.5% loyalist conversion
Launch a referral incentive program — ₹2,962 avg LTV at ₹347 CAC, ~99% profitable


Long-term
4. Suppress discounts for returning buyers — discount hunters only buy when discounted
5. Invest in organic content (SEO/community) — ₹200 CAC vs. ₹4,187 LTV, best unit economics
6. Build a retention program for True Loyalists — 5,730 customers, ₹3,599 avg LTV, highest-ROI segment to protect

Projected impact: reallocating spend per these findings is projected to lift average LTV per new customer by +₹1,886.


📌 Conclusion

Acquisition channel is the single strongest predictor of customer lifetime value for this D2C brand.
Organic and Instagram produce True Loyalists worth 3–5× the LTV of coupon-site customers, who churn within 60 days and carry heavy discount costs. This dashboard gives stakeholders a real-time view of channel LTV, cohort retention, and segment mix — a data foundation for smarter marketing budget allocation.
