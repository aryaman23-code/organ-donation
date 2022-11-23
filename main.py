import streamlit as st
import mysql.connector

from database_doctor import *
from database_hospital import *
from database_doctor import *
from database_organ import *
from database_patient import *
from create import *
from read import *
from delete import *
from update import *
from front_query import *

def main():


#have to add crud feature 
#have to add triggers and functions and procedures 


    st.title("Organ Donation App")
    menu = ["Hospital", "Patient","Doctor","Donor","Organ","front_end_query"]
    crud = ["Add", "View", "Edit", "Remove",]
    crud2=["Add", "View"]
    crud4=["Add", "View","count"]
    crud3=["View"]
    crud7=["Add", "View","View_date"]
    choice = st.sidebar.selectbox("Menu", menu)


    create_hospital_table()
    # hospital is done 
    if choice == "Hospital":
        choice1 = st.sidebar.selectbox("CRUD", crud)
        if choice1=="Add":
            st.subheader("Enter Hospital Details:")
            create_hospital()
           
        elif choice1 == "View":
            st.subheader("View Hospital Details")   
            read_hospital()

        elif choice1 == "Remove":
            st.subheader("Delete Hospital Details")
            delete_hospital()

        elif choice1 == "Edit":
            st.subheader("Edit Hospital Details")   
            update_hospital()

        else:
            st.subheader("Not allowed to edit hospital details")


    #this needs to be done
    elif choice == "Patient":
        choice1 = st.sidebar.selectbox("CRUD", crud)
        if choice1=="Add":
            st.subheader("Enter Patient Details:")
            create_patient()
           
        elif choice1 == "View":
            st.subheader("View Patient Details")
            read_patient()
            
        elif choice1 == "Edit":
            st.subheader("Edit Patient Details")
            
        elif choice1 == "Remove":
            st.subheader("Delete Patient Details")
            delete_patient()
        else:
            st.subheader("About tasks")

    
    elif choice == "Doctor":   
        choice1 = st.sidebar.selectbox("CRUD", crud4)
        if choice1 == "View":
            st.subheader("View Doctor Details")
            read_doctor()
        elif choice1=="Add":
            st.subheader("Enter Doctor Details:")
            create_doctor()
        elif choice1=="count":
            st.subheader("View Doctors in Each Hospital")
            count_doctor()
        else:
            st.subheader("You are only permitted to view & add Doctors details")
    
    #have to make add feature 
    elif choice == "Donor":
        choice1 = st.sidebar.selectbox("CRUD", crud7)
        if choice1=="View":
            st.subheader("View Donor Details:") 
            read_donor()
        elif choice1=="Add":
            st.subheader("Enter Donor Details:")
        
            create_donor()
        elif choice1=="View_date":
            st.subheader("Enter Donor Details:")
            view_date()
        
        
        else:
            st.subheader("You are only permitted to view & enter donor  details")

    #have to make add feature 
    elif choice == "Organ":  
        choice1 = st.sidebar.selectbox("CRUD", crud3)
        if choice1 == "View":
            st.subheader("View Organ Details")  
            read_organ()          
        else:
            st.subheader("You can only view and delete organ details")

    # this is for frontend query
    elif choice=='front_end_query':
        st.subheader("enter query")
        front_query()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
