# Analysis 5: Births By District Over Time

[← Back to main README](../README.md)

## What this shows
An animated choropleth map of births by district, year by year from 1993 through 2025, drag the slider to see how the distribution shifts over time (as seen in the recording below) 


## Method
Grouped the cleaned dataset by `year`, `district_code`, and `district_name`, summing `births`  
Joined to the district boundary GeoJSON, with `year` on Tableau's Pages shelf to drive the animation, and the color scale locked to a fixed range (1–423) across all years so shading stays comparable frame to frame 

## Visualization

<video src="../visualizations/analysis-5.mp4" controls width="700"></video>

## Observations
- The far-west district (Altstetten) is the darkest shape in nearly every frame across the full 33 years; its lead over the rest of the city isn't recent, it's consistent 
- The central old-town cluster stays the lightest area on the map throughout 
- Overall map saturation deepens through the 2010s, peaking around 2021, then eases slightly by 2025; the citywide rise-then-pullback from Analysis 1 shows up spatially here too
