import streamlit as st

st.set_page_config(
    page_title="GraphShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ GraphShield AI")
st.subheader(
    "AI Powered Fraud Detection using Machine Learning and Graph Neural Networks"
)

st.divider()

# =====================================================
# Overview
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Models", 4)

with col2:
    st.metric("API", "Running")

with col3:
    st.metric("Dataset", "PaySim")

st.divider()

# =====================================================
# Project Modules
# =====================================================

st.header("📦 Project Modules")

c1, c2 = st.columns(2)

with c1:
    st.success("✅ Random Forest")
    st.success("✅ XGBoost")
    st.success("✅ GCN")

with c2:
    st.success("✅ GraphSAGE")
    st.success("✅ SHAP Explainability")
    st.success("✅ Fraud Ring Detection")

st.divider()

# =====================================================
# Project Workflow
# =====================================================

st.header("🔄 Project Workflow")

st.markdown("""
```text
             PaySim Dataset
                    │
                    ▼
          Data Validation & EDA
                    │
                    ▼
      Customer Transaction Graph
                    │
        Graph Feature Engineering
                    │
     ┌──────────────┴──────────────┐
     ▼                             ▼
 Random Forest                 XGBoost
     ▼                             ▼
 Graph Neural Networks (GCN & GraphSAGE)
                    │
                    ▼
        Fraud Ring Detection
                    │
                    ▼
        Customer Risk Scoring
                    │
                    ▼
         SHAP Explainability
                    │
                    ▼
          FastAPI Prediction API
                    │
                    ▼
          Streamlit Dashboard
```
""")