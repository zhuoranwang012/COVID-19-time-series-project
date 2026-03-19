# COVID-19 Time Series Analysis with SARIMA

This project analyzes daily COVID-19 case counts in the United States using classical time series methods. The goal is to understand temporal patterns in the data and assess whether there is evidence of a long-term increasing or decreasing trend.

---

## Dataset

- Source: Google COVID-19 Open Data  
- Variable: Daily new confirmed cases (United States)  
- Time period: 2020 – 2022  

The data were preprocessed by removing missing values, correcting negative values (due to reporting adjustments), and converting dates into a proper time index.

---

## Methodology

The analysis follows a standard time series workflow:

1. **Exploratory Analysis**
   - Time series visualization
   - Identification of non-stationarity and wave patterns

2. **ACF / PACF Analysis**
   - Detection of dependence structure
   - Identification of strong weekly seasonality (lag = 7)

3. **Modeling**
   - First-order differencing for stationarity
   - Seasonal differencing (period = 7)
   - SARIMA model:SARIMA(1,1,1)(1,1,1,7)

4. **Forecasting**
- 30-day ahead forecast
- Prediction intervals to quantify uncertainty

---

##  Results

### Time Series
The data exhibit large fluctuations and multiple waves, with a strong weekly reporting pattern.

### Key Findings
- Clear **weekly seasonality** is present  
- Strong **short-term dependence** in case counts  
- No clear **long-term increasing or decreasing trend**  
- Forecast shows **stable oscillation** with increasing uncertainty over time  

---

## Forecast

The SARIMA model produces short-term forecasts that follow the observed seasonal pattern. However, prediction intervals widen quickly, indicating that long-term forecasts are highly uncertain.

---

## Insights

This analysis shows that COVID-19 case counts are better characterized by **wave-like dynamics** rather than a simple monotonic trend. While classical time series models capture short-term patterns effectively, external factors (e.g., policy changes, reporting delays) introduce substantial variability.

---
## How to Run
jupyter notebook notebooks/covid_time_series_analysis.ipynb
