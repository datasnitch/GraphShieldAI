# 🛡️ GraphShield AI

> AI-Powered Fraud Detection using Machine Learning, Graph Neural Networks (GNNs), FastAPI, and Streamlit Dashboard.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-success)
![PyTorch](https://img.shields.io/badge/PyTorch-Geometric-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Project Overview

GraphShield AI is an end-to-end AI-powered fraud detection system that combines **Machine Learning**, **Graph Analytics**, and **Graph Neural Networks** to detect fraudulent financial transactions.

The project builds a customer transaction network, identifies suspicious fraud rings, computes graph-based customer risk scores, trains multiple ML and GNN models, explains predictions using SHAP, exposes a FastAPI prediction service, and provides an interactive Streamlit dashboard.

---

# 🚀 Features

- 🔍 Fraud Detection using Random Forest
- ⚡ Fraud Detection using XGBoost
- 🧠 Graph Convolutional Network (GCN)
- 🌐 GraphSAGE
- 🕸 Customer Transaction Graph
- 🚨 Fraud Ring Detection
- 📊 Customer Risk Scoring
- 📈 Graph Analytics
- 🔎 SHAP Explainability
- 🌍 FastAPI REST API
- 📖 Swagger API Documentation
- 🎯 Streamlit Dashboard
- ⚡ Live Fraud Prediction

---

# 🏗️ Project Architecture

```text
                 PaySim Dataset
                        │
                        ▼
              Data Validation & EDA
                        │
                        ▼
          Customer Transaction Graph
                        │
      ┌─────────────────┴─────────────────┐
      ▼                                   ▼
Graph Features                  Fraud Ring Detection
      │                                   │
      └───────────────┬───────────────────┘
                      ▼
          Customer Feature Engineering
                      │
      ┌───────────────┴──────────────────┐
      ▼                                  ▼
Traditional ML                    Graph Neural Networks
(Random Forest)                     (GCN, GraphSAGE)
(XGBoost)
      │                                  │
      └───────────────┬──────────────────┘
                      ▼
             Model Comparison
                      ▼
          SHAP Explainability
                      ▼
           FastAPI Prediction API
                      ▼
           Streamlit Dashboard
```

---

# 🛠️ Technologies Used

## Programming

- Python

## Machine Learning

- Scikit-Learn
- XGBoost

## Graph Machine Learning

- PyTorch Geometric
- NetworkX

## Explainable AI

- SHAP

## Backend

- FastAPI
- Uvicorn

## Dashboard

- Streamlit

## Data Processing

- Pandas
- NumPy

## Visualization

- Matplotlib

---

# 📂 Project Structure

```text
GraphShieldAI/
│
├── api/
│
├── dashboard/
│   ├── app.py
│   └── pages/
│
├── src/
│   ├── analysis/
│   ├── explainability/
│   ├── features/
│   ├── fraud_ring/
│   ├── gnn/
│   ├── graph/
│   ├── models/
│   └── preprocessing/
│
├── outputs/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 📊 Machine Learning Models

| Model | Purpose |
|--------|---------|
| Random Forest | Baseline Fraud Detection |
| XGBoost | Gradient Boosting Fraud Detection |
| GCN | Graph Neural Network |
| GraphSAGE | Inductive Graph Learning |

---

# 📈 Graph Analytics

GraphShield AI computes:

- Degree
- In Degree
- Out Degree
- PageRank
- Betweenness Centrality
- Clustering Coefficient

These graph metrics are used to generate customer risk scores and improve fraud detection.

---

# 🚨 Fraud Ring Detection

The project identifies suspicious customer communities using graph connectivity.

Features include:

- Weakly Connected Components
- Fraud Ring Identification
- Community Ranking
- Fraud Ring Report Generation

---

# 🧠 Explainable AI

SHAP (SHapley Additive exPlanations) is used to explain model predictions.

Generated outputs include:

- SHAP Summary Plot
- SHAP Feature Importance Plot
- Feature Importance Report

---

# 🌐 REST API

GraphShield AI provides a FastAPI backend for real-time predictions.

### Swagger Documentation

```
http://127.0.0.1:8000/docs
```

### Prediction Endpoint

```
POST /predict
```

### Example Request

```json
{
  "type": "TRANSFER",
  "amount": 50000,
  "oldbalanceOrg": 100000,
  "newbalanceOrig": 50000,
  "oldbalanceDest": 0,
  "newbalanceDest": 50000
}
```

### Example Response

```json
{
  "prediction": 0,
  "fraud_probability": 0.0003,
  "risk_level": "Low"
}
```

---

# 📺 Dashboard

The Streamlit dashboard includes:

- 📊 Dashboard Overview
- 🤖 Model Comparison
- 🌐 Graph Analytics
- 🚨 Fraud Rings
- 🧠 SHAP Explainability
- ⚡ Live Prediction

Run the dashboard:

```bash
streamlit run dashboard/app.py
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/datasnitch/GraphShieldAI.git
```

Navigate to the project:

```bash
cd GraphShieldAI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

### Train Models

```bash
python main.py
```

### Start FastAPI

```bash
uvicorn api.app:app --reload
```

### Start Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📊 Outputs

The project automatically generates:

- Graph Features
- Customer Risk Scores
- Fraud Ring Reports
- Model Comparison Report
- SHAP Explainability Plots
- Network Graph
- Fraud Distribution Charts
- Trained Models

---

# 📚 Dataset

**PaySim Mobile Money Transaction Dataset**

Source:

https://www.kaggle.com/datasets/ealaxi/paysim1

> The raw dataset is not included in this repository because of its size. Download it separately and place it in `data/raw/`.

---

# 🚀 Future Improvements

- Graph Attention Networks (GAT)
- Temporal Graph Networks
- Neo4j Graph Database
- Docker Deployment
- Kubernetes Deployment
- AWS Cloud Deployment
- Kafka Streaming
- Online Learning

---

# 👨‍💻 Author

**Akash Jadhav**

- 🎓 B.Sc. Computer Science Hons
- 🏫 MIT World Peace University, Pune
- 💻 Aspiring AI Engineer | Machine Learning Engineer | Data Engineer

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates further development.