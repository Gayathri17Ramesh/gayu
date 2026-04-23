import streamlit as st
import time
import pandas as pd

# Page title
st.set_page_config(page_title="AI-Sentinel Security Dashboard", layout="wide")

st.title("🛡️ AI-Sentinel: Autonomous Self-Healing Security Framework")

st.write("Multi-Agent RAG based Web Security System Demo")

# Fake server logs
logs = [
    "INFO User login success IP=192.168.1.10",
    "WARNING Failed login IP=192.168.1.100",
    "WARNING Failed login IP=192.168.1.100",
    "ERROR SQL Injection attempt IP=192.168.1.200",
]

# Initialize session state
if "threats" not in st.session_state:
    st.session_state.threats = []

if "blocked_ips" not in st.session_state:
    st.session_state.blocked_ips = []

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Server Logs")
    for log in logs:
        st.text(log)

with col2:
    st.subheader("🤖 Agent Control")

    if st.button("Start Monitoring"):

        # Monitor Agent
        with st.spinner("Monitor Agent: Scanning logs..."):
            time.sleep(2)

        suspicious = [
            "192.168.1.100",
            "192.168.1.200"
        ]

        st.success("Monitor Agent: Suspicious activity detected")

        # Analyst Agent
        with st.spinner("Analyst Agent: Analyzing using RAG..."):
            time.sleep(2)

        threats = {
            "192.168.1.100": "Brute Force Attack",
            "192.168.1.200": "SQL Injection Attack"
        }

        st.session_state.threats = threats

        st.success("Analyst Agent: Threat identified")

        # Remediation Agent
        with st.spinner("Remediation Agent: Blocking malicious IPs..."):
            time.sleep(2)

        st.session_state.blocked_ips = list(threats.keys())

        st.success("Remediation Agent: System secured")

# Display Threats
st.subheader("🚨 Detected Threats")

if st.session_state.threats:
    threat_df = pd.DataFrame(
        list(st.session_state.threats.items()),
        columns=["IP Address", "Threat Type"]
    )
    st.table(threat_df)
else:
    st.info("No threats detected")

# Display Blocked IPs
st.subheader("🔒 Blocked IPs")

if st.session_state.blocked_ips:
    blocked_df = pd.DataFrame(
        st.session_state.blocked_ips,
        columns=["Blocked IP"]
    )
    st.table(blocked_df)
else:
    st.info("No blocked IPs")

# Footer
st.write("---")
st.write("AI-Sentinel Demo | Multi-Agent RAG Security System")