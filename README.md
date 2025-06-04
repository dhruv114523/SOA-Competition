# SOA Competition – EDFIP Project Repository

This repository contains analysis and modeling work submitted for the **EDFIP Project** in the **2025 SOA Competition**. It includes two related but distinct components:

1. **Loss Analysis for Earth-Type Dams**
2. **Premium Calculation Model for Insurance Pricing**

Each component is self-contained and has its own `README.md` with detailed documentation. This file provides a high-level overview of the repository structure and purpose.

---

## Disclaimer

2 more scripts have been added, this README and their respective REAMEs will be updated shortly

---

## Repository Structure

```
SOA-Competition/
│
├── earth-dam-loss-analysis/
│   ├── data/
│   │   └── data.csv
│   ├── earth_dam_loss_analysis.py
│   └── README.md        # Loss analysis explanation
│
├── premium-calculation/
│   ├── data/
│   │   └── data.csv
│   ├── premium_model.py
│   └── README.md        # Premium pricing model explanation
│
└── README.md            # This parent overview file
```

---

## 1. Earth Dam Loss Analysis

This script processes dam failure and financial loss data, filtered for **Earth-type dams**, and:

- Filters dataset by dam type
- Calculates average losses per region:
  - Property Loss (Qm)
  - Liability Loss (Qm)
  - Business Interruption Loss (Qm)
- Adjusts annual probability of failure to a 10-year equivalent
- Outputs:
  - Regional summaries to console
  - A grouped bar chart visualizing average losses by region

For full documentation, see:  
[`earth-dam-loss-analysis/README.md`](./earth-dam-loss-analysis/README.md)

---

## 2. Premium Calculation Model

This module estimates insurance premiums for properties affected by dam-related risk, incorporating:

- Region-specific failure probabilities and hazard classifications
- House value categories and participation rates
- Inflation adjustments over multi-year coverage terms
- A scaling mechanism to align collected premiums with expected inflows

It prints detailed premium breakdowns by region and property category.

For full documentation, see:  
[`premium-calculation/README.md`](./premium-calculation/README.md)

---

## Requirements

Both components require:

- Python 3.x
- pandas
- numpy
- matplotlib

Install dependencies with:

```bash
pip install pandas numpy matplotlib
```

---

## Usage

Each module is self-contained. To run either:

1. Place `data.csv` in the corresponding `data/` folder.
2. Run the relevant Python script using:

```bash
python script_name.py
```

---
