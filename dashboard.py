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
    st.markdown("""
    Track your daily hydration with the help of AI assistnt.
    log your intake, get smart feedback and stay healthy effortlessly
    """)


    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.experimental_rerun()


else: 
    # Slidebar: Intake Input
    st.sidebar.header("Log Your Water Intake")
    user_id = st.sidebar.text_input("User ID", value="user_123")
    intake_ml = st.sidebar.number_input("Water intake (ml)", min_value=0, step=100)




    if st.sidebar.button("Submit"):
        if user_id and intake_ml:
            log_intake(user_id, intake_ml)
            st.success(f"Logged {intake_ml}ml for {user_id}")



            agent = WaterIntakeAgent()
            feedback = agent.analyze_intake(intake_ml)
            st.info(f"AI feedback: ({feedback})")

        
    
    # Divider
    st.markdown("---")