import streamlit as st
from database_hospital import *


def update_hospital():
    col1, col2 = st.columns(2)
    with col1:
        H_ID  = st.number_input("Enter the ID of hospital you want to update:")
        new_H_Name = st.text_input("Name:")
        
    with col2:
        new_H_Address=st.text_input("Address")
        new_Ph_Number=st.text_input("Number:")

    if st.button("Update"):
        update_hospital_row(H_ID, new_H_Name, new_H_Address, new_Ph_Number)
        st.success("Successfully UPDATED : {}".format(new_H_Name))
        
