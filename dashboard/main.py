import streamlit as st
import requests
import pandas as pd


institutitions = requests.get('http://127.0.0.1:8000/api/institution/')
teste = pd.json_normalize(institutitions.json())
teste