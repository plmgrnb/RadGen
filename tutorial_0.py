# -*- coding: utf-8 -*-
"""
Created by Oscar Palmgren on 2025-02-15

(c) Copyright 2025 Oscar Palmgren
"""

import streamlit as st

st.header("NCS Colour to Radiance Material")

st.markdown("""
            The *Natural Colour System (NCS)* is a colour notation system based on human perception of colours, developed by the *Scandinavian Colour Institute*.
            It uses six elementary colours — *white*, *black*, *red*, *green*, *blue*, and *yellow* — as a foundation, and every other colour is described in terms of its similarity to these.
            For example, a specific shade of blue might be represented as a blend of blue and black, with a hint of green.
            The NCS is widely used in architecture and interior design because it offers a scientifically-based way to communicate colours accurately.
            
            Translating *NCS* colours into *Radiance* materials should be a fundamental skill for any architect, engineer, and designer involved in interior daylight assessment.
            This capability is essential for accurately predicting daylight provision in indoor environments according to their intended design.
            
            In this tutorial we'll walk through how to translate an *NCS* colour into a *Radiance* material.
            """)

st.subheader("1. Navigating the NCS")

st.markdown("""
            The *Scandinavian Colour Institute* offers a free application called *NCS+*, which provides an index of the colors in the *NCS*.
            It is available as a mobile app for *iOS* and *Android*, as well as a browser app.
            In this tutorial, we will use the **browser app**, but the mobile apps are equally easy to navigate.
            
            Navigate to [*NCS+*](https://app.ncscolour.com/) (when prompted, log in to or sign up for a free account).
            On the landing page, click *BROWSE Colours* to reach the database of all indexed colours.
            The database can be browsed for colours, or the exact colour code be searched for using the search bar.
            """)
            
st.video(data = 'media\Tutorial_0_Video_A1_1080p.mp4',
         autoplay = True,
         loop = True,
         muted = True)

st.markdown("""
            Upon selecting a colour, the colour details are shown, some of which we need to take note.
            
            Firstly, the *NCS* colour code, which is composed of three parts - *blackness*, *chromaticness*, and *hue*.
            It's good practice to name *Radiance* materials according to their colour code.
            
            Secondly, the *sRGB* values for the red, green, and blue components of the colour.
            These values ensure an identical appearance when the colour is rendered in *Radiance*.
            
            And thirdly, the *Light Reflectance Value* measured for the colour.
            This value ensures appropriate behaviour of the *Radiance* material.
            """)

st.video(data = 'media\Tutorial_0_Video_A2_1080p.mp4',
         autoplay = True,
         loop = True,
         muted = True)

st.markdown("""
            Great, we now posess all the information required to create our *Radiance* material!
            """)

st.subheader("2. Creating the Radiance Material")

st.markdown("""
            Next, we'll translate the selected *NCS* colour into a *Radiance* material using its colour code, *sRGB* values and *Light Reflectance Value*.
            
            To begin, launch the *Opaque Materials* generator, and enable the **advanced** settings.
            """)

st.video(data = 'media\Tutorial_0_Video_B1_1080p.mp4',
         autoplay = True,
         loop = True,
         muted = True)

st.markdown("""
            Firstly, enter the colour code into *Material Name*, **without** any spaces.
            It's good practice to name *Radiance* materials according to their colour code.
            
            Also, make sure the *Plastic* material type is selected, which simulates non-reflective surfaces.
            
            Secondly, enter the *sRBG* values for the red, green, and blue components of the colour into the respective fields.
            These values ensure an identical appearance when the colour is rendered in *Radiance*.
            
            Thirdly, enter the *Light Reflectance Value* measured for the colour into *Reflectance* as a fraction.
            The *NCS+* application provides the *Light Reflectance Value* in percent, which we need to convert into a fraction.
            This value ensures appropriate behaviour of the *Radiance* material.
            """)

st.info(body =
        """
        **Pro tip!** Convert *Light Reflectance Value* to *Reflectance*.
        
        Devide the *Light Reflectance Value* by one hundred to get a fraction.
        """,
        icon = ":material/lightbulb:")

st.markdown("""
            Optionally, enter the desired *specularity* and *roughness* as fractions.
            
            Specularity indicates the "shinyness" of a surface, ranging from perfectly diffuse to polished and brushed finishes.
            It is typically below 0.1 in plastic materials, and can be left at the default value of zero for most purposes.
            
            Roughness indicates the "bupyness" of a surface, ranging from perfectly smooth to jagged finishes.
            It is typically below 0.2 in plastic materials, and can be left at the default value of zero for most purposes.
            """)

st.video(data = 'media\Tutorial_0_Video_B2_1080p.mp4',
         autoplay = True,
         loop = True,
         muted = True)

st.markdown("""
            The *NCS* colour has now been translated into a *Radiance* material!
            All that's left is to click the big, red *Download Material* button, and our download should begin promplty.
            
            The material comes in the form of a *.rad* material file, which can be installed in our choice of interface for *Radiance*.
            """)

st.info(body =
        """
        **Pro tip!** Preview the material.
        
        The material can be previewed in the drop-down below the big, red *Download Material* button.
        """,
        icon = ":material/lightbulb:")