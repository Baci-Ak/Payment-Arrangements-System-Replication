import streamlit as st
import pandas as pd
from PIL import Image

# Load the data
processed_data = pd.read_excel("data/Processed_Data.xlsx")
payment_schedule = pd.read_excel("data/Payment_Schedule.xlsx")
Original_Data = pd.read_csv("data/CaseStudy Data.csv")

# Title and logo
st.title("Payment Arrangements System Replication")
image = Image.open('profile_photo.png')
st.image(image, caption='Baci Akom', width=100)

st.header("Processed Data")
st.markdown("This section displays the processed data generated by the system, including the calculated last payment date and last payment amount for each arrangement.")
st.write(processed_data)

st.header("Payment Schedule")
st.markdown("This section displays the detailed payment schedule for each customer, including all planned payment dates and payment amounts generated by the system.")
st.write(payment_schedule)


st.header("Original Data")
st.markdown("This section displays the original data provided by the company, including anonymized arrangements.")
st.write(Original_Data)

# Download processed data
st.header("Download Processed Data")
csv_processed = processed_data.to_csv(index=False)
st.download_button(
    label="Download Processed Data as CSV",
    data=csv_processed,
    file_name='Processed_Data.csv',
    mime='text/csv',
)

# Download payment schedule
st.header("Download Payment Schedule")
csv_schedule = payment_schedule.to_csv(index=False)
st.download_button(
    label="Download Payment Schedule as CSV",
    data=csv_schedule,
    file_name='Payment_Schedule.csv',
    mime='text/csv',
)

# Footer
st.markdown("Developed by Baci Akom")




