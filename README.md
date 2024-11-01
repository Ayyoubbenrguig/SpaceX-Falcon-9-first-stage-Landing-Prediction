# SpaceX Falcon 9 First Stage Landing Prediction

This project aims to predict the likelihood of a successful landing for the SpaceX Falcon 9 rocket's first stage. By determining whether the first stage will land successfully, we can estimate the cost of a launch. This analysis can be valuable for companies competing with SpaceX in the space launch market.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/landing_1.gif)

## Project Overview

Using data from various sources, we analyzed SpaceX launch data to understand the factors contributing to a successful first-stage landing. The project involved data collection, cleaning, exploration, and predictive modeling. The findings suggest that SpaceX's success rate has been improving over time, especially for heavy payloads in certain orbits.

## Table of Contents

- [Data Collection](#data-collection)
- [Data Wrangling and Preprocessing](#data-wrangling-and-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Interactive Visualizations](#interactive-visualizations)
- [Predictive Modeling](#predictive-modeling)
- [Conclusion](#conclusion)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)

## Data Collection

We gathered data from two main sources:

1. **SpaceX API**: Used to obtain launch data, including rocket type, payload, and mission details.
2. **Web Scraping**: Extracted additional data from Wikipedia using Beautiful Soup to fill in missing information.

## Data Wrangling and Preprocessing

- Processed and cleaned the collected data using Pandas.
- Created new features, including a landing outcome label based on mission outcomes.
- Addressed missing values by replacing them with averages where applicable.

## Exploratory Data Analysis (EDA)

Performed visual and SQL-based analysis to gain insights into:

- Launch success rates across different sites.
- Success rates for various payload masses and orbits.
- Trends over time in launch success rates.

### Key Findings

- Initial launches had lower success rates, particularly with lighter payloads.
- Success rates have been increasing over time, with certain orbits achieving 100% success.

## Interactive Visualizations

We used **Folium** and **Plotly Dash** to build interactive dashboards that allow users to explore:

- Launch site locations and success rates.
- Success rates by payload mass and orbit type.

## Predictive Modeling

Built and evaluated several classification models to predict landing success:

- **Logistic Regression**
- **Support Vector Machine (SVM)**
- **Decision Tree**
- **K-Nearest Neighbors (KNN)**

The Decision Tree model achieved the highest accuracy (87.5%) and was selected as the best model.

## Conclusion

The analysis indicates a clear improvement in SpaceX's success rates, especially for heavy payloads in high-demand orbits. Based on this trend, it may not be wise to bet against SpaceX in the rocket launch industry.

## Project Structure

- `data/`: Contains raw and processed data.
- `notebooks/`: Jupyter notebooks for data collection, wrangling, EDA, and modeling.
- `dashboard/`: Plotly Dash app scripts for interactive visualizations.
- `results/`: Final model evaluations, visualizations, and summary reports.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SpaceX-Falcon-9-Landing-Prediction.git
   ```
2. Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- Run the notebooks in `notebooks/` to perform data analysis and modeling.
- To explore interactive visualizations, run the Plotly Dash app located in `dashboard/`.
