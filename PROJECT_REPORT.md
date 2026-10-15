# Project Report: Learner Demographics and Course Enrollment Behavior Analysis on EduPro

## Abstract
This project demonstrates descriptive analytics for an online learning platform. It explores learner age, education, employment, region, course choice, enrollment source, weekly study hours, engagement, course completion and satisfaction. Python, pandas, Plotly and Streamlit are used to prepare and visualize a synthetic dataset of 1,200 learner records. The data is fictional and contains no real learner records.

## 1. Problem Statement
Online learning providers need to understand who enrolls, which courses attract learners, how learners engage and what proportion complete courses. A structured dashboard can support monitoring and guide further investigation, provided that privacy and data quality are respected.

## 2. Objectives
- Summarize learner demographic and education characteristics.
- Compare enrollment volume across courses and acquisition sources.
- Examine monthly enrollment trends.
- Compare completion rates, engagement and satisfaction by course.
- Offer data-informed recommendations without claiming causality.

## 3. Tools
Python 3, pandas, NumPy, Plotly and Streamlit. Data is stored in CSV format.

## 4. Dataset
The dataset contains 1,200 synthetic learner enrollment records. Features include learner ID, enrollment date, age, gender, region, education level, employment status, course, enrollment source, weekly study hours, engagement score, course duration, completion status and satisfaction rating. All records are simulated for learning purposes.

## 5. Methodology
1. Load the CSV and inspect its shape, data types and missing values.
2. Summarize learners and course enrollments.
3. Calculate completion rate as completed learners divided by learners in the selected group.
4. Calculate mean engagement and satisfaction.
5. Group enrollments by month, course, education level and source.
6. Build an interactive dashboard with course and region filters.
7. Interpret patterns cautiously and state data limitations.

## 6. Dashboard Features
- Learner count, completion rate, average engagement and satisfaction KPI cards.
- Enrollment counts by course and age distribution.
- Monthly enrollment trend.
- Course completion-rate comparison.
- Education-level and enrollment-source charts.
- Course performance table, filters and CSV download.

## 7. Recommendations
- Identify courses with lower completion and investigate learner feedback, prerequisites and course difficulty.
- Provide early support to learners whose engagement is low, using transparent and privacy-respecting methods.
- Test marketing channels using cost-per-enrollment and long-term completion, not enrollment count alone.
- Offer flexible learning schedules for different employment groups.
- Collect consent-based feedback and validate insights using real platform data.

## 8. Limitations and Ethics
The data is synthetic and does not represent actual EduPro users. Patterns are illustrative and cannot support claims about real learners. Engagement and completion relationships are not proof of causation. In real deployment, minimize personal data, restrict access, document consent and avoid discriminatory decisions based on demographic characteristics.

## 9. Conclusion
The project demonstrates how an interactive dashboard can organize enrollment and learner-behavior metrics. It provides a reproducible starting point for analysis, while emphasizing that meaningful institutional conclusions require validated data, privacy safeguards and stakeholder review.
