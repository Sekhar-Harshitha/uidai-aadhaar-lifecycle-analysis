# UIDAI Aadhaar Lifecycle Analysis

## 📌 Overview
This repository contains an end-to-end analysis of Aadhaar enrolment and update patterns using official UIDAI datasets. The project studies the complete Aadhaar lifecycle — enrolment, biometric updates, and demographic updates — to identify regional disparities and support data-driven policy decisions.

This project is developed as part of the **UIDAI Data Hackathon 2026**.

---

## 🎯 Objectives
- Analyze Aadhaar enrolment trends across Indian states
- Identify states with high and low enrolment coverage
- Study biometric update demand across age groups
- Study demographic update patterns across regions
- Create policy-ready visualizations for decision-makers
- Support targeted outreach and infrastructure planning

---

## 📂 Datasets Used
All datasets are officially provided by UIDAI for the hackathon.

### Aadhaar Enrolment Dataset
- `api_data_aadhar_enrolment_0_500000.csv`
- Columns: `date, state, district, pincode, age_0_5, age_5_17, age_18_greater`

### Biometric Update Dataset
- `api_data_aadhar_biometric_0_500000.csv`
- Columns: `date, state, district, pincode, bio_age_5_17, bio_age_17_`

### Demographic Update Dataset
- `api_data_aadhar_demographic_0_500000.csv`
- Columns: `date, state, district, pincode, demo_age_5_17, demo_age_17_`

---

## 🧪 Methodology

### Data Cleaning
- Converted date columns to standard datetime format
- Cleaned and standardized state names
- Handled missing or invalid records safely

### Feature Engineering
- Created total enrolment column
- Created total biometric update column
- Created total demographic update column

### Analysis
- Aggregated data at state level
- Identified top and low performing states
- Compared enrolment vs update patterns
- Highlighted regions needing targeted intervention

### Visualization
- Designed clean, aesthetic dashboard-style charts
- Used visual hierarchy and annotations
- Optimized graphs for presentations and judging

---

## 📊 Key Insights
- Aadhaar enrolment is concentrated in a few high-population states
- Several states show lower enrolment coverage
- Adult enrolment dominates total numbers
- High biometric update demand indicates ongoing identity maintenance
- Demographic update patterns reflect correction and update needs
- Insights can guide infrastructure and outreach planning

---

## 🗂️ Project Structure
```
uidai-aadhaar-lifecycle-analysis/
│
├── api_data_aadhar_enrolment/
├── api_data_aadhar_biometric/
├── api_data_aadhar_demographic/
│
├── aadhaar_analysis.py
├── biometric_analysis.py
├── demographic_analysis.py
├── eda_clustering.py
│
└── README.md
```

---

## ⚙️ How to Run the Project

1. Clone the repository
```bash
git clone https://github.com/your-username/uidai-aadhaar-lifecycle-analysis.git
cd uidai-aadhaar-lifecycle-analysis
```

2. Install dependencies
```bash
pip install pandas matplotlib numpy
```

3. Run the analysis scripts
```bash
python aadhaar_analysis.py
python biometric_analysis.py
python demographic_analysis.py
```

---

## 📈 Outputs
- State-wise Aadhaar enrolment visualizations
- Biometric update distribution charts
- Demographic update distribution charts
- Policy-ready insights for UIDAI planning

---

## 🏆 Hackathon Submission
This project is submitted as part of the **UIDAI Data Hackathon 2026**.  
All analysis strictly uses the datasets provided by UIDAI.

---

## 📜 License
MIT License — for educational and hackathon use only.

---

## 🙌 Acknowledgements
- UIDAI for providing open datasets
- Data.gov.in for hosting datasets
- UIDAI Data Hackathon 2026 organizing committee
