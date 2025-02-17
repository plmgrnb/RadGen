# -*- coding: utf-8 -*-
"""
Created by Oscar Palmgren on 2025-02-15

(c) Copyright 2025 Oscar Palmgren
"""

import streamlit as st

st.title("Radiance Material Generator", anchor = None)

with st.container():
    st.markdown("""
                **Radiance** is a powerful tool used for lighting simulation.
                It employs ray tracing to predict light levels in indoor environments.
                **Radiance** is widely used in architecture to create realistic assessnents of spaces before they are built.

                **Radiance** materials define the way light interacts with a surface.
                The optical properties of materials control the appearance and behavior of surfaces in the simulation.
                
                The generator allows the creation of both opaque and transparent **Radiance** materials.
                These materials can be downloaded as *.rad* material files.
                For walkthroughs on material creation and installation, visit the tutorial section.
                """)
    
    st.info(body = "For details, read the [Radiance documentation](https://radsite.lbl.gov/radiance/refer/ray.html)!",
            icon = ":material/lightbulb:")
    
    st.markdown("""
                The **Radiance** material generator was created by Oscar Palmgren.
                It's licensed under [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
                Please provide attribution if you found the material generator useful!
                """)