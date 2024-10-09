import streamlit as st

st.write("""
# My first app
Hello *everybody!*

Thanks for using Posit Connect Cloud!
""")

st.write("## Headers")
st.write(st.context.headers)
st.write("## Cookies")
st.write(st.context.cookies)
st.write("## Query parameters")
st.write(st.query_params)
