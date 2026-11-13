import streamlit as st

st.set_page_config(
    page_title="Digital Sign-Off Dashboard",
    layout="wide"
)

st.title("✅ Digital Sign-Off Dashboard")

st.sidebar.header("Filters")

oe = st.sidebar.selectbox(
    "Operating Entity",
    [
        "Australia",
        "Singapore",
        "Germany"
    ]
)

lob = st.sidebar.selectbox(
    "Line of Business",
    [
        "Construction",
        "Marine",
        "Property"
    ]
)

quarter = st.sidebar.selectbox(
    "Quarter",
    [
        "Q1",
        "Q2",
        "Q3",
        "Q4"
    ]
)

st.write("OE:", oe)
st.write("LOB:", lob)
st.write("Quarter:", quarter)

st.subheader("KPI Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total KPIs", "24")

with c2:
    st.metric("Completed", "15")

with c3:
    st.metric("Pending", "9")

with c4:
    st.metric("Progress", "63%")

st.subheader("Sign Off Status")

st.dataframe(
    {
        "KPI": ["GNWP", "Policy Count", "Loss Count"],
        "Status": ["Complete", "Pending", "Complete"]
    }
)
