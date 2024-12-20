# Alzheimer's Disease and Healthy Aging Data Analysis

## Overview
This project analyzes trends and growth rates in Alzheimer's Disease data using techniques like data preprocessing, confidence interval analysis, and K-Means clustering. The dataset is derived from the **Behavioral Risk Factor Surveillance System (BRFSS)**, a premier health-related telephone survey in the United States.

## Objectives
1. Data Preprocessing and Imputation  
2. Analyzing Trends and Growth Rates Over Time  
3. Confidence Interval Analysis  
4. K-Means Clustering Analysis  

## Data Source
The dataset was downloaded from the **Alzheimer’s Official Website**, containing:
- **31 Features**
- **284,142 Rows**

---

## Methodology

### 1. **Data Preprocessing and Imputation**
- Renamed columns to standardized format for easy processing.
- Identified and imputed missing values:
  - **Numerical Features**: Imputed with the mean.
  - **Categorical Features**: Imputed with the mode.
- Verified preprocessing results using descriptive statistics.

---

### 2. **Analyzing Trends and Growth Rates**
- **Yearly Growth Analysis**: Examined the year-over-year percentage change in data entries.
- **State-wise Insights**: Identified the top 10 states with the highest average data values.
- **Visualization**: Created heatmaps to represent data distribution over states and years.

---

### 3. **Confidence Interval Analysis**
- **Definition**: Used confidence intervals to infer population parameters from the dataset.
- **Key Outcomes**:
  - Precision of data across regions.
  - Differences in confidence limits for cognitive decline measurements.

---

### 4. **K-Means Clustering**
- **Objective**: Cluster locations based on Alzheimer’s prevalence rates and demographic characteristics.
- **Methodology**:
  - Applied **Principal Component Analysis (PCA)** for dimensionality reduction.
  - Implemented **K-Means Clustering** with `k=3`.
- **Findings**:
  - Cluster 1: Outliers or unique prevalence patterns.
  - Cluster 2: Average prevalence rates.
  - Cluster 3: High prevalence rates with distinct demographic factors.
- **Visualization**: PCA plots for cluster interpretation.

---

## Key Insights
- Significant yearly growth in Alzheimer’s-related data reporting.
- Geographical disparities in Alzheimer’s prevalence.
- Distinct demographic and prevalence patterns across clusters.

---

## Technologies Used
- **Python**
  - Pandas
  - Matplotlib
  - Seaborn
  - Scikit-learn

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/adongol123/Alzheimer-s_Disease.git

2. Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

3. Run the Analysis

```bash
  python main.ipynb
```

---

## Contributors
- Stuti Bimali
- Ayush Dangol
- Binay Dhakal
- Hrishabh Mahaju

