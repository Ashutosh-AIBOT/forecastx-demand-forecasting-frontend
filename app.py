"""
DemandPulse Analytics — Streamlit Dashboard (Full Version)
Author: Ashutosh | Python & Backend Developer

All personal info is defined in the USER PROFILE section at the top.
Update only that section — everything else (footer, about page) pulls from it.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



# ══════════════════════════════════════════════════════════════════════════════
# USER PROFILE — edit only this section
# ══════════════════════════════════════════════════════════════════════════════
USER = {
    "name":        "Ashutosh",
    "role":        "Data Analyst · Business Analytics",
    "college":     "Dr. Ambedkar Institute of Technology for Handicapped",
    "location":    "Kanpur, Uttar Pradesh",
    "phone":       "+91-7390986296",
    "email":       "ashutoshknp12@gmail.com",
    "github":      "https://github.com/Ashutosh-AIBOT",
    "github_repo": "https://github.com/Ashutosh-AIBOT/forecastx-demand-forecasting",
    "linkedin":    "https://linkedin.com/in/ashutosh1975271",
    "huggingface": "https://huggingface.co/Ashutosh1975",
    "portfolio":   "https://ashutosh-aibot.github.io",
    "kaggle":      "https://www.kaggle.com/ashutosh1975270",
    "summary": (
        "Data Analyst with experience building analytics pipelines on 1M+ row datasets. "
        "Detected 18% profit leakage across 96,454 orders, built churn model at 85% ROC-AUC, "
        "and reduced stock-outs by 12% on 1,048,575 records. Skilled in Python, SQL, Power BI (DAX), "
        "ML segmentation, and ETL pipelines. Delivered 6 live applications across Vercel, Render, and HuggingFace Spaces."
    ),
    "skills": [
        "Languages & Databases: Python, SQL, Java, MySQL, PostgreSQL, SQLite",
        "Analytics & ML: Pandas, NumPy, Scikit-learn, XGBoost, Random Forest, KMeans, ARIMA, Prophet, EDA, A/B Testing, RFM, CLV Modeling, Cohort Analysis, Statistics",
        "BI, Visualization & Engineering: Power BI (DAX), Plotly, Matplotlib, Seaborn, Streamlit, ETL Pipelines, Star Schema, Data Warehousing, Web Scraping",
        "Tools & Certifications: Git, GitHub, Docker, Linux · Google Advanced Data Analytics (Coursera) · DSMP CampusX – Python, SQL, ML, DL, GenAI, LLMs",
    ],
    "experience": [
        {
            "title":    "AI/ML Developer Intern",
            "company":  "Enloomed India Pvt. Ltd.",
            "period":   "Dec 2023 – Feb 2024",
            "points": [
                "Built production voice-to-image pipeline using OpenAI Whisper + DALL-E, reducing user input time by 60%.",
                "Developed Streamlit dashboard tracking pipeline KPIs — latency, success rate, generation quality.",
                "Automated audio ingestion using Whisper API for real-time transcription.",
                "Cleaned unstructured audio datasets powering business intelligence pipelines.",
            ],
        }
    ],
    "projects": [
        {
            "name": "Olist E-Commerce Analytics",
            "stack": "Python, SQL, Power BI, Scikit-learn, KMeans, RFM",
            "github": "https://github.com/Ashutosh-AIBOT/olist-ecommerce-analytics",
            "live": "https://ashutosh-aibot-olist-analytics.hf.space",
            "desc": "Analyzed 96,454 orders across 9 tables; built SQL star schema with 12+ revenue and CLV KPIs. Applied RFM segmentation, CLV modeling, and KMeans to identify high-value and churn-risk segments. Built Random Forest churn model achieving 85% ROC-AUC across High, Medium, Low risk tiers. Developed Power BI dashboard detecting 18% profit leakage across 74 categories and 27 states.",
        },
        {
            "name": "ForecastX – Demand Forecasting",
            "stack": "Python, ARIMA, Prophet, SQL, Power BI, Star Schema",
            "github": "https://github.com/Ashutosh-AIBOT/forecastx-demand-forecasting",
            "live": "https://forecast-x-frontend.vercel.app/",
            "desc": "Processed 1,048,575 records across 2,160 products, 33 categories, and 4 warehouses (2011–2017). Built star-schema DWH; cleaned 11,239 null dates and engineered 7 temporal features for modeling. Applied ARIMA + Prophet for 30-day forecasting; optimized reorder points cutting stock-outs by 12%. Deployed interactive Power BI and Tableau dashboards visualizing warehouse KPIs and demand trends.",
        },
        {
            "name": "Social Media Campaign Analytics",
            "stack": "Python, Power BI, Scikit-learn, A/B Testing, KMeans",
            "github": "https://github.com/Ashutosh-AIBOT/social-media-campaign-analytics",
            "live": "https://forecast-x-frontend-vz8c.vercel.app/",
            "desc": "Analyzed ad performance across Facebook, Instagram, Google, LinkedIn computing CTR, ROAS, and ROI. Conducted A/B testing on ad creatives using two-sample t-test; identified significant conversion uplift. Applied KMeans to segment campaigns into High ROAS, Medium, and At-Risk tiers for budget decisions. Built Power BI dashboard with DAX measures for cross-platform KPI comparison and trend analysis.",
        },
    ],
    "achievements": [
        "25+ end-to-end projects across Python backend, REST APIs, Django, GenAI — all on GitHub",
        "200+ LeetCode problems solved (DSA practice)",
        "Built analytics on Olist (96,454 orders) and Product Demand (1,048,575 rows) with full ML pipelines",
        "Google Advanced Data Analytics — Coursera Certified",
        "DSMP CampusX — Python, SQL, ML, DL, GenAI",
        "Microsoft & SAP TechSaksham AI Program",
    ],
}


# ══════════════════════════════════════════════════════════════════════════════
# PROJECT INFO — edit only this section for dataset, pipeline, and tech stack
# ══════════════════════════════════════════════════════════════════════════════

PROJECT_INFO = {
    "name": "ForecastX – Demand Forecasting & Analytics",
    "dataset": {
        "source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/felixzhao/productdemandforecasting",
        "title": "Historical Product Demand",
        "description": (
            "The dataset contains historical product demand for a manufacturing company "
            "with footprints globally. It provides thousands of products within dozens of "
            "product categories, shipped from four central warehouses. The goal is to achieve "
            "accurate monthly demand forecasts to optimize inventory and supply chain."
        ),
        "size": "51.25 MB",
        "rows": "1,048,575",
        "columns": 5,
        "features": ["Product_Code", "Warehouse", "Product_Category", "Date", "Order_Demand"],
        "period": "2011–2017 (7 years)",
        "license": "CC BY-SA 4.0",
    },
    "pipeline": {
        "title": "Project Pipeline",
        "stages": [
            {
                "name": "1. Data Ingestion & Cleaning",
                "tools": ["Pandas", "NumPy"],
                "details": [
                    "Loaded 1M+ rows from CSV",
                    "Parsed dates, handled missing values (11,239 null dates)",
                    "Cleaned and converted 'Order_Demand' column to numeric",
                    "Removed outliers using 99.9th percentile cap",
                ]
            },
            {
                "name": "2. Exploratory Data Analysis (EDA)",
                "tools": ["Pandas", "Matplotlib", "Seaborn"],
                "details": [
                    "Analyzed demand distribution across warehouses, categories, and time",
                    "Generated statistical summaries and identified top products",
                    "Created pivot tables for warehouse-category demand",
                ]
            },
            {
                "name": "3. Static & Interactive Visualizations",
                "tools": ["Matplotlib", "Seaborn", "Plotly"],
                "details": [
                    "Created bar charts, box plots, heatmaps, and Pareto charts for insights",
                    "Built interactive dashboards with Plotly for time series and warehouse analysis",
                    "Developed animated bar race for yearly warehouse demand",
                ]
            },
            {
                "name": "4. SQL Data Warehousing",
                "tools": ["SQLite", "SQL"],
                "details": [
                    "Loaded data into SQLite for complex analytical queries",
                    "Performed aggregations, joins, and window functions for business metrics",
                ]
            },
            {
                "name": "5. Machine Learning – Segmentation & Forecasting",
                "tools": ["Scikit-learn", "XGBoost", "Prophet", "ARIMA"],
                "details": [
                    "Applied K-Means clustering to segment products by demand volume and volatility",
                    "Evaluated models (Random Forest, XGBoost) for demand prediction (R² < 0.20 due to volatility)",
                    "Implemented ARIMA and Prophet for time-series forecasting, reducing stock-outs by 12%",
                ]
            },
            {
                "name": "6. Streamlit Dashboard Deployment",
                "tools": ["Streamlit", "HuggingFace Spaces", "GitHub"],
                "details": [
                    "Built an interactive analytics dashboard with 7+ analytical views",
                    "Integrated ML segmentation and user-driven filters",
                    "Deployed live on HuggingFace Spaces with GitHub version control",
                ]
            },
        ]
    },
    "tech_stack": {
        "title": "🛠️ Technology Stack",
        "categories": {
            "Data Processing": ["Python", "Pandas", "NumPy", "SQLite"],
            "Visualization": ["Matplotlib", "Seaborn", "Plotly", "Power BI (DAX)"],
            "Machine Learning": ["Scikit-learn", "XGBoost", "Prophet", "ARIMA", "KMeans"],
            "Web & Deployment": ["Streamlit", "HuggingFace Spaces", "GitHub"],
        }
    },
    "links": {
        "GitHub Repository": "https://github.com/Ashutosh-AIBOT/forecastx-demand-forecasting",
        "Live Demo (HuggingFace)": "https://huggingface.co/spaces/Ashutosh-AIBOT/forecastx",
        "Dataset (Kaggle)": "https://www.kaggle.com/datasets/felixzhao/productdemandforecasting",
        "Portfolio": "https://ashutosh-aibot.github.io",
    }
}

# ══════════════════════════════════════════════════════════════════════════════


st.set_page_config(page_title="DemandPulse Analytics", page_icon="📦",
                   layout="wide", initial_sidebar_state="expanded")

st.markdown("""<style>
    .main{background-color:#0a0e1a}
    .stMetric{background:#111827;border:1px solid #1e2d42;border-radius:10px;padding:16px}
    .stMetricLabel{color:#94a3b8!important;font-size:12px!important}
    .stMetricValue{color:#f1f5f9!important}
    h1{color:#f1f5f9!important}
    h2,h3{color:#93c5fd!important}
    .insight-box{background:#0f172a;border-left:3px solid #3b82f6;padding:12px 16px;
                 border-radius:4px;margin:8px 0;color:#cbd5e1;font-size:.9rem}
    .good-box{background:#0f2a1a;border-left:3px solid #10b981;padding:12px 16px;
              border-radius:4px;margin:8px 0;color:#a7f3d0;font-size:.9rem}
    .warn-box{background:#2a1f0f;border-left:3px solid #f59e0b;padding:12px 16px;
              border-radius:4px;margin:8px 0;color:#fde68a;font-size:.9rem}
    .footer-box{background:#111827;border:1px solid #1e2d42;border-radius:12px;
                padding:20px;text-align:center;margin-top:40px}
    .profile-card{background:#111827;border:1px solid #1e3a5f;border-radius:14px;padding:28px 20px;text-align:center}
    .link-card{border-radius:12px;padding:20px;text-align:center;transition:all .2s;text-decoration:none;display:block}
    .skill-tag{display:inline-block;background:#1e2d42;color:#93c5fd;border-radius:6px;
               padding:4px 10px;font-size:12px;margin:3px 2px}
</style>""", unsafe_allow_html=True)

plt.rcParams.update({
    'figure.facecolor': '#111827', 'axes.facecolor': '#111827',
    'axes.edgecolor': '#1e2d42',   'axes.labelcolor': '#94a3b8',
    'xtick.color': '#94a3b8',      'ytick.color': '#94a3b8',
    'text.color': '#f1f5f9',       'grid.color': '#1e2d42', 'grid.alpha': 0.6,
})
C = ['#3b82f6', '#06b6d4', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444', '#f472b6', '#34d399']
DAY_NAMES = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',
             4:'Friday', 5:'Saturday', 6:'Sunday'}


# ─────────────────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    import os
    ROOT = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(os.path.join(ROOT, 'data', 'raw', 'Historical Product Demand.csv'))
    df['Order_Demand'] = (df['Order_Demand'].astype(str)
                          .str.replace('(', '', regex=False)
                          .str.replace(')', '', regex=False)
                          .str.strip())
    df['Order_Demand'] = pd.to_numeric(df['Order_Demand'], errors='coerce')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date', 'Order_Demand'])
    df = df[df['Order_Demand'] > 0]
    q999 = df['Order_Demand'].quantile(0.999)
    df = df[df['Order_Demand'] <= q999]
    df = df.groupby(['Product_Code', 'Warehouse', 'Product_Category', 'Date'])[
        'Order_Demand'].sum().reset_index()
    df['Year']       = df['Date'].dt.year
    df['Month']      = df['Date'].dt.month
    df['Quarter']    = df['Date'].dt.quarter
    df['DayOfWeek']  = df['Date'].dt.dayofweek
    df['WeekOfYear'] = df['Date'].dt.isocalendar().week.astype(int)
    return df


def ibox(t): st.markdown(f'<div class="insight-box">💡 {t}</div>', unsafe_allow_html=True)
def gbox(t): st.markdown(f'<div class="good-box">✅ {t}</div>', unsafe_allow_html=True)
def wbox(t): st.markdown(f'<div class="warn-box">⚠️ {t}</div>', unsafe_allow_html=True)
def divider(): st.markdown("<hr style='border-color:#1e2d42;margin:24px 0'>", unsafe_allow_html=True)


def footer():
    st.markdown(f"""<div class="footer-box">
        <div style="font-size:18px;font-weight:600;color:#f1f5f9;margin-bottom:4px">{USER['name']}</div>
        <div style="font-size:13px;color:#3b82f6;margin-bottom:4px">{USER['role']}</div>
        <div style="margin-top:10px;display:flex;justify-content:center;gap:16px;flex-wrap:wrap">
            <a href="{USER['github']}" target="_blank" style="color:#94a3b8;font-size:12px;text-decoration:none">🐙 GitHub</a>
            <a href="{USER['linkedin']}" target="_blank" style="color:#94a3b8;font-size:12px;text-decoration:none">🔗 LinkedIn</a>
            <a href="{USER['huggingface']}" target="_blank" style="color:#94a3b8;font-size:12px;text-decoration:none">🤗 HuggingFace</a>
            <a href="{USER['kaggle']}" target="_blank" style="color:#94a3b8;font-size:12px;text-decoration:none">📂 Kaggle</a>
        </div>
    </div>""", unsafe_allow_html=True)



# ─────────────────────────────────────────────────────────────────────────────
with st.spinner("Loading 1M+ records..."):
    df = load_data()

_n_products   = df['Product_Code'].nunique()
_n_categories = df['Product_Category'].nunique()
_n_warehouses = df['Warehouse'].nunique()
_yr_min       = int(df['Year'].min())
_yr_max       = int(df['Year'].max())
_n_years      = _yr_max - _yr_min + 1
_top_wh       = df.groupby('Warehouse')['Order_Demand'].sum().idxmax()
_top_cat      = df.groupby('Product_Category')['Order_Demand'].sum().idxmax()
_cat_demand   = df.groupby('Product_Category')['Order_Demand'].sum().sort_values(ascending=False)
_top5_share   = round(_cat_demand.head(5).sum() / _cat_demand.sum() * 100, 1)
_q_demand     = df.groupby('Quarter')['Order_Demand'].sum()
_peak_q       = f"Q{_q_demand.idxmax()}"


# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📦 DemandPulse")
    st.markdown("---")
    page = st.radio("Navigation", [
        "👨‍💻 About",
        "📊 Project Info",
        "⚡ Dashboard",
        "🏭 Warehouse Analysis",
        "📦 Product Analysis",
        "📊 Category Analysis",
        "⏰ Time Analysis",
        "🤖 ML Segmentation",
    ])
    
    st.markdown("---")
    st.markdown(f"• **{len(df):,}** records")
    st.markdown(f"• **{_n_products:,}** products")
    st.markdown(f"• **{_n_warehouses}** warehouses")
    st.markdown(f"• **{_n_categories}** categories")
    st.markdown(f"• **{_yr_min}–{_yr_max}** date range")

    if page in ["🏭 Warehouse Analysis", "📦 Product Analysis",
                "📊 Category Analysis", "⏰ Time Analysis"]:
        st.markdown("---")
        yr  = st.multiselect("Year",      sorted(df['Year'].unique()),
                             default=sorted(df['Year'].unique()))
        whs = st.multiselect("Warehouse", df['Warehouse'].unique().tolist(),
                             default=df['Warehouse'].unique().tolist())
    else:
        yr  = sorted(df['Year'].unique())
        whs = df['Warehouse'].unique().tolist()


def fdf():
    return df[(df['Year'].isin(yr)) & (df['Warehouse'].isin(whs))]


# ══════════════════════════════════════════════════════════════════════════════
# ⚡ DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
if page == "⚡ Dashboard":
    st.title("DemandPulse Analytics Dashboard")
    st.caption(
        f"Product Demand Analysis · {_n_warehouses} Warehouses · "
        f"{_n_products:,} Products · {_n_categories} Categories · "
        f"{_yr_min}–{_yr_max}"
    )

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Total Records",  f"{len(df):,}")
    c2.metric("Total Demand",   f"{df['Order_Demand'].sum()/1e9:.2f}B")
    c3.metric("Avg Demand",     f"{df['Order_Demand'].mean():,.0f}")
    c4.metric("Median Demand",  f"{df['Order_Demand'].median():,.0f}")
    c5.metric("Top Warehouse",  _top_wh)
    c6.metric("Top Category",   _top_cat)
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Yearly Demand Trend")
        yr_d = df.groupby('Year')['Order_Demand'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(7, 4))
        bars = ax.bar(yr_d['Year'], yr_d['Order_Demand']/1e6,
                      color=C[0], alpha=0.85, edgecolor='none')
        ax.set_ylabel("Demand (M)"); ax.grid(axis='y', alpha=0.4)
        for b in bars:
            ax.text(b.get_x()+b.get_width()/2, b.get_height()+1,
                    f'{b.get_height():.0f}M', ha='center', fontsize=9)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col2:
        st.subheader("Demand by Warehouse")
        wh_d = df.groupby('Warehouse')['Order_Demand'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(7, 4))
        bars = ax.bar(wh_d['Warehouse'], wh_d['Order_Demand']/1e6,
                      color=C[:4], alpha=0.85, edgecolor='none')
        ax.set_ylabel("Demand (M)"); ax.grid(axis='y', alpha=0.4)
        for b in bars:
            ax.text(b.get_x()+b.get_width()/2, b.get_height()+0.5,
                    f'{b.get_height():.0f}M', ha='center', fontsize=9)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Monthly Demand Pattern")
        mo_d = df.groupby('Month')['Order_Demand'].mean()
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(mo_d.index, mo_d.values/1e3, 'o-', color=C[0], lw=2, ms=6)
        ax.fill_between(mo_d.index, mo_d.values/1e3, alpha=0.2, color=C[0])
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun',
                            'Jul','Aug','Sep','Oct','Nov','Dec'])
        ax.set_ylabel("Avg Demand (K)"); ax.grid(alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col4:
        st.subheader("Demand by Quarter")
        q_d = df.groupby('Quarter')['Order_Demand'].sum()
        fig, ax = plt.subplots(figsize=(7, 4))
        bars_q = ax.bar(['Q1','Q2','Q3','Q4'], q_d.values/1e6,
                        color=C[:4], alpha=0.85, edgecolor='none')
        ax.set_ylabel("Total Demand (M)"); ax.grid(axis='y', alpha=0.4)
        for b in bars_q:
            ax.text(b.get_x()+b.get_width()/2, b.get_height()+0.5,
                    f'{b.get_height():.0f}M', ha='center', fontsize=9)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    st.subheader("Demand Statistics Summary")
    stats = df['Order_Demand'].describe().reset_index()
    stats.columns = ['Statistic', 'Value']
    stats['Value'] = stats['Value'].apply(lambda x: f"{x:,.2f}")
    st.dataframe(stats, use_container_width=True, hide_index=True)

    ibox(
        f"Total demand is {df['Order_Demand'].sum()/1e9:.2f}B units across "
        f"{_n_years} years ({_yr_min}–{_yr_max}). "
        f"{_top_wh} is the dominant warehouse handling the highest share of demand. "
        f"Demand peaks in {_peak_q}."
    )
    footer()



# ══════════════════════════════════════════════════════════════════════════════
# 👨‍💻 ABOUT — pulls everything from USER dict at the top
# ══════════════════════════════════════════════════════════════════════════════
elif page == "👨‍💻 About":

    # ── Hero banner
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0f172a 0%,#1e3a5f 50%,#0f172a 100%);
                border:1px solid #1e3a5f;border-radius:16px;padding:36px 32px;
                text-align:center;margin-bottom:24px">
        <div style="font-size:2rem;color:#f1f5f9;font-weight:700;letter-spacing:-1px;margin-bottom:6px">
            📦 ForecastX
        </div>
        <div style="font-size:1rem;color:#3b82f6;margin-bottom:16px;letter-spacing:0.5px">
            Product Demand Analytics Platform
        </div>
        <div style="font-size:13px;color:#94a3b8;max-width:600px;margin:0 auto;line-height:1.7">
            An end-to-end business analytics dashboard built on the Kaggle Historical
            Product Demand dataset. Covers data cleaning, EDA, warehouse &amp; product
            analysis, seasonality, and ML-based segmentation.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Creator card
    st.subheader("👨‍💻 About the Creator")
    ca, cb = st.columns([1, 2])
    with ca:
        st.markdown(f"""
        <div class="profile-card">
            <div style="font-size:52px;margin-bottom:10px">🧑‍💻</div>
            <div style="font-size:1.05rem;color:#f1f5f9;font-weight:700">{USER['name']}</div>
            <div style="font-size:12px;color:#3b82f6;margin:4px 0">Data Analyst · Business Analytics</div>
            <div style="font-size:11px;color:#64748b;margin-top:6px;line-height:1.7">
                {USER['college']}<br>{USER['location']}
            </div>
            <div style="margin-top:12px;font-size:11px;color:#64748b">
                📞 {USER['phone']}<br>✉️ {USER['email']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with cb:
        skills_html = "".join(f'<span class="skill-tag">{s}</span>' for s in USER['skills'])
        st.markdown(f"""
        <div style="background:#111827;border:1px solid #1e2d42;border-radius:14px;
                    padding:24px;font-size:13px;color:#94a3b8;line-height:1.9">
            <div style="color:#f1f5f9;font-weight:600;margin-bottom:8px;font-size:14px">Summary</div>
            <div style="margin-bottom:14px">{USER['summary']}</div>
            <div style="color:#f1f5f9;font-weight:600;margin-bottom:8px;font-size:13px">Tech Stack</div>
            <div>{skills_html}</div>
        </div>
        """, unsafe_allow_html=True)

    divider()

    # ── Experience
    st.subheader("💼 Experience")
    for exp in USER['experience']:
        points_html = "".join(f"<li style='margin-bottom:4px'>{p}</li>" for p in exp['points'])
        st.markdown(f"""
        <div style="background:#111827;border:1px solid #1e2d42;border-radius:12px;
                    padding:20px;margin-bottom:12px;font-size:13px;color:#94a3b8">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
                <div>
                    <span style="color:#f1f5f9;font-weight:600;font-size:14px">{exp['title']}</span>
                    <span style="color:#3b82f6;margin-left:8px">{exp['company']}</span>
                </div>
                <span style="font-size:12px;color:#64748b">{exp['period']}</span>
            </div>
            <ul style="margin-left:16px;line-height:1.9">{points_html}</ul>
        </div>
        """, unsafe_allow_html=True)

    divider()

    # ── Projects with Dual Links (GitHub + Live Demo)
    st.subheader("🚀 Featured Projects")
    
    # Display projects in 2-column grid
    proj_cols = st.columns(2)
    for i, proj in enumerate(USER['projects']):
        with proj_cols[i % 2]:
            st.markdown(f"""
            <div style="background:#111827;border:1px solid #1e2d42;border-radius:12px;
                        padding:18px;margin-bottom:12px">
                <div style="color:#f1f5f9;font-weight:600;font-size:14px;margin-bottom:6px">
                    📁 {proj['name']}
                </div>
                <div style="font-size:11px;color:#3b82f6;margin-bottom:10px">{proj['stack']}</div>
                <div style="font-size:12px;color:#94a3b8;line-height:1.5;margin-bottom:14px">{proj['desc']}</div>
                <div style="display:flex;gap:12px;margin-top:8px">
                    <a href="{proj['github']}" target="_blank" style="text-decoration:none">
                        <div style="background:#1e2d42;border-radius:8px;padding:6px 12px;display:inline-flex;align-items:center;gap:6px;transition:all 0.2s"
                             onmouseover="this.style.background='#2d3a4e'"
                             onmouseout="this.style.background='#1e2d42'">
                            <span style="font-size:14px">🐙</span>
                            <span style="font-size:11px;color:#93c5fd">GitHub</span>
                        </div>
                    </a>
                    <a href="{proj['live']}" target="_blank" style="text-decoration:none">
                        <div style="background:#1e2d42;border-radius:8px;padding:6px 12px;display:inline-flex;align-items:center;gap:6px;transition:all 0.2s"
                             onmouseover="this.style.background='#2d3a4e'"
                             onmouseout="this.style.background='#1e2d42'">
                            <span style="font-size:14px">🚀</span>
                            <span style="font-size:11px;color:#93c5fd">Live Demo</span>
                        </div>
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    divider()

    # ── Links row (Profiles)
    st.subheader("🔗 Profiles & Links")
    l1, l2, l3, l4, l5 = st.columns(5)
    links = [
        (l1, USER['github_repo'], "#3b82f6", "💻", "GitHub Repo",      "ForecastX source code"),
        (l2, USER['github'],      "#8b5cf6", "🐙", "GitHub Profile",    f"@Ashutosh-AIBOT"),
        (l3, USER['linkedin'],    "#0ea5e9", "🔗", "LinkedIn",          "Connect with me"),
        (l4, USER['huggingface'], "#10b981", "🤗", "HuggingFace",       "Models & Spaces"),
        (l5, USER['kaggle'],      "#f59e0b", "📂", "Kaggle",            "Datasets & notebooks"),
    ]
    for col, url, color, icon, label, sub in links:
        with col:
            st.markdown(f"""
            <a href="{url}" target="_blank" style="text-decoration:none">
            <div style="background:#111827;border:1px solid {color};border-radius:12px;
                        padding:16px;text-align:center">
                <div style="font-size:24px;margin-bottom:6px">{icon}</div>
                <div style="font-size:12px;color:{color};font-weight:600">{label}</div>
                <div style="font-size:10px;color:#64748b;margin-top:3px">{sub}</div>
            </div>
            </a>
            """, unsafe_allow_html=True)

    divider()

    # ── Achievements
    st.subheader("🏆 Achievements & Certifications")
    for item in USER['achievements']:
        st.markdown(f"""
        <div style="display:flex;align-items:flex-start;gap:10px;padding:8px 0;
                    border-bottom:1px solid #1e2d42;font-size:13px;color:#94a3b8">
            <span style="color:#f59e0b;min-width:16px">★</span>
            <span>{item}</span>
        </div>
        """, unsafe_allow_html=True)

    divider()

    # ── Dataset & tech info
    st.subheader("📂 Dataset & Tech Stack")
    d1, d2 = st.columns(2)
    with d1:
        st.markdown("""
        <div style="background:#111827;border:1px solid #1e2d42;border-radius:12px;padding:18px;
                    font-size:12px;color:#94a3b8;line-height:2">
            <div style="color:#f1f5f9;font-weight:600;font-size:13px;margin-bottom:8px">📂 Dataset</div>
            <b style="color:#f1f5f9">Source:</b>
            <a href="https://www.kaggle.com/datasets/felixzhao/productdemandforecasting"
               target="_blank" style="color:#3b82f6">Kaggle — Historical Product Demand</a><br>
            <b style="color:#f1f5f9">Period:</b> 2011–2017 (7 years)<br>
            <b style="color:#f1f5f9">Raw rows:</b> ~1,048,575 records<br>
            <b style="color:#f1f5f9">Warehouses:</b> Whse_A, Whse_C, Whse_J, Whse_S<br>
            <b style="color:#f1f5f9">License:</b> CC BY-SA 4.0
        </div>
        """, unsafe_allow_html=True)

    with d2:
        st.markdown("""
        <div style="background:#111827;border:1px solid #1e2d42;border-radius:12px;padding:18px;
                    font-size:12px;color:#94a3b8;line-height:2">
            <div style="color:#f1f5f9;font-weight:600;font-size:13px;margin-bottom:8px">🛠️ Stack</div>
            <b style="color:#3b82f6">Data:</b> Python · Pandas · NumPy · Matplotlib<br>
            <b style="color:#10b981">ML:</b> Scikit-learn · K-Means · StandardScaler<br>
            <b style="color:#8b5cf6">App:</b> Streamlit<br>
            <b style="color:#f59e0b">Deploy:</b> HuggingFace Spaces · GitHub
        </div>
        """, unsafe_allow_html=True)

    gbox(
        "This project demonstrates end-to-end data analytics skills — "
        "data engineering, EDA, business insight generation, ML modelling, "
        "and production deployment. Built by Ashutosh as a full portfolio project."
    )
    footer()

# ------------------- Project-info---------------------------------------    

elif page == "📊 Project Info":
    
    # ── Hero Banner ──────────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#0f172a 0%,#1e3a5f 50%,#0f172a 100%);
                border:1px solid #1e3a5f;border-radius:20px;padding:32px 28px;
                text-align:center;margin-bottom:28px">
        <div style="font-size:2rem;color:#f1f5f9;font-weight:700;letter-spacing:-1px;margin-bottom:8px">
            📊 {PROJECT_INFO['name']}
        </div>
        <div style="font-size:0.95rem;color:#94a3b8;max-width:750px;margin:0 auto;line-height:1.6">
            End-to-end analytics platform for demand forecasting and business intelligence
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # ── Dataset Overview Section ────────────────────────────────────────────────
    st.subheader("📂 Dataset Overview")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div style="background:#111827;border:1px solid #1e2d42;border-radius:14px;padding:20px;margin-bottom:20px">
            <div style="color:#f1f5f9;font-weight:600;font-size:1rem;margin-bottom:12px">
                📄 {PROJECT_INFO['dataset']['title']}
            </div>
            <div style="font-size:0.85rem;color:#94a3b8;line-height:1.6;margin-bottom:16px">
                {PROJECT_INFO['dataset']['description']}
            </div>
            <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;font-size:0.8rem">
                <div><span style="color:#3b82f6">📦 Source:</span> <a href="{PROJECT_INFO['dataset']['url']}" target="_blank" style="color:#94a3b8;text-decoration:none">Kaggle</a></div>
                <div><span style="color:#3b82f6">📏 Size:</span> <span style="color:#94a3b8">{PROJECT_INFO['dataset']['size']}</span></div>
                <div><span style="color:#3b82f6">📊 Rows:</span> <span style="color:#94a3b8">{PROJECT_INFO['dataset']['rows']}</span></div>
                <div><span style="color:#3b82f6">📋 Columns:</span> <span style="color:#94a3b8">{PROJECT_INFO['dataset']['columns']}</span></div>
                <div><span style="color:#3b82f6">📅 Period:</span> <span style="color:#94a3b8">{PROJECT_INFO['dataset']['period']}</span></div>
                <div><span style="color:#3b82f6">⚖️ License:</span> <span style="color:#94a3b8">{PROJECT_INFO['dataset']['license']}</span></div>
            </div>
            <div style="margin-top:12px;padding-top:12px;border-top:1px solid #1e2d42">
                <span style="color:#3b82f6;font-size:0.8rem">🔍 Features:</span>
                <span style="color:#94a3b8;font-size:0.75rem;margin-left:8px">{', '.join(PROJECT_INFO['dataset']['features'])}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background:#111827;border:1px solid #1e2d42;border-radius:14px;padding:20px;margin-bottom:20px;text-align:center">
            <div style="font-size:2rem;margin-bottom:8px">🎯</div>
            <div style="color:#f1f5f9;font-weight:600;margin-bottom:8px">Challenge</div>
            <div style="font-size:0.8rem;color:#94a3b8;line-height:1.5">
                Forecast monthly demand for 2,160 products across 4 warehouses with 1M+ historical records
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # ── Project Pipeline Section ────────────────────────────────────────────────
    st.subheader("⚙️ Project Pipeline")
    
    # Create a visual pipeline with columns
    stages = PROJECT_INFO['pipeline']['stages']
    cols = st.columns(len(stages))
    
    for idx, (col, stage) in enumerate(zip(cols, stages)):
        with col:
            st.markdown(f"""
            <div style="background:#111827;border:1px solid #1e2d42;border-radius:12px;padding:16px;margin-bottom:12px;height:100%">
                <div style="text-align:center;margin-bottom:12px">
                    <div style="background:#1e2d42;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 10px auto">
                        <span style="color:#3b82f6;font-weight:bold">{idx + 1}</span>
                    </div>
                    <div style="color:#f1f5f9;font-weight:600;font-size:0.85rem">{stage['name']}</div>
                    <div style="font-size:0.7rem;color:#3b82f6;margin:6px 0">{', '.join(stage['tools'])}</div>
                </div>
                <ul style="font-size:0.7rem;color:#94a3b8;margin-left:16px;padding-left:0;line-height:1.5">
                    {"".join(f"<li style='margin-bottom:4px'>{d}</li>" for d in stage['details'][:2])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # Detailed pipeline expander
    with st.expander("🔍 View Complete Pipeline Details", expanded=False):
        for stage in stages:
            st.markdown(f"""
            <div style="background:#111827;border-left:3px solid #3b82f6;border-radius:8px;padding:16px;margin-bottom:16px">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
                    <div style="color:#f1f5f9;font-weight:600">{stage['name']}</div>
                    <div style="font-size:0.7rem;color:#3b82f6">{', '.join(stage['tools'])}</div>
                </div>
                <ul style="margin-left:20px;margin-bottom:0;font-size:0.8rem;color:#94a3b8">
                    {"".join(f"<li>{d}</li>" for d in stage['details'])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # ── Technology Stack Section ────────────────────────────────────────────────
    st.subheader(PROJECT_INFO['tech_stack']['title'])
    
    tech_cols = st.columns(4)
    tech_items = list(PROJECT_INFO['tech_stack']['categories'].items())
    
    for idx, (col, (category, tools)) in enumerate(zip(tech_cols, tech_items)):
        with col:
            st.markdown(f"""
            <div style="background:#111827;border:1px solid #1e2d42;border-radius:12px;padding:14px;margin-bottom:12px">
                <div style="color:#3b82f6;font-weight:600;font-size:0.8rem;margin-bottom:10px">{category}</div>
                <div style="display:flex;flex-wrap:wrap;gap:6px">
                    {"".join(f'<span style="background:#1e2d42;color:#93c5fd;border-radius:6px;padding:3px 8px;font-size:0.7rem">{tool}</span>' for tool in tools)}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # ── Project Links Section ──────────────────────────────────────────────────
    st.subheader("🔗 Quick Links")
    
    link_cols = st.columns(4)
    link_icons = {
        "GitHub Repository": "🐙",
        "Live Demo (HuggingFace)": "🤗",
        "Dataset (Kaggle)": "📂",
        "Portfolio": "🌐"
    }
    
    for idx, (col, (name, url)) in enumerate(zip(link_cols, PROJECT_INFO['links'].items())):
        with col:
            st.markdown(f"""
            <a href="{url}" target="_blank" style="text-decoration:none">
                <div style="background:#111827;border:1px solid #3b82f6;border-radius:12px;padding:16px;text-align:center;transition:all 0.2s"
                     onmouseover="this.style.borderColor='#60a5fa';this.style.transform='translateY(-2px)'"
                     onmouseout="this.style.borderColor='#3b82f6';this.style.transform='translateY(0)'">
                    <div style="font-size:24px;margin-bottom:8px">{link_icons.get(name, "🔗")}</div>
                    <div style="font-size:12px;color:#3b82f6;font-weight:500">{name}</div>
                    <div style="font-size:9px;color:#64748b;margin-top:4px;word-break:break-all">{url.split('/')[-2] if 'github' in url else url.split('/')[-1]}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)
    
    # ── Key Metrics Section ────────────────────────────────────────────────────
    st.subheader("📈 Key Project Metrics")
    
    metric_cols = st.columns(4)
    metrics = [
        ("📊 Total Records", f"{int(PROJECT_INFO['dataset']['rows'].replace(',', '')):,}", "rows processed"),
        ("🏭 Warehouses", "4", "Whse_A, Whse_C, Whse_J, Whse_S"),
        ("📦 Products", "2,160", "across 33 categories"),
        ("📉 Stock-out Reduction", "12%", "via ML forecasting"),
    ]
    
    for col, (label, value, desc) in zip(metric_cols, metrics):
        with col:
            st.metric(
                label=label,
                value=value,
                delta=desc,
                delta_color="off"
            )
    
    # ── Closing Note ──────────────────────────────────────────────────────────
    divider()
    gbox(
        "This project demonstrates end-to-end data analytics skills — "
        "data engineering, EDA, business insight generation, ML modelling, "
        "and production deployment. Built by Ashutosh as a full portfolio project."
    )
    footer()

# ══════════════════════════════════════════════════════════════════════════════
# 🏭 WAREHOUSE ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🏭 Warehouse Analysis":
    st.title("Warehouse Analysis")
    st.caption(f"Performance comparison across {_n_warehouses} warehouses")
    d = fdf()

    wh = d.groupby('Warehouse').agg(
        total     =('Order_Demand', 'sum'),
        avg       =('Order_Demand', 'mean'),
        records   =('Order_Demand', 'count'),
        products  =('Product_Code', 'nunique'),
        categories=('Product_Category', 'nunique')
    ).reset_index()

    cols = st.columns(len(wh))
    for i, (_, r) in enumerate(wh.iterrows()):
        cols[i].metric(r['Warehouse'], f"{r['total']/1e6:.1f}M",
                       f"{r['products']} products")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Demand Share by Warehouse")
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.pie(wh['total'], labels=wh['Warehouse'], colors=C[:len(wh)],
               autopct='%1.1f%%', startangle=90, pctdistance=0.75)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col2:
        st.subheader("Avg Order Demand by Warehouse")
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.bar(wh['Warehouse'], wh['avg'], color=C[:len(wh)],
               alpha=0.85, edgecolor='none')
        ax.set_ylabel("Avg Demand"); ax.grid(axis='y', alpha=0.4)
        for i, v in enumerate(wh['avg']):
            ax.text(i, v+50, f'{v:,.0f}', ha='center', fontsize=9)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    st.subheader("Yearly Demand Trend by Warehouse")
    yr_wh = d.groupby(['Year','Warehouse'])['Order_Demand'].sum().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(12, 5))
    for i, w in enumerate(yr_wh.columns):
        ax.plot(yr_wh.index, yr_wh[w]/1e6, 'o-', label=w, color=C[i], lw=2, ms=5)
    ax.set_ylabel("Demand (M)"); ax.legend(); ax.grid(alpha=0.4)
    fig.tight_layout(); st.pyplot(fig); plt.close()

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Demand Records by Warehouse")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(wh['Warehouse'], wh['records'], color=C[:len(wh)],
               alpha=0.85, edgecolor='none')
        ax.set_ylabel("Demand Records"); ax.grid(axis='y', alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col4:
        st.subheader("Unique Products per Warehouse")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(wh['Warehouse'], wh['products'], color=C[:len(wh)],
               alpha=0.85, edgecolor='none')
        ax.set_ylabel("Unique Products"); ax.grid(axis='y', alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    st.subheader("Warehouse Performance Table")
    wh_disp = wh.copy()
    wh_disp['Total Demand (M)'] = (wh_disp['total']/1e6).round(2)
    wh_disp['Avg Demand']       = wh_disp['avg'].round(0)
    wh_disp['Demand Records']   = wh_disp['records']
    wh_disp['Unique Products']  = wh_disp['products']
    wh_disp['Categories']       = wh_disp['categories']
    st.dataframe(
        wh_disp[['Warehouse','Total Demand (M)','Avg Demand',
                  'Demand Records','Unique Products','Categories']],
        use_container_width=True, hide_index=True
    )

    best   = wh.loc[wh['total'].idxmax(), 'Warehouse']
    second = wh.sort_values('total', ascending=False).iloc[1]['Warehouse']
    ibox(
        f"{best} handles the highest demand volume. "
        f"Consider load balancing with {second} for operational resilience."
    )
    footer()


# ══════════════════════════════════════════════════════════════════════════════
# 📦 PRODUCT ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📦 Product Analysis":
    st.title("Product Analysis")
    st.caption("Top products by demand, frequency and warehouse distribution")
    d = fdf()

    prod_total  = d.groupby('Product_Code')['Order_Demand'].sum()
    top10_share = round(prod_total.nlargest(10).sum() / prod_total.sum() * 100, 1)

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Products",  f"{d['Product_Code'].nunique():,}")
    c2.metric("Total Demand",    f"{d['Order_Demand'].sum()/1e6:.1f}M")
    c3.metric("Avg per Product", f"{prod_total.mean():,.0f}")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 15 Products by Total Demand")
        top15 = prod_total.nlargest(15).reset_index()
        fig, ax = plt.subplots(figsize=(7, 6))
        ax.barh(top15['Product_Code'], top15['Order_Demand']/1e6,
                color=C[0], alpha=0.85, edgecolor='none')
        ax.set_xlabel("Demand (M)"); ax.grid(axis='x', alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col2:
        st.subheader("Top 15 Products by Order Frequency")
        top15f = d.groupby('Product_Code').size().nlargest(15).reset_index()
        top15f.columns = ['Product_Code', 'Records']
        fig, ax = plt.subplots(figsize=(7, 6))
        ax.barh(top15f['Product_Code'], top15f['Records'],
                color=C[2], alpha=0.85, edgecolor='none')
        ax.set_xlabel("Demand Records"); ax.grid(axis='x', alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Top Products by Avg Order Size")
        top_avg = d.groupby('Product_Code')['Order_Demand'].mean().nlargest(10).reset_index()
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.barh(top_avg['Product_Code'], top_avg['Order_Demand']/1e3,
                color=C[3], alpha=0.85, edgecolor='none')
        ax.set_xlabel("Avg Demand (K)"); ax.grid(axis='x', alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col4:
        st.subheader("Demand Distribution — Top 5 Products (Log Scale)")
        top5_prods = prod_total.nlargest(5).index.tolist()
        bp_data    = [np.log1p(d[d['Product_Code']==p]['Order_Demand'].values)
                      for p in top5_prods]
        short_lbl  = [p.replace('Product_','P') for p in top5_prods]
        fig, ax = plt.subplots(figsize=(7, 5))
        parts = ax.violinplot(bp_data, positions=range(1, len(top5_prods)+1),
                              showmedians=True, showextrema=True)
        for i, pc in enumerate(parts['bodies']):
            pc.set_facecolor(C[i]); pc.set_alpha(0.65)
        parts['cmedians'].set_color('#f1f5f9')
        parts['cmins'].set_color('#94a3b8')
        parts['cmaxes'].set_color('#94a3b8')
        parts['cbars'].set_color('#94a3b8')
        ax.set_xticks(range(1, len(top5_prods)+1))
        ax.set_xticklabels(short_lbl)
        ax.set_ylabel("log(1 + Order Demand)")
        ax.grid(axis='y', alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    st.subheader("Top Products by Warehouse")
    for wh_name in sorted(d['Warehouse'].unique()):
        with st.expander(f"Top 5 Products — {wh_name}"):
            top_wh = (d[d['Warehouse']==wh_name]
                      .groupby('Product_Code')['Order_Demand'].sum()
                      .nlargest(5).reset_index())
            top_wh['Demand (M)'] = (top_wh['Order_Demand']/1e6).round(3)
            st.dataframe(top_wh[['Product_Code','Demand (M)']],
                         hide_index=True, use_container_width=True)

    ibox(
        f"Top 10 products account for {top10_share}% of total demand. "
        "Focus procurement and safety stock on these high-impact SKUs."
    )
    footer()


# ══════════════════════════════════════════════════════════════════════════════
# 📊 CATEGORY ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📊 Category Analysis":
    st.title("Category Analysis")
    st.caption(f"{_n_categories} product categories analyzed by demand, warehouse and time")
    d = fdf()

    cat_demand      = d.groupby('Product_Category')['Order_Demand'].sum()
    top_cat_dyn     = cat_demand.idxmax()
    top5_share_dyn  = round(cat_demand.nlargest(5).sum() / cat_demand.sum() * 100, 1)
    avg_cat_demand  = cat_demand.mean()

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Categories", _n_categories)
    c2.metric("Top Category",     top_cat_dyn)
    c3.metric("Avg per Category", f"{avg_cat_demand/1e6:.2f}M")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 15 Categories by Total Demand")
        cat15 = cat_demand.nlargest(15).reset_index()
        fig, ax = plt.subplots(figsize=(7, 6))
        ax.barh(cat15['Product_Category'], cat15['Order_Demand']/1e6,
                color=C[1], alpha=0.85, edgecolor='none')
        ax.set_xlabel("Demand (M)"); ax.grid(axis='x', alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col2:
        st.subheader("Category Demand by Warehouse (Top 5)")
        top5_cats = cat_demand.nlargest(5).index
        cat_wh = (d[d['Product_Category'].isin(top5_cats)]
                  .groupby(['Product_Category','Warehouse'])['Order_Demand']
                  .sum().unstack(fill_value=0))
        fig, ax = plt.subplots(figsize=(7, 6))
        x = np.arange(len(cat_wh)); w = 0.2
        for i, wh in enumerate(cat_wh.columns):
            ax.bar(x + i*w - w*1.5, cat_wh[wh]/1e6, w,
                   label=wh, color=C[i], alpha=0.85)
        ax.set_xticks(x)
        ax.set_xticklabels([c.replace('Category_', 'C') for c in cat_wh.index], rotation=20)
        ax.set_ylabel("Demand (M)"); ax.legend(); ax.grid(axis='y', alpha=0.3)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Category Demand Trend (Top 3)")
        top3_cats = cat_demand.nlargest(3).index
        cat_yr = (d[d['Product_Category'].isin(top3_cats)]
                  .groupby(['Year','Product_Category'])['Order_Demand']
                  .sum().unstack(fill_value=0))
        fig, ax = plt.subplots(figsize=(7, 5))
        for i, cat in enumerate(cat_yr.columns):
            ax.plot(cat_yr.index, cat_yr[cat]/1e6, 'o-',
                    label=cat, color=C[i], lw=2)
        ax.set_ylabel("Demand (M)"); ax.legend(fontsize=9); ax.grid(alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col4:
        st.subheader("Products per Category (Top 10)")
        cat_prod = (d.groupby('Product_Category')['Product_Code']
                    .nunique().nlargest(10).reset_index())
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.barh(cat_prod['Product_Category'], cat_prod['Product_Code'],
                color=C[4], alpha=0.85, edgecolor='none')
        ax.set_xlabel("Unique Products"); ax.grid(axis='x', alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    st.subheader("Full Category Table")
    cat_table = d.groupby('Product_Category').agg(
        Total_Demand =('Order_Demand', 'sum'),
        Avg_Demand   =('Order_Demand', 'mean'),
        Total_Records=('Order_Demand', 'count'),
        Products     =('Product_Code', 'nunique')
    ).reset_index().sort_values('Total_Demand', ascending=False)
    cat_table['Total_Demand'] = (cat_table['Total_Demand']/1e6).round(2)
    cat_table['Avg_Demand']   = cat_table['Avg_Demand'].round(0)
    st.dataframe(
        cat_table.rename(columns={
            'Total_Demand':  'Demand (M)',
            'Avg_Demand':    'Avg Demand',
            'Total_Records': 'Demand Records'
        }),
        use_container_width=True, hide_index=True
    )
    ibox(
        f"{top_cat_dyn} is the highest-demand category. "
        f"Top 5 categories account for {top5_share_dyn}% of all demand — "
        "prioritize these for inventory planning and supplier negotiations."
    )
    footer()


# ══════════════════════════════════════════════════════════════════════════════
# ⏰ TIME ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "⏰ Time Analysis":
    st.title("Time-Based Analysis")
    st.caption("Seasonality, day-of-week and yearly demand patterns")
    d = fdf()

    mo_means   = d.groupby('Month')['Order_Demand'].mean()
    peak_month = mo_means.idxmax()
    month_names = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
                   7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    q_totals = d.groupby('Quarter')['Order_Demand'].sum()
    peak_qtr = f"Q{q_totals.idxmax()}"

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Monthly Demand Pattern")
        mo = d.groupby('Month')['Order_Demand'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(7, 4))
        bars_m = ax.bar(mo['Month'], mo['Order_Demand']/1e3,
                        color=C[0], alpha=0.85, edgecolor='none')
        bars_m[peak_month - 1].set_color(C[4])
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun',
                            'Jul','Aug','Sep','Oct','Nov','Dec'], rotation=30)
        ax.set_ylabel("Avg Demand (K)"); ax.grid(axis='y', alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col2:
        st.subheader("Day of Week Pattern")
        dow = d.groupby('DayOfWeek')['Order_Demand'].mean().reset_index()
        dow['Day'] = dow['DayOfWeek'].map(DAY_NAMES)
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(dow['Day'], dow['Order_Demand']/1e3,
               color=C[2], alpha=0.85, edgecolor='none')
        ax.set_ylabel("Avg Demand (K)"); ax.grid(axis='y', alpha=0.4)
        ax.tick_params(axis='x', rotation=30)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Quarterly Demand by Year")
        qy = d.groupby(['Year','Quarter'])['Order_Demand'].sum().unstack(fill_value=0)
        fig, ax = plt.subplots(figsize=(7, 4))
        x = np.arange(len(qy)); w = 0.2
        for i, q in enumerate(qy.columns):
            ax.bar(x + i*w - w*1.5, qy[q]/1e6, w,
                   label=f'Q{q}', color=C[i], alpha=0.85)
        ax.set_xticks(x); ax.set_xticklabels(qy.index)
        ax.set_ylabel("Demand (M)"); ax.legend(); ax.grid(axis='y', alpha=0.3)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col4:
        st.subheader("Week of Year Heatmap")
        wk = d.groupby(['Year','WeekOfYear'])['Order_Demand'].mean().unstack(fill_value=0)
        fig, ax = plt.subplots(figsize=(7, 4))
        im = ax.imshow(wk.values/1e3, aspect='auto', cmap='YlOrRd')
        ax.set_yticks(range(len(wk.index))); ax.set_yticklabels(wk.index)
        ax.set_xlabel("Week of Year"); ax.set_ylabel("Year")
        plt.colorbar(im, ax=ax, label='Avg Demand (K)')
        fig.tight_layout(); st.pyplot(fig); plt.close()

    st.subheader("Monthly Demand Trend (All Years)")
    monthly_all = (d.groupby(d['Date'].dt.to_period('M'))['Order_Demand']
                   .sum().reset_index())
    monthly_all['Date'] = monthly_all['Date'].dt.to_timestamp()
    monthly_all = monthly_all.sort_values('Date')
    fig, ax = plt.subplots(figsize=(14, 4))
    ax.plot(monthly_all['Date'], monthly_all['Order_Demand']/1e6,
            color=C[0], lw=1.5)
    ax.fill_between(monthly_all['Date'], monthly_all['Order_Demand']/1e6,
                    alpha=0.2, color=C[0])
    ax.set_ylabel("Demand (M)"); ax.grid(alpha=0.3)
    fig.tight_layout(); st.pyplot(fig); plt.close()

    ibox(
        f"Demand peaks in {month_names[peak_month]} on a monthly basis and "
        f"in {peak_qtr} on a quarterly basis. "
        f"Plan inventory replenishment 6–8 weeks before these peak periods."
    )
    footer()


# ══════════════════════════════════════════════════════════════════════════════
# 🤖 ML SEGMENTATION
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🤖 ML Segmentation":
    st.title("ML Segmentation — K-Means Product Clustering")
    st.caption(
        "Products segmented by demand volume, frequency and volatility. "
        "Validated with Elbow curve and Silhouette score."
    )
    st.info(
        "Demand prediction (regression) was evaluated on this dataset but yielded "
        "R² < 0.20 across all models due to high demand volatility and limited features. "
        "K-Means segmentation produces reliable, actionable clusters instead."
    )

    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import silhouette_score

    with st.spinner("Running K-Means segmentation..."):
        ps = df.groupby('Product_Code').agg(
            total=('Order_Demand', 'sum'),
            avg  =('Order_Demand', 'mean'),
            count=('Order_Demand', 'count'),
            std  =('Order_Demand', 'std')
        ).fillna(0).reset_index()

        X_seg = StandardScaler().fit_transform(ps[['total','avg','count','std']])

        inertias   = []
        sil_scores = []
        K_range    = range(2, 9)
        for k in K_range:
            km     = KMeans(n_clusters=k, random_state=42, n_init=10)
            labels = km.fit_predict(X_seg)
            inertias.append(km.inertia_)
            sil_scores.append(
                silhouette_score(X_seg, labels, sample_size=min(5000, len(X_seg)))
            )

        sil_k4          = sil_scores[2]
        sil_optimal_idx = int(np.argmax(sil_scores))
        sil_optimal_k   = list(K_range)[sil_optimal_idx]
        sil_optimal_val = sil_scores[sil_optimal_idx]

        km4 = KMeans(n_clusters=4, random_state=42, n_init=10)
        ps['Segment'] = km4.fit_predict(X_seg)

        seg_stats = ps.groupby('Segment').agg(
            mean_total=('total', 'mean'),
            mean_std  =('std',   'mean')
        ).reset_index()
        global_total_median = ps['total'].median()
        global_std_median   = ps['std'].median()

        def assign_label(row):
            high_vol = row['mean_total'] >= global_total_median
            high_std = row['mean_std']   >= global_std_median
            if high_vol and not high_std:    return "High Volume Stable"
            if high_vol and high_std:        return "High Volume Volatile"
            if not high_vol and not high_std: return "Low Volume Steady"
            return "Low Volume Sporadic"

        seg_stats['Label'] = seg_stats.apply(assign_label, axis=1)
        label_map = dict(zip(seg_stats['Segment'], seg_stats['Label']))
        ps['Label'] = ps['Segment'].map(label_map)

    st.subheader("🔍 Cluster Validation")
    col_v1, col_v2, col_v3, col_v4 = st.columns(4)
    col_v1.metric("Chosen k (Business)", "4")
    col_v2.metric("Silhouette @ k=4",    f"{sil_k4:.4f}")
    col_v3.metric("Statistical Best k",  str(sil_optimal_k))
    col_v4.metric(f"Silhouette @ k={sil_optimal_k}", f"{sil_optimal_val:.4f}")

    inertia_arr = np.array(inertias)
    drops       = np.diff(inertia_arr)
    accel       = np.diff(drops)
    elbow_idx   = int(np.argmax(accel)) + 1
    elbow_k     = list(K_range)[elbow_idx]

    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.subheader("Elbow Curve")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(list(K_range), inertias, 'o-', color=C[0], lw=2)
        ax.axvline(elbow_k, color='#f59e0b', ls=':', lw=1.8, label=f'k={elbow_k} elbow')
        ax.axvline(4, color='#ef4444', ls='--', lw=1.5, label='k=4 chosen')
        ax.set_xlabel("k"); ax.set_ylabel("Inertia")
        ax.legend(fontsize=8); ax.grid(alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col_e2:
        st.subheader("Silhouette Score by k")
        k_list = list(K_range)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(k_list, sil_scores, 'o-', color=C[1], lw=2)
        for k_val, s_val in zip(k_list, sil_scores):
            ax.annotate(f'{s_val:.3f}', (k_val, s_val),
                        textcoords='offset points', xytext=(0, 7),
                        ha='center', fontsize=7, color='#94a3b8')
        ax.axvline(sil_optimal_k, color='#10b981', ls='--', lw=1.5,
                   label=f'k={sil_optimal_k} best ({sil_optimal_val:.3f})')
        if sil_optimal_k != 4:
            ax.axvline(4, color='#ef4444', ls='--', lw=1.5,
                       label=f'k=4 chosen ({sil_k4:.3f})')
        ax.set_xlabel("k"); ax.set_ylabel("Silhouette Score")
        ax.legend(fontsize=8); ax.grid(alpha=0.4)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    sil_above_k4 = [(list(K_range)[i], s) for i, s in enumerate(sil_scores)
                    if s > sil_k4 and list(K_range)[i] != sil_optimal_k and list(K_range)[i] != 4]

    if sil_optimal_k == 4:
        gbox(f"Silhouette peaks at k=4 ({sil_k4:.4f}) — statistically and for business interpretability k=4 is the best choice.")
    else:
        sil_gap    = sil_optimal_val - sil_k4
        extra_note = ""
        if sil_above_k4:
            ks_above   = ", ".join([f"k={k} ({s:.3f})" for k, s in sil_above_k4])
            extra_note = f" Note also that {ks_above} score higher than k=4."
        wbox(
            f"Statistical best: k={sil_optimal_k} (silhouette {sil_optimal_val:.4f}). "
            f"Elbow inflection: k={elbow_k}. Chosen: k=4 (silhouette {sil_k4:.4f}, "
            f"gap of {sil_gap:.4f} vs best). k=4 is selected for business interpretability."
            + extra_note
        )
    st.metric("Products Segmented", f"{len(ps):,}")
    st.markdown("---")

    st.subheader("🔮 Product Segments")
    col5, col6 = st.columns(2)
    with col5:
        sc = ps['Label'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.pie(sc.values, labels=sc.index, colors=C[:4],
               autopct='%1.1f%%', startangle=90)
        ax.set_title("Products by Segment")
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col6:
        ss = ps.groupby('Label').agg(
            Products    =('Product_Code', 'count'),
            Avg_Demand  =('avg',          'mean'),
            Total_Demand=('total',        'sum'),
            Avg_Std     =('std',          'mean')
        ).reset_index()
        ss['Total (M)']  = (ss['Total_Demand']/1e6).round(2)
        ss['Avg Demand'] = ss['Avg_Demand'].round(0)
        ss['Avg Std Dev']= ss['Avg_Std'].round(0)
        st.dataframe(
            ss[['Label','Products','Avg Demand','Avg Std Dev','Total (M)']],
            use_container_width=True, hide_index=True
        )

    st.subheader("Cluster Scatter — Total Demand vs Volatility")
    label_order = list(ps['Label'].unique())
    fig, ax = plt.subplots(figsize=(10, 5))
    for i, label in enumerate(label_order):
        sub = ps[ps['Label'] == label]
        ax.scatter(sub['total']/1e6, sub['std']/1e3,
                   label=label, alpha=0.45, s=16, color=C[i])
    ax.set_xlabel("Total Demand (M)"); ax.set_ylabel("Std Dev (K)")
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout(); st.pyplot(fig); plt.close()

    st.subheader("Top 5 Products per Segment")
    for label in label_order:
        with st.expander(f"Top 5 — {label}"):
            top_seg = (ps[ps['Label']==label]
                       .nlargest(5, 'total')
                       [['Product_Code','total','avg','std','count']]).copy()
            top_seg['Total (M)'] = (top_seg['total']/1e6).round(3)
            top_seg['Avg Demand']= top_seg['avg'].round(0)
            top_seg['Std Dev']   = top_seg['std'].round(0)
            top_seg['Records']   = top_seg['count']
            st.dataframe(
                top_seg[['Product_Code','Total (M)','Avg Demand','Std Dev','Records']],
                hide_index=True, use_container_width=True
            )

    st.subheader("Segment Action Guide")
    actions = {
        "High Volume Stable":    "🟢 Reliable — automate replenishment, negotiate volume discounts.",
        "High Volume Volatile":  "🔴 Priority — maintain high safety stock, monitor weekly.",
        "Low Volume Steady":     "🟡 Efficient — lean inventory, regular reorder points.",
        "Low Volume Sporadic":   "⚪ Review — assess SKU viability, consider make-to-order.",
    }
    for label, action in actions.items():
        if label in ps['Label'].values:
            count = (ps['Label']==label).sum()
            ibox(f"**{label}** ({count} products): {action}")

    footer()

