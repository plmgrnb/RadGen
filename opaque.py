# -*- coding: utf-8 -*-
"""
Created by Oscar Palmgren on 2025-02-15

(c) Copyright 2025 Oscar Palmgren
"""

import streamlit as st

st.header("Opaque Material", anchor = False)

st.markdown("""
            **Plastic materials** simulate non-reflective surfaces with varying levels of specularity and roughness, providing a realistic representation of matte surfaces.
            **Metal materials** mimic reflective surfaces with higher specularity, accurately depicting polished and brushed finishes.
            """)

def calculate(name, reflectance, specularity, roughness, R, G, B):
    try:
        luminousEfficacy_R = 0.30
        luminousEfficacy_G = 0.59
        luminousEfficacy_B = 0.11
        
        luminousEfficacy = R * luminousEfficacy_R + G * luminousEfficacy_G + B * luminousEfficacy_B
        
        reflectance_R = round(R / luminousEfficacy * reflectance, 3)
        reflectance_G = round(G / luminousEfficacy * reflectance, 3)
        reflectance_B = round(B / luminousEfficacy * reflectance, 3)
        
        return(reflectance_R, reflectance_G, reflectance_B)
    except:
        reflectance_R = 0
        reflectance_G = 0
        reflectance_B = 0
        
        return(reflectance_R, reflectance_G, reflectance_B)

with st.container():
    cola, colb = st.columns([2, 1])

    with colb:
        advanced = st.toggle(label = "Advanced",
                             value = False)
    
    colc, cold = st.columns(2)

    if advanced:
        with colc:
            name = st.text_input(label = "Material Name",
                                 help = "Enter material name as one word, *without* any spaces.")
            
            material_type = st.selectbox(label = "Material Type",
                                         options = ["Plastic", "Metal"],
                                         help = "Select material type. Plastic represents most materials with low specularity and uncoloured specular highlights, while metal represents materials with high specularity and coloured specular highlights.")
            
            specularity = st.number_input(label = "Specularity",
                                          min_value = 0.000,
                                          max_value = 1.000,
                                          help = "Enter measured specularity as a fraction with three decimal accuracy. Specularity of 0 indicates a perfectly diffuse surface. Typically below 0.1 in plastic materials, and above 0.9 in metal materials.")
            
            roughness = st.number_input(label = "Roughness",
                                        min_value = 0.000,
                                        max_value = 1.000,
                                        help = "Enter measured roughness as a fraction with three decimal accuracy. Roughness of 0 indicates a perfectly smooth surface. Usually doesn't exceed 0.2.")
            
        with cold:
            reflectance = st.number_input(label = "Reflectance",
                                          min_value = 0.000,
                                          max_value = 1.000,
                                          help = "Enter measured reflectance as a fraction with three decimal accuracy.")
            
            R = st.number_input(label = "Red",
                                min_value = 0,
                                max_value = 255,
                                help = "Enter colour as RGB-value.")
            
            G = st.number_input(label = "Green",
                                min_value = 0,
                                max_value = 255)
            
            B = st.number_input(label = "Blue",
                                min_value = 0,
                                max_value = 255)
        
        reflectance_R, reflectance_G, reflectance_B = calculate(name, reflectance, specularity, roughness, R, G, B)
        
    else:
        with colc:
            name = st.text_input(label = "Material Name",
                                 help = "Enter material name as one word, *without* any spaces.")
        with cold:
            reflectance = st.number_input(label = "Reflectance / %",
                                          min_value = 0,
                                          max_value = 100,
                                          help = "Enter reflectance in percent as integer.")
        
        material_type = "plastic"
        
        specularity = 0
        
        roughness = 0
        
        reflectance_R = round(reflectance / 100, 3)
        reflectance_G = round(reflectance / 100, 3)
        reflectance_B = round(reflectance / 100, 3)

with st.container():
    line0 = "void " + material_type.lower() + " " + name
    line1 = "0"
    line2 = "0"
    line3 = "5 " + str(reflectance_R) + " " + str(reflectance_G) + " " + str(reflectance_B) + " " + str(round(specularity, 3)) + " " + str(round(roughness, 3))

    data = line0 + "  \n" + line1 + "  \n" + line2 + "  \n" + line3

    cole, colf = st.columns(2)
    
    with colf:
        st.download_button(label = "Download Material",
                           data = data,
                           file_name = name + ".rad",
                           type = "primary",
                           use_container_width = True)
        
        with st.expander(label = "Preview Material"):
            st.write(data)