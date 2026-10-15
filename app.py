import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="EduPro Learner Analytics", page_icon="🎓", layout="wide")
st.title("🎓 EduPro: Learner Demographics & Enrollment Behavior")
st.caption("Education analytics dashboard | Demonstration dataset is synthetic; no real learner records are used.")
file = Path(__file__).parent / "edupro_learner_enrollments.csv"
df = pd.read_csv(file, parse_dates=["Enrollment_Date"])
courses = st.sidebar.multiselect("Course", sorted(df.Course_Name.unique()), default=sorted(df.Course_Name.unique()))
regions = st.sidebar.multiselect("Region", sorted(df.Region.unique()), default=sorted(df.Region.unique()))
d = df[df.Course_Name.isin(courses) & df.Region.isin(regions)].copy()
if d.empty:
    st.warning("Select at least one course and one region.")
    st.stop()
total = len(d)
completion = (d.Completed_Course.eq("Yes").mean()*100) if total else 0
avg_engagement = d.Engagement_Score.mean()
avg_rating = d.Satisfaction_Rating.mean()
c1,c2,c3,c4 = st.columns(4)
c1.metric("Learners", f"{total:,}")
c2.metric("Completion Rate", f"{completion:.1f}%")
c3.metric("Avg Engagement", f"{avg_engagement:.1f}/100")
c4.metric("Avg Satisfaction", f"{avg_rating:.2f}/5")
a,b = st.columns(2)
course_counts = d.groupby("Course_Name",as_index=False).agg(Enrollments=("Learner_ID","count"))
a.plotly_chart(px.bar(course_counts, x="Course_Name", y="Enrollments", title="Enrollments by Course", color="Course_Name"), use_container_width=True)
b.plotly_chart(px.histogram(d, x="Age", nbins=18, title="Learner Age Distribution"), use_container_width=True)
a,b = st.columns(2)
monthly = d.assign(Month=d.Enrollment_Date.dt.to_period("M").astype(str)).groupby("Month",as_index=False).size().rename(columns={"size":"Enrollments"})
a.plotly_chart(px.line(monthly, x="Month", y="Enrollments", markers=True, title="Monthly Enrollment Trend"), use_container_width=True)
completion_course = d.groupby("Course_Name",as_index=False).agg(Completion_Rate=("Completed_Course",lambda s:(s=="Yes").mean()*100), Avg_Engagement=("Engagement_Score","mean"), Avg_Rating=("Satisfaction_Rating","mean"))
b.plotly_chart(px.bar(completion_course, x="Course_Name", y="Completion_Rate", title="Completion Rate by Course (%)", color="Course_Name"), use_container_width=True)
st.subheader("Learner profile")
a,b = st.columns(2)
a.plotly_chart(px.bar(d.groupby("Education_Level",as_index=False).size().rename(columns={"size":"Learners"}), x="Education_Level", y="Learners", title="Education Level"), use_container_width=True)
b.plotly_chart(px.bar(d.groupby("Enrollment_Source",as_index=False).size().rename(columns={"size":"Learners"}), x="Enrollment_Source", y="Learners", title="Enrollment Source"), use_container_width=True)
st.subheader("Course performance table")
st.dataframe(completion_course.sort_values("Completion_Rate",ascending=False).style.format({"Completion_Rate":"{:.1f}%","Avg_Engagement":"{:.1f}","Avg_Rating":"{:.2f}"}), use_container_width=True)
st.subheader("Automated observations")
popular = course_counts.sort_values("Enrollments",ascending=False).iloc[0]
best_completion = completion_course.sort_values("Completion_Rate",ascending=False).iloc[0]
source_counts = d.groupby("Enrollment_Source").size().sort_values(ascending=False)
st.write(f"- Most enrolled course in the selected data: **{popular.Course_Name} ({int(popular.Enrollments)} learners)**.")
st.write(f"- Highest completion rate: **{best_completion.Course_Name} ({best_completion.Completion_Rate:.1f}%)**.")
st.write(f"- Largest enrollment source: **{source_counts.index[0]} ({int(source_counts.iloc[0])} learners)**.")
st.info("Recommendations: provide early support for learners with low engagement; review course difficulty and length; test acquisition channels using cost-per-enrollment data; collect consent-based learner feedback and validate these synthetic-data findings against EduPro's real, privacy-protected records.")
with st.expander("Dataset preview"):
    st.dataframe(d.head(100), use_container_width=True)
st.download_button("Download filtered data as CSV", d.to_csv(index=False).encode("utf-8"), "edupro_filtered_data.csv", "text/csv")
