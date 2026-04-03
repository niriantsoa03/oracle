🔮 ORACLE
### *Optimized Regression Analytics for Crypto Live Exchange*

> A research project exploring the application of linear regression models for short-term cryptocurrency price prediction, powered by real-time Binance WebSocket data.

---

## 📌 Overview

ORACLE is a structured research pipeline that goes from statistical fundamentals to live market interaction. The goal is to study whether a linear regression model can produce actionable signals for short-term BTC/LTC price prediction — and, if results are conclusive, to move toward automated trading execution.

---

## 🧭 Project Roadmap

```
Phase 1 — Foundation       →   Study & implement linear regression from scratch
Phase 2 — Data Pipeline    →   Fetch real-time prices via Binance WebSocket
Phase 3 — Evaluation       →   Feed live data to the model & compare predictions vs reality
Phase 4 — Deployment       →   If results are conclusive, connect to Binance trading API
```

---

## 🏗️ Architecture (Planned)

```
Binance WebSocket
       │
       ▼
 Price Stream (BTC / LTC)
       │
       ▼
 Feature Engineering
       │
       ▼
 Linear Regression Model
       │
       ▼
 Prediction vs Reality Comparison
       │
       ▼
 [If conclusive] → Trading Execution via Binance API
```

---

## 🎯 Objectives

- [x] Understand and implement linear regression from first principles
- [ ] Connect to Binance WebSocket to stream live crypto prices
- [ ] Build a prediction pipeline feeding real-time data to the model
- [ ] Design a comparison and evaluation framework (predicted vs actual)
- [ ] Document findings, edge cases, and model limitations
- [ ] If results are promising — implement a live trading strategy via Binance REST API

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Data Stream | Binance WebSocket API |
| Modeling | Scikit-learn / NumPy (linear regression) |
| Evaluation | Pandas / Matplotlib |
| Trading API | Binance REST API *(Phase 4)* |

> *Stack subject to change as the project evolves.*

---

## 📂 Project Structure

```
oracle/
├── data/               # Historical and streamed price data
├── model/              # Linear regression implementation & training
├── stream/             # Binance WebSocket connection & handlers
├── evaluation/         # Comparison tools, metrics, visualizations
├── trading/            # Live trading logic (Phase 4)
├── notebooks/          # Research & experimentation notebooks
└── README.md
```

---

## ⚠️ Disclaimer

This project is a **research and learning exercise**. It is not financial advice. Cryptocurrency markets are highly volatile and unpredictable. Any live trading implementation should start with minimal capital or a paper trading environment.

---

## 📖 Research Notes

Key challenges anticipated during the project:

- **Non-stationarity** — Crypto price series are not stationary, which directly challenges linear regression assumptions. This will be studied and documented.
- **Feature selection** — Determining which inputs (lag values, volume, moving averages) carry the most predictive signal.
- **Overfitting** — Preventing the model from fitting noise rather than signal.
- **Latency** — Ensuring the prediction pipeline can keep up with live WebSocket data.

---

## 👤 Author

*ORACLE is a personal research project.*

---

*"All models are wrong, but some are useful." — George Box*
