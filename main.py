# -*- coding: utf-8 -*-
"""
Created by Oscar Palmgren on 2025-02-15

(c) Copyright 2025 Oscar Palmgren
"""

import streamlit as st

st.set_page_config(page_title = "Radiance Material Generator",
                   page_icon = ':material/nest_true_radiant:')

home = st.Page(page = "start.py",
               title = "Start")

opaque = st.Page(page = "opaque.py",
                 title = "Opaque Materials")

transparent = st.Page(page = "transparent.py",
                      title = "Transparent Materials")

tutorial_0 = st.Page(page = "tutorial_0.py",
                     title = "NCS Colour to Radiance Material")

pages = st.navigation(pages = {"General":[home],
                               "Generators":[opaque, transparent],
                               "Tutorials":[tutorial_0]})

pages.run()

st.sidebar.markdown("Copyright © 2025 Oscar Palmgren. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).")