import mysql.connector
import streamlit as st
import pandas as pd 
import plotly.express as px


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="PES1UG20CS078_organ"
)

c = mydb.cursor()


def view_patient_details():
      c.execute('SELECT * FROM patient')
      data=c.fetchall()
      return data
    


def add_patient_data(patient_ID,name,date_of_Birth,organ_ID,reason_of_request,date_of_procurement,d_id):
    c.execute('INSERT INTO  patient ( patient_ID,name,date_of_Birth,organ_ID,reason_of_request,date_of_procurement,d_id) VALUES(%s,%s,%s,%s,%s,%s,%s)',( patient_ID,name,date_of_Birth,organ_ID,reason_of_request,date_of_procurement,d_id))
    mydb.commit()
    

def delete_patient_row(patient_ID):
    c.execute('DELETE From patient where  patient_ID="{}"'.format(patient_ID))
    mydb.commit()