import streamlit as st
import forallpeople as si
from handcalcs.decorator import handcalc
from func_handcalcs import compressive_strength

si.environment("structural")

A_value = st.sidebar.number_input("Section Area ($mm^2$)", value=2500)
#a_value = st.sidebar.number_input("Section Height (mm)", value=50)
#b_value = st.sidebar.number_input("Section width (mm)", value=50)
fy_value = st.sidebar.number_input("Steel yield strength (MPa)", value=355)

A = A_value * si.mm**2
#a = a_value * si.mm
#b = b_value * si.mm
fy = fy_value * si.MPa

N_Rd_latex, N_Rd_value = compressive_strength(A, fy)

st.markdown("# Compressive strength of beam cross-sections")
st.subheader("This is a subheader")
st.latex(N_Rd_latex)