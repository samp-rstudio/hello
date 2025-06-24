import streamlit as st
import time

start=st.date_input('Start Date')
end=st.date_input('End Date')
if start and end:
 time.sleep(30)
 st.write(end-start)
