# Project 02: Agricultural Intelligence for Kenya Agricultural Research Institute (KARI)

## 🌾 Business Context

**Kenya Agricultural Research Institute (KARI)** is the leading agricultural research organization in Kenya, responsible for developing and promoting agricultural technologies to enhance food security and farmer livelihoods across the nation. Agriculture is the backbone of Kenya's economy, employing over 40% of the population and contributing significantly to GDP.

KARI has been collecting comprehensive data on crop production, weather patterns, and market prices across different counties in Kenya over several years. However, the institute faces critical challenges:

- **Seasonal Uncertainty**: Farmers need better guidance on optimal planting times and crop selection
- **Yield Prediction**: Inability to accurately forecast crop yields affects food security planning
- **Climate Variability**: Understanding the impact of rainfall and temperature on different crops
- **Market Volatility**: Price fluctuations make it difficult for farmers to plan and maximize profits
- **Resource Optimization**: Determining optimal fertilizer usage for different crops and conditions
- **Regional Variations**: Different counties have different agricultural potential and challenges

The Ministry of Agriculture and farmer cooperatives are requesting evidence-based recommendations to improve agricultural productivity and farmer incomes.

As a newly hired **Agricultural Data Analyst** at KARI, you have been tasked with analyzing time series data to uncover insights that can improve agricultural planning, enhance food security, and support farmer decision-making.

---

## 📊 Dataset Description

You have been provided access to KARI's agricultural database in a CSV file named `kenyan_agriculture_data.csv` containing multi-year agricultural data across Kenyan counties.

### Data Fields:
- **Date**: Monthly timestamp of the observation
- **County**: Kenyan county (e.g., Nakuru, Kisumu, Meru, etc.)
- **Crop**: Type of crop (Maize, Wheat, Rice, Beans, etc.)
- **Yield_Tons**: Crop yield in metric tons
- **Rainfall_mm**: Monthly rainfall in millimeters
- **Temperature_C**: Average monthly temperature in Celsius
- **Price_KSH_per_kg**: Market price in Kenyan Shillings per kilogram
- **Area_Planted_Hectares**: Area planted in hectares
- **Fertilizer_Used_kg**: Amount of fertilizer used in kilograms

### Time Series Characteristics:
- **Temporal Coverage**: Multiple years of monthly data
- **Spatial Coverage**: Multiple counties across Kenya
- **Crop Diversity**: Various staple and cash crops
- **Weather Integration**: Rainfall and temperature data aligned with crop performance

---

## 🎯 Your Mission

Your client is particularly interested in understanding seasonal patterns, yield trends, weather impacts, and market price fluctuations, as this information is crucial for developing evidence-based agricultural policies and farmer advisory services.

### Expected Deliverables:

1. **Time Series Exploratory Data Analysis**
   - Examine the temporal structure of the data
   - Identify data quality issues, missing values, and outliers
   - Generate summary statistics for key variables over time
   - Understand the frequency and granularity of observations

2. **Seasonal Pattern Analysis**
   - Identify seasonal patterns in crop yields across different crops
   - Analyze rainfall and temperature seasonality
   - Examine seasonal price fluctuations for different crops
   - Determine optimal planting and harvesting seasons

3. **Trend Analysis**
   - Analyze long-term trends in crop yields
   - Examine trends in weather patterns (rainfall, temperature)
   - Investigate price trends over time
   - Identify improving or declining agricultural productivity

4. **Weather Impact Analysis**
   - Examine the relationship between rainfall and crop yields
   - Analyze the impact of temperature on different crops
   - Identify optimal weather conditions for each crop type
   - Assess climate variability and its agricultural implications

5. **Crop Performance Comparison**
   - Compare yield performance across different crops
   - Analyze profitability (yield × price) of different crops
   - Examine fertilizer efficiency for different crops
   - Identify high-performing and underperforming crops

6. **Regional Analysis**
   - Compare agricultural performance across counties
   - Identify regional specializations and comparative advantages
   - Analyze regional weather patterns and their impact
   - Provide county-specific recommendations

7. **Data Visualization**
   - Create time series plots showing trends and patterns
   - Use appropriate visualizations for seasonal decomposition
   - Develop comparative visualizations across crops and regions
   - Ensure visualizations effectively communicate temporal insights

8. **Actionable Insights and Recommendations**
   - Provide evidence-based crop selection recommendations
   - Suggest optimal planting schedules based on seasonal patterns
   - Recommend fertilizer optimization strategies
   - Advise on climate adaptation strategies
   - Support food security planning with yield forecasts
