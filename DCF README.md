# Financial-models

Welcome to MA's repository. Here, as a young senior high student, also a financial addict, I'd like to share my learning process and projects with you guys. Looking forward to your guidance.

## 📊 FCFE Valuation Models - Two Implementations

This project contains two versions of Free Cash Flow to Equity (FCFE) valuation models, demonstrating different approaches to equity valuation using discounted cash flow methodology.

### 🎯 Project Overview

The Free Cash Flow to Equity (FCFE) model is a fundamental valuation technique that calculates the intrinsic value of a company's equity by discounting future cash flows available to equity shareholders. This repository contains two implementations:

1. **Simplified Version** - Uses revenue-based FCF estimation
2. **Detailed Version** - Uses comprehensive financial statement components

### 📈 Model Characteristics

#### Common Features (Both Versions):
- **Five-year detailed forecast period** with customizable growth rates
- **Gordon Growth Model** for terminal value calculation
- **WACC-based discounting** for present value calculations
- **Interactive user input** for parameter customization
- **Visualization** of cash flow projections and valuation components
- **Input validation** to ensure data integrity
- **Chinese language support** for matplotlib visualizations

#### Simplified Version Features:
- **Revenue-based approach**: Estimates FCF as a percentage of revenue
- **Streamlined inputs**: Requires fewer financial parameters
- **Quick analysis**: Ideal for preliminary valuations

#### Detailed Version Features:
- **Comprehensive FCFE calculation**: 
  - Starts with net income
  - Adds back non-cash expenses (depreciation)
  - Adjusts for working capital changes
  - Accounts for capital expenditures
  - Includes debt financing effects
- **Thorough financial analysis**: Captures complex capital structure effects

### 🧮 Core Valuation Methodology

Both models follow this fundamental DCF structure:

```
Equity Value = PV of Detailed Forecast Period + PV of Terminal Value
```

**Terminal Value Calculation:**
```
TV = FCF_Year5 × (1 + g) ÷ (WACC - g)
```

**Key Input Parameters:**
- Weighted Average Cost of Capital (WACC)
- Long-term growth rate (g)
- Forecast period growth rates
- Net debt position
- Total shares outstanding

### 📊 Output Analysis

Both models provide:
- **Annual FCF projections** with growth rates
- **Present value calculations** for each forecast year
- **Enterprise value and equity value**
- **Per-share intrinsic value**
- **Visual breakdown** of valuation components

### 🛠 Technical Implementation

**Core Libraries:**
- `pandas` for data manipulation and financial projections
- `numpy` for mathematical computations
- `matplotlib` for financial visualization
- Custom Chinese font configuration for professional charts

**Key Features:**
- Robust input validation with error handling
- Interactive growth rate input with format checking
- Automatic data frame creation for organized output
- Professional visualization with bar charts and pie charts
- Terminal value sanity checks (WACC > growth rate)

### 🚀 How to Use

1. **Run either script** based on your data availability:
   - Use simplified version for quick estimates with limited data
   - Use detailed version for comprehensive analysis with full financials

2. **Input required parameters** when prompted:
   - Company name and financial metrics
   - Growth rate assumptions
   - Cost of capital and terminal growth
   - Capital structure information

3. **Review outputs:**
   - Detailed financial projections table
   - Valuation summary (enterprise value, equity value, per-share value)
   - Visual charts showing cash flow trends and valuation composition

### 📚 Educational Value

Through developing these models, I've deepened my understanding of:

- **DCF valuation theory** and practical implementation
- **FCFE vs FCFF** distinctions and applications
- **Financial modeling best practices**
- **Time value of money** concepts
- **Terminal value estimation** methodologies
- **Python programming** for financial analysis

### 💡 Key Learnings

**Valuation Insights:**
- The importance of growth rate assumptions in terminal value
- How WACC sensitivity affects valuation outcomes
- Why detailed FCFE calculation provides more accurate results
- The critical relationship between WACC and long-term growth rates

**Technical Skills:**
- Data validation and error handling in financial applications
- Creating professional financial visualizations
- Structuring interactive financial analysis tools
- Building modular, reusable valuation code

### 🔍 Model Comparison

| Aspect | Simplified Version | Detailed Version |
|--------|-------------------|------------------|
| **Data Requirements** | Minimal (revenue-based) | Comprehensive financials |
| **Calculation Depth** | Basic FCF estimation | Full FCFE derivation |
| **Accuracy** | Approximate | More precise |
| **Use Case** | Quick screening | Detailed analysis |
| **Input Complexity** | Low | High |

### 📈 Future Enhancements

Potential improvements for these models:
- [ ] Monte Carlo simulation for sensitivity analysis
- [ ] Multiple scenario analysis (base, bull, bear cases)
- [ ] Integration with real-time financial data APIs
- [ ] Comparable company analysis integration
- [ ] Historical financial data visualization
- [ ] Export functionality for reports

---

*These FCFE models represent my exploration of fundamental equity valuation techniques. As a student passionate about finance, I'm continually learning and welcome feedback to improve my understanding and coding practices!*

**MA**  
*Young Financial Enthusiast & Aspiring Analyst*
