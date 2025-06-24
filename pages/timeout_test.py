import streamlit as st

st.title("Timeout Test Done")

# Get the timeout value from session state
if 'timeout_seconds' in st.session_state:
    timeout_seconds = st.session_state.timeout_seconds

    # Display a message indicating that we're waiting
    st.write(f"Done sleeping")

    # Button to go back to the main page
    if st.button("Back to Timeout Selection"):
        st.switch_page("timeout_page.py")
else:
    st.error("No timeout duration specified. Please go back to the timeout selection page.")
    if st.button("Go to Timeout Selection"):
        st.switch_page("timeout_page.py")
