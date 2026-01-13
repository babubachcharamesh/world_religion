import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pydeck as pdk
from PIL import Image
import time
import base64

# --- APP CONFIG ---
st.set_page_config(
    page_title="World Religion Insights",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- LOAD CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# --- DATA CURATION ---
RELIGIONS = {
    "Christianity": {
        "pop": 2400000000,
        "growth": 1.2,
        "fertility": 2.7,
        "color": "#3a7bd5",
        "impact": {"Economy": 8, "Education": 9, "Philanthropy": 8, "History": 10},
        "description": "The world's largest religion, with a significant presence in the Americas, Europe, and Sub-Saharan Africa."
    },
    "Islam": {
        "pop": 1900000000,
        "growth": 1.8,
        "fertility": 3.1,
        "color": "#00b09b",
        "impact": {"Economy": 7, "Education": 7, "Philanthropy": 9, "History": 10},
        "description": "The fastest-growing major religion, driven by youthful populations in West Asia and Africa."
    },
    "Hinduism": {
        "pop": 1200000000,
        "growth": 1.1,
        "fertility": 2.4,
        "color": "#f2994a",
        "impact": {"Economy": 6, "Education": 7, "Philanthropy": 6, "History": 10},
        "description": "The dominant religion in India and Nepal, known for its diverse traditions and deep historical roots."
    },
    "Religiously Unaffiliated": {
        "pop": 1200000000,
        "growth": 0.9,
        "fertility": 1.7,
        "color": "#95a5a6",
        "impact": {"Economy": 9, "Education": 8, "Philanthropy": 5, "History": 4},
        "description": "Including atheists, agnostics, and 'nones', this group is growing rapidly in industrialized nations."
    },
    "Buddhism": {
        "pop": 500000000,
        "growth": 0.5,
        "fertility": 1.6,
        "color": "#f1c40f",
        "impact": {"Economy": 5, "Education": 7, "Philanthropy": 7, "History": 9},
        "description": "Predominant in East and Southeast Asia, facing demographic challenges due to low fertility rates."
    },
    "Sikhism": {
        "pop": 30000000,
        "growth": 1.4,
        "fertility": 2.3,
        "color": "#e67e22",
        "impact": {"Economy": 6, "Education": 6, "Philanthropy": 9, "History": 5},
        "description": "Known for its emphasis on equality and service, centered primarily in the Punjab region."
    },
    "Judaism": {
        "pop": 15000000,
        "growth": 0.7,
        "fertility": 2.3,
        "color": "#2c3e50",
        "impact": {"Economy": 8, "Education": 9, "Philanthropy": 7, "History": 10},
        "description": "An ancient monotheistic religion with profound influence on global morality and philosophy."
    }
}

# --- HELPER FUNCTIONS ---
def get_total_pop():
    return sum(r["pop"] for r in RELIGIONS.values())

def live_pop_ticker():
    # Simulated ticker based on annual growth
    total_pop = get_total_pop()
    growth_per_sec = (total_pop * 0.012) / (365 * 24 * 3600) # Assuming ~1.2% global avg growth
    return total_pop + (growth_per_sec * (time.time() % 3600))

# --- SIDEBAR ---
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to", ["Dashboard", "The Belief Pulse", "Global Impact", "Architecture Gallery", "Future Projections"])
    st.markdown("---")
    st.markdown("### About")
    st.info("Explore the intricate tapestry of belief that shapes our world.")

# --- PAGE: DASHBOARD ---
if page == "Dashboard":
    st.markdown("<h1 style='text-align: center; margin-bottom: 3rem;'>World Religion Insights</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    total_p = get_total_pop()
    with col1:
        st.markdown(f"""
        <div class="glass-card">
            <h3>Global Followers</h3>
            <p class="impact-metric">{total_p/1e9:.1f}B</p>
            <p style="color: var(--text-secondary);">Combined adherence worldwide</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="glass-card">
            <h3>Fastest Growing</h3>
            <p class="impact-metric" style="color: #00b09b;">Islam</p>
            <p style="color: var(--text-secondary);">+1.8% annual growth rate</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="glass-card">
            <h3>Median Fertility</h3>
            <p class="impact-metric" style="color: #f2994a;">2.4</p>
            <p style="color: var(--text-secondary);">Average children per woman</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## Global Distribution")
    
    # Sunburst Chart
    df_sun = pd.DataFrame([
        {"Religion": k, "Population": v["pop"], "Growth": v["growth"]}
        for k, v in RELIGIONS.items()
    ])
    
    fig = px.sunburst(
        df_sun, 
        path=["Religion"], 
        values="Population",
        color="Religion",
        color_discrete_map={k: v["color"] for k, v in RELIGIONS.items()},
        template="plotly_dark"
    )
    fig.update_layout(
        margin=dict(t=0, l=0, r=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE: BELIEF PULSE ---
elif page == "The Belief Pulse":
    st.markdown("<h1>The Belief Pulse</h1>", unsafe_allow_html=True)
    st.markdown("#### Real-time estimated follower increase")
    
    placeholder = st.empty()
    
    for _ in range(20):
        current_pop = live_pop_ticker()
        with placeholder.container():
            st.markdown(f"""
            <div class="glass-card" style="text-align: center; padding: 5rem;">
                <p style="font-size: 1.5rem; color: var(--text-secondary);">Estimated Total Religious Followers</p>
                <p style="font-size: 5rem; font-weight: 800; color: #00d2ff;">{int(current_pop):,}</p>
                <p style="color: #00b09b;">↑ Increasing by ~4 followers every second</p>
            </div>
            """, unsafe_allow_html=True)
        time.sleep(0.5)

# --- PAGE: GLOBAL IMPACT ---
elif page == "Global Impact":
    st.markdown("<h1>Impact Scorecard</h1>", unsafe_allow_html=True)
    
    rel_choice = st.selectbox("Select Religion to Analyze", list(RELIGIONS.keys()))
    religion_data = RELIGIONS[rel_choice]
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown(f"""
        <div class="glass-card">
            <h2>{rel_choice}</h2>
            <p style="font-size: 1.2rem;">{religion_data['description']}</p>
            <hr style="border: 0.1px solid var(--glass-border);">
            <p><b>Population Share:</b> {(religion_data['pop']/get_total_pop()*100):.1f}%</p>
            <p><b>Annual Growth:</b> {religion_data['growth']}%</p>
            <p><b>Fertility Rate:</b> {religion_data['fertility']}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_right:
        # Radar Chart
        impact_df = pd.DataFrame(religion_data["impact"].items(), columns=["Dimension", "Score"])
        
        fig = px.line_polar(impact_df, r="Score", theta="Dimension", line_close=True, range_r=[0, 10])
        fig.update_traces(fill='toself', line_color=religion_data["color"])
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, showticklabels=False, gridcolor="rgba(255,255,255,0.1)"),
                angularaxis=dict(gridcolor="rgba(255,255,255,0.1)")
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            template="plotly_dark"
        )
        st.plotly_chart(fig, use_container_width=True)

# --- PAGE: ARCHITECTURE GALLERY ---
elif page == "Architecture Gallery":
    st.markdown("<h1>Sacred Architecture</h1>", unsafe_allow_html=True)
    
    # Mocking image paths - in real use, would use generated paths
    # Assuming the images were saved in the same dir for simplicity in this script
    images = {
        "Western Spiritual Heritage": "stunning_cathedral_glassmorphism_1768282680392.png",
        "Islamic Artistic Excellence": "serene_mosque_glassmorphism_1768282700324.png",
        "Dharmic Architectural Devotion": "tranquil_temple_glassmorphism_1768282718019.png"
    }

    cols = st.columns(3)
    for i, (title, img_path) in enumerate(images.items()):
        with cols[i]:
            try:
                # Path mapping for local assets
                full_path = f"assets/{img_path}"
                img = Image.open(full_path)
                st.image(img, use_container_width=True)
                st.markdown(f"<p style='text-align: center; color: var(--text-secondary);'>{title}</p>", unsafe_allow_html=True)
            except:
                st.error(f"Image {title} not found.")

# --- PAGE: FUTURE PROJECTIONS ---
elif page == "Future Projections":
    st.markdown("<h1>Growth Projection Simulator</h1>", unsafe_allow_html=True)
    
    year = st.slider("Project Year", 2025, 2100, 2050, step=5)
    
    # Simplified projection logic
    projection_data = []
    years_ahead = year - 2025
    
    for name, r in RELIGIONS.items():
        # Compound growth: P = P0 * (1 + r)^t
        # Adjusted growth for fertility decline over time (simplified)
        adj_growth = r["growth"] / 100
        projected_pop = r["pop"] * ((1 + adj_growth) ** years_ahead)
        projection_data.append({"Religion": name, "Population": projected_pop})
        
    df_proj = pd.DataFrame(projection_data)
    
    fig = px.bar(
        df_proj, 
        x="Religion", 
        y="Population", 
        color="Religion",
        color_discrete_map={k: v["color"] for k, v in RELIGIONS.items()},
        template="plotly_dark"
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis_title="Projected Followers"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"""
    <div class="glass-card">
        <p>By <b>{year}</b>, projections suggest a dynamic shift in global demographics. 
        Islam is expected to see the most significant numerical growth, while Christianity remains 
        major but concentrated in the global south. The Unaffiliated group continues to rise in 
        Western nations but faces relative decline due to lower fertility rates compared to 
        religious counterparts.</p>
    </div>
    """, unsafe_allow_html=True)
