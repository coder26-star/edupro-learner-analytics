# Learner Demographics and Course Enrollment Behavior: A Descriptive Analytics Framework for an Online Learning Platform

**Document type:** Student project research-paper draft  
**Author:** [Add student name before publication]  
**Important note:** This is a draft, not an approved or published paper. The dataset is synthetic.

## Abstract
Understanding enrollment patterns and learner engagement can help online learning providers improve course design and student support. This project demonstrates a descriptive-analytics workflow using a synthetic dataset of 1,200 learner records. Demographic and educational attributes, course choices, acquisition sources, weekly study hours, engagement, completion and satisfaction are summarized in an interactive Streamlit dashboard. The analysis uses Python, pandas and Plotly. Since all data is simulated, results are not claims about a real platform. Future work should use privacy-protected, consented operational data and investigate differences with appropriate statistical methods.

## Keywords
Learning analytics; enrollment behavior; learner demographics; course completion; dashboard; Python.

## 1. Introduction
Online learning platforms generate data about enrollments, course selections and learner activity. Descriptive analytics can help teams monitor these patterns and decide where further investigation is useful. Demographic attributes must be handled carefully and should not be used to make unfair or unsupported assumptions about individuals.

## 2. Objectives and Research Questions
1. Which courses attract the largest number of enrollments in the dataset?
2. How do enrollment counts vary over time and by acquisition source?
3. How do completion, engagement and satisfaction metrics vary across courses?
4. How can a dashboard communicate these summaries clearly?

## 3. Dataset and Methods
A synthetic dataset of 1,200 records was generated with learner age, gender, region, education, employment status, course, enrollment date, enrollment source, weekly study hours, engagement score, course duration, completion status and satisfaction rating. The analysis uses counts, means, proportions and group-by summaries. Completion rate is calculated as completed enrollments divided by total enrollments in a group.

## 4. Dashboard and Results
The dashboard presents learner count, completion rate, average engagement and average satisfaction. It includes course enrollment counts, age distribution, monthly enrollment trends, completion-rate comparisons, education-level distribution and enrollment-source counts. Results are recalculated under course and region filters. Exact dashboard values depend on the selected subset.

## 5. Discussion
These metrics can help a learning team form hypotheses about course demand and learner support. Enrollment volume is not equivalent to learning quality, and a higher completion rate alone does not prove that a course is better. Additional context such as course length, assessment difficulty, learner goals and marketing cost would be needed for robust evaluation.

## 6. Ethics and Limitations
All records are synthetic, so no conclusion can be drawn about actual EduPro learners. The analysis is descriptive and does not establish causation. Real learner data requires appropriate consent, data minimization, access controls, retention policies and fairness review.

## 7. Conclusion
A dashboard can make enrollment and learner-behavior summaries accessible to non-technical stakeholders. Future research could compare cohorts, examine retention over time and evaluate interventions using carefully designed methods and real, privacy-protected data.

## References
This draft does not claim a complete literature review or peer-reviewed publication. Before formal academic publication, add and verify relevant sources on learning analytics and follow the institution's citation format.
