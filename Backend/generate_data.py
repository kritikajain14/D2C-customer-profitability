import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

# --- Config ---
N_CUSTOMERS = 10_000
START_DATE = datetime(2023, 1, 1)
CHANNELS = ["instagram", "google", "coupon_site", "organic", "referral"]

# Channel characteristics: (cac, avg_orders, discount_prob, return_prob, churn_month)
CHANNEL_PROFILE = {
    "instagram":   dict(cac=1200, avg_orders=4.5, discount_prob=0.15, return_prob=0.06, churn_month=8),
    "google":      dict(cac=900,  avg_orders=3.2, discount_prob=0.20, return_prob=0.08, churn_month=6),
    "coupon_site": dict(cac=400,  avg_orders=1.8, discount_prob=0.85, return_prob=0.18, churn_month=2),
    "organic":     dict(cac=200,  avg_orders=5.1, discount_prob=0.10, return_prob=0.05, churn_month=10),
    "referral":    dict(cac=350,  avg_orders=3.8, discount_prob=0.12, return_prob=0.07, churn_month=7),
}

CHANNEL_WEIGHTS = [0.25, 0.22, 0.20, 0.18, 0.15]  # acquisition mix

customers = []
transactions = []
txn_id = 1

for cust_id in range(1, N_CUSTOMERS + 1):
    channel = np.random.choice(CHANNELS, p=CHANNEL_WEIGHTS)
    p = CHANNEL_PROFILE[channel]
    
    acq_date = START_DATE + timedelta(days=np.random.randint(0, 180))
    cac = p["cac"] * np.random.uniform(0.7, 1.3)
    
    # How many months does this customer stay active?
    active_months = max(1, int(np.random.exponential(p["churn_month"])))
    active_months = min(active_months, 12)
    
    n_orders = max(1, int(np.random.poisson(p["avg_orders"])))
    
    customers.append({
        "customer_id": cust_id,
        "channel": channel,
        "acquisition_date": acq_date,
        "cac": round(cac, 2),
        "active_months": active_months,
    })
    
    for order_num in range(n_orders):
        # Spread orders across active months
        order_month = random.randint(0, active_months - 1)
        order_date = acq_date + timedelta(days=order_month * 30 + random.randint(0, 29))
        
        # Base AOV ₹950 with variance
        base_aov = np.random.normal(950, 220)
        base_aov = max(200, base_aov)
        
        # Discount logic
        used_discount = np.random.random() < p["discount_prob"]
        discount_pct = 0.30 if used_discount else 0.0
        discount_amount = round(base_aov * discount_pct, 2)
        
        # Return logic
        returned = np.random.random() < p["return_prob"]
        
        revenue = round(base_aov - discount_amount, 2) if not returned else 0.0
        
        transactions.append({
            "txn_id": txn_id,
            "customer_id": cust_id,
            "order_date": order_date,
            "order_month": order_month,
            "base_aov": round(base_aov, 2),
            "discount_amount": discount_amount,
            "used_discount": used_discount,
            "returned": returned,
            "net_revenue": revenue,
        })
        txn_id += 1

df_customers = pd.DataFrame(customers)
df_txns = pd.DataFrame(transactions)

df_customers.to_csv("customers.csv", index=False)
df_txns.to_csv("transactions.csv", index=False)

print("=== Dataset Summary ===")
print(f"Customers: {len(df_customers):,}")
print(f"Transactions: {len(df_txns):,}")
print(f"\nChannel breakdown:")
print(df_customers["channel"].value_counts().to_string())
print(f"\nAvg CAC by channel:")
print(df_customers.groupby("channel")["cac"].mean().round(0).to_string())
print(f"\nDiscount rate by channel:")
print(df_txns.merge(df_customers[["customer_id","channel"]], on="customer_id")
      .groupby("channel")["used_discount"].mean().mul(100).round(1).to_string())
print(f"\nReturn rate by channel:")
print(df_txns.merge(df_customers[["customer_id","channel"]], on="customer_id")
      .groupby("channel")["returned"].mean().mul(100).round(1).to_string())
