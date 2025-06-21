import sys
import streamlit as st

st.title("Environment Checker")

st.write("🔍 Python Executable Path:")
st.code(sys.executable)

st.write("📦 Installed TensorFlow Version:")
try:
    import tensorflow as tf
    st.success(f"TensorFlow is installed: v{tf.__version__}")
except Exception as e:
    st.error(f"TensorFlow not found or error: {e}")
