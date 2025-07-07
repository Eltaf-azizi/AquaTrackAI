import streamlit as st
import pandas as pd
import datetime as datetime
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history



if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False



# Welcome section

if not st.session_state.tracker_started:
    st.title(" Welcome to AI water tracker")