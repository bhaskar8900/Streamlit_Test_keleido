# streamlit_piechart_to_png.py
 
import streamlit as st
import plotly.express as px
import plotly.io as pio
import time
import os
 
# Ensure output directory exists
os.makedirs("temp_report", exist_ok=True)
 
# --- UI Section ---
st.title("Pie Chart to PNG - Fast Export with Kaleido")
st.markdown("This app creates a Plotly pie chart and saves it as a PNG using `write_image()` without HTML conversion.")
 
# Sample data
labels = ["Boiler Loss", "Radiation Loss", "Flue Gas Loss", "Unburnt Carbon Loss"]
values = [30, 10, 45, 15]
 
# Create Plotly Pie Chart
fig = px.pie(
    names=labels,
    values=values,
    title="Boiler Loss Breakdown",
    hole=0.3,
    color_discrete_sequence=px.colors.qualitative.Plotly
)
 
# Display Plotly chart
st.plotly_chart(fig, use_container_width=True)
 
# Button to save as PNG
if st.button("Save as PNG"):
    with st.spinner("Saving PNG..."):
        start_time = time.perf_counter()
 
        timestamp = int(time.time() * 1000)
        png_path = f"temp_report/pie_chart_{timestamp}.png"
 
        try:
            # Save image directly using Kaleido
            fig.write_image(png_path, format='png')
            end_time = time.perf_counter()
 
            elapsed = end_time - start_time
 
            # Save to session state
            st.session_state["boiler_graph_path_d"] = png_path
 
            st.success(f"✅ Image saved to `{png_path}` in **{elapsed:.3f} seconds**")
        except Exception as e:
            st.error(f"❌ Failed to save image: {e}")
 
# If saved, show image
if "boiler_graph_path_d" in st.session_state:
    st.image(st.session_state["boiler_graph_path_d"], caption="Saved PNG Image", use_column_width=True)
 
 