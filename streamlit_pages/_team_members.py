import streamlit as st
from config import TEAM_MEMBERS, DEFAULT_IMAGE

def team_members():
    # Define centralized CSS for styling
    st.markdown(
        """
        <style>
        .team-card {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            height: 350px; /* Fixed height to ensure equal size */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .team-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        .team-image-wrapper {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            overflow: hidden;
            margin: 0 auto 10px auto;
        }
        .team-name {
            color: #ffffff;
            font-size: 22px;
            margin: 0;
        }
        .team-role {
            color: #aaaaaa;
            font-size: 16px;
            margin: 5px 0;
        }
        .team-links {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 10px;
        }
        .team-links a {
            color: #1e90ff;
            text-decoration: none;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .team-links a:hover {
            text-decoration: underline;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header
    st.header("Meet Our Dedicated Team Members", anchor=False)

    # Validate TEAM_MEMBERS
    if not TEAM_MEMBERS or not isinstance(TEAM_MEMBERS, list):
        st.error("Team members data is missing or invalid.")
        return
    if len(TEAM_MEMBERS) < 4:
        st.warning("Please provide at least 4 team members for the 2x2 grid layout.")
        return

    # Create a 2x2 grid for 4 team members
    # First row
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="team-card">', unsafe_allow_html=True)
        st.markdown('<div class="team-image-wrapper">', unsafe_allow_html=True)
        try:
            st.image(TEAM_MEMBERS[0]['image'], width=120, caption="", clamp=True, output_format="JPEG")
        except Exception as e:
            st.warning(f"Failed to load image for {TEAM_MEMBERS[0]['name']}: {str(e)}")
            st.image(DEFAULT_IMAGE, width=120, caption="Default Image", clamp=True, output_format="JPEG")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <h3 class="team-name">{TEAM_MEMBERS[0]['name']}</h3>
            <p class="team-role">{TEAM_MEMBERS[0]['role']}</p>
            <div class="team-links">
                <a href="{TEAM_MEMBERS[0]['links'][0]}" target="_blank">🔗 LinkedIn</a>
                <a href="{TEAM_MEMBERS[0]['links'][1]}" target="_blank">🐙 GitHub</a>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="team-card">', unsafe_allow_html=True)
        st.markdown('<div class="team-image-wrapper">', unsafe_allow_html=True)
        try:
            st.image(TEAM_MEMBERS[1]['image'], width=120, caption="", clamp=True, output_format="JPEG")
        except Exception as e:
            st.warning(f"Failed to load image for {TEAM_MEMBERS[1]['name']}: {str(e)}")
            st.image(DEFAULT_IMAGE, width=120, caption="Default Image", clamp=True, output_format="JPEG")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <h3 class="team-name">{TEAM_MEMBERS[1]['name']}</h3>
            <p class="team-role">{TEAM_MEMBERS[1]['role']}</p>
            <div class="team-links">
                <a href="{TEAM_MEMBERS[1]['links'][0]}" target="_blank">🔗 LinkedIn</a>
                <a href="{TEAM_MEMBERS[1]['links'][1]}" target="_blank">🐙 GitHub</a>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # Second row
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="team-card">', unsafe_allow_html=True)
        st.markdown('<div class="team-image-wrapper">', unsafe_allow_html=True)
        try:
            st.image(TEAM_MEMBERS[2]['image'], width=120, caption="", clamp=True, output_format="JPEG")
        except Exception as e:
            st.warning(f"Failed to load image for {TEAM_MEMBERS[2]['name']}: {str(e)}")
            st.image(DEFAULT_IMAGE, width=120, caption="Default Image", clamp=True, output_format="JPEG")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <h3 class="team-name">{TEAM_MEMBERS[2]['name']}</h3>
            <p class="team-role">{TEAM_MEMBERS[2]['role']}</p>
            <div class="team-links">
                <a href="{TEAM_MEMBERS[2]['links'][0]}" target="_blank">🔗 LinkedIn</a>
                <a href="{TEAM_MEMBERS[2]['links'][1]}" target="_blank">🐙 GitHub</a>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="team-card">', unsafe_allow_html=True)
        st.markdown('<div class="team-image-wrapper">', unsafe_allow_html=True)
        try:
            st.image(TEAM_MEMBERS[3]['image'], width=120, caption="", clamp=True, output_format="JPEG")
        except Exception as e:
            st.warning(f"Failed to load image for {TEAM_MEMBERS[3]['name']}: {str(e)}")
            st.image(DEFAULT_IMAGE, width=120, caption="Default Image", clamp=True, output_format="JPEG")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <h3 class="team-name">{TEAM_MEMBERS[3]['name']}</h3>
            <p class="team-role">{TEAM_MEMBERS[3]['role']}</p>
            <div class="team-links">
                <a href="{TEAM_MEMBERS[3]['links'][0]}" target="_blank">🔗 LinkedIn</a>
                <a href="{TEAM_MEMBERS[3]['links'][1]}" target="_blank">🐙 GitHub</a>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)