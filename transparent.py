# -*- coding: utf-8 -*-
"""
Created by Oscar Palmgren on 2025-02-15

(c) Copyright 2025 Oscar Palmgren
"""

import streamlit as st
import math

st.header("Transparent Material", anchor = False)

st.markdown("""
            The **glass material** simulates transparent surfaces with varying levels transmissivity, accurately representing glass.
            It captures how light passes through and refracts within these surfaces, creating realistic visual effects.
            
            **Radiance** uses *transmissivity* for glass materials, while glazing is typically measured with *transmittance*.
            The material generator converts the measured *transmittance* for use in **Radiance** automatically.
            """)

def calculateSimple(name, transmittance):
    try:
        transmittance = transmittance / 100
    
        transmissivity = (math.sqrt(0.8402528435 + 0.0072522239 * transmittance ** 2) - 0.9166530661) / 0.0036261119 / transmittance
    
        return(transmissivity)
    
    except:
        transmissivity = 0
        
        return(transmissivity)

def calculateAdvanced(name, transmittance_R, transmittance_G, transmittance_B, refraction):
    try:
        transmissivity_R = (math.sqrt(0.8402528435 + 0.0072522239 * transmittance_R ** 2) - 0.9166530661) / 0.0036261119 / transmittance_R
        transmissivity_G = (math.sqrt(0.8402528435 + 0.0072522239 * transmittance_G ** 2) - 0.9166530661) / 0.0036261119 / transmittance_G
        transmissivity_B = (math.sqrt(0.8402528435 + 0.0072522239 * transmittance_B ** 2) - 0.9166530661) / 0.0036261119 / transmittance_B
    
        return(transmissivity_R, transmissivity_G, transmissivity_B)
    
    except:
        transmissivity_R = 0
        transmissivity_G = 0
        transmissivity_B = 0
        
        return(transmissivity_R, transmissivity_G, transmissivity_B)

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
            
            refraction = st.number_input(label = "Refractive Index",
                                         min_value = 0.000,
                                         max_value = None,
                                         value = 1.52,
                                         help = "Enter the refractive index with three decimal accuracy. The refractive index of glass is 1.52.")
            
        with cold:
            transmittance_R = st.number_input(label = "Red",
                                              min_value = 0.000,
                                              max_value = 1.000,
                                              help = "Enter measured transmittance per colour as a fraction with three decimal accuracy.")
            
            transmittance_G = st.number_input(label = "Green",
                                              min_value = 0.000,
                                              max_value = 1.000)
            
            transmittance_B = st.number_input(label = "Blue",
                                              min_value = 0.000,
                                              max_value = 1.000)
            
        transmissivity_R, transmissivity_G, transmissivity_B = calculateAdvanced(name, transmittance_R, transmittance_G, transmittance_B, refraction)
        
    else:
        with colc:
            name = st.text_input(label = "Material Name",
                                 help = "Enter material name as one word, *without* any spaces.")
        with cold:
            transmittance = st.number_input(label = "Transmittance / %",
                                            min_value = 0,
                                            max_value = 100,
                                            help = "Enter transmittance in percent as integer.")
        
        refraction = 1.52
        
        transmissivity = calculateSimple(name, transmittance)
        
        transmissivity_R = round(transmissivity, 3)
        transmissivity_G = round(transmissivity, 3)
        transmissivity_B = round(transmissivity, 3)

with st.container():
    line0 = "void glass " + name
    line1 = "0"
    line2 = "0"
    line3 = "3 " + str(transmissivity_R) + " " + str(transmissivity_G) + " " + str(transmissivity_B) + " " + str(refraction)

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