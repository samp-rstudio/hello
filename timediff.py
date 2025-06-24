import streamlit as st
import time

start=st.date_input('Start Date')
end=st.date_input('End Date')
if start and end:
 number_of_days = (end - start).days
 time.sleep(number_of_days)
 st.write(end-start)
