# Financial-models__CAPM Model

Welcome to MA's repository. Here, as a young senior high student, also a financial addict, I'd like to share my learning process and projects with you guys. Looking forward to your guidance.

## 📊 CAPM Analysis: Marvell Technology (MRVL) vs. NASDAQ

This project demonstrates a practical implementation of the Capital Asset Pricing Model (CAPM) by analyzing the relationship between Marvell Technology (MRVL) stock and the NASDAQ market index through Monte Carlo simulation.

### 🎯 Project Overview

This Python script generates simulated stock price data for MRVL and NASDAQ over a one-year period (March 2025 - March 2026) and performs comprehensive CAPM analysis including:

- **Beta Coefficient Calculation**: Measures systematic risk relative to the market
- **Alpha Calculation**: Identifies excess returns above market performance
- **R-squared Analysis**: Determines how much of MRVL's volatility is explained by market movements
- **Visualization**: Multiple charts showing price trends, returns, and regression analysis

### 📈 Key Features

1. **Realistic Data Simulation**
   - Simulates MRVL stock prices with a preset Beta of 2.1 (high volatility tech stock)
   - Models NASDAQ index movements with realistic market parameters
   - Includes both systematic and idiosyncratic risk components

2. **Comprehensive CAPM Analysis**
   - Calculates actual Beta from simulated returns
   - Determines Alpha (excess returns)
   - Computes R-squared to measure model fit
   - Analyzes total returns and annualized volatility

3. **Professional Visualizations**
   - Price trend comparison charts
   - Daily returns time series
   - Scatter plots with regression lines
   - Statistical summary displays

### 🛠 Technical Implementation

**Libraries Used:**
- `pandas` for data manipulation
- `numpy` for numerical computations and random number generation
- `matplotlib` for professional financial charting
- `datetime` for time series management

**Core Algorithm:**
- Geometric Brownian Motion for price simulation
- Linear regression for Beta calculation
- Daily compounding for return calculations
- Statistical methods for risk assessment

### 📊 Sample Output Metrics

```
=== CAPM Analysis Results ===
Preset Beta coefficient: 2.1
Calculated Beta (systematic risk): ~2.1
Alpha (excess returns): ~0.0002
R-squared: ~0.85 (market explains 85% of MRVL's volatility)

Total Returns: MRVL = ~45%, NASDAQ = ~12%
Annual Volatility: MRVL = ~35%, NASDAQ = ~24%
```

### 🚀 How to Run

1. Ensure you have Python installed with required libraries:
   ```bash
   pip install pandas numpy matplotlib
   ```

2. Run the script:
   ```bash
   python capm_analysis.py
   ```

3. The script will:
   - Generate simulated price data
   - Perform CAPM calculations
   - Display multiple analytical charts
   - Print comprehensive results summary

### 📚 Learning Outcomes

Through this project, I've gained practical understanding of:

- **CAPM Theory**: Relationship between expected returns and systematic risk
- **Financial Modeling**: Creating realistic market simulations
- **Risk Assessment**: Quantifying Beta, volatility, and market exposure
- **Python Financial Programming**: Using libraries for quantitative analysis
- **Data Visualization**: Creating professional financial charts

### 🔍 Educational Value

This project serves as an excellent learning tool for:
- Understanding how Beta affects stock performance
- Visualizing the market-stock relationship
- Practicing financial data analysis with Python
- Building foundations for more complex financial models

### 📈 Future Enhancements

Potential improvements for this project:
- [ ] Add real historical data integration
- [ ] Implement multiple regression for additional factors
- [ ] Create interactive web dashboard
- [ ] Add portfolio optimization features
- [ ] Include statistical significance testing

---

*This project represents my journey into quantitative finance as a high school student. I welcome any feedback, suggestions, or collaboration opportunities to help me grow in this exciting field!*

**MA**  
*Young Financial Enthusiast & Aspiring Quant*
