import streamlit as st

st.title("Timeout Test")

# Create a slider to select timeout duration (0-600 seconds) with 5-second increments
timeout_seconds = st.slider("Select timeout duration (seconds)", 0, 600, 10, step=5)

# Display the selected timeout value
st.write(f"Selected timeout: {timeout_seconds} seconds")

# Button to navigate to the timeout page
if st.button("Start Timeout Test"):
    # Set the timeout value in session state so it can be accessed by the timeout page
    st.session_state.timeout_seconds = timeout_seconds
    # Sleep BEFORE navigating to the timeout page
    import time
    time.sleep(timeout_seconds)
    # Navigate to the timeout test page
    st.switch_page("pages/timeout_test.py")
  
