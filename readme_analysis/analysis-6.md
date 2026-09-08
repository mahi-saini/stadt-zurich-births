# Analysis 6: Year-on-Year Percentage Change By District 

[← Back to main README](../README.md)

## What this shows
Year-over-year percentage change in births for every district, drag the year slider to see how much each district's births grew or shrank compared to the previous year (as seen in the recording below)

## Method
Computed as `(current_year_births - previous_year_births) / previous_year_births` per district, using pandas' `pct_change()`. Infinite values (from districts going from zero births one year to nonzero the next) were replaced with null rather than left in, since a true division-by-zero would otherwise distort the chart. Kept all 34 districts rather than filtering to a top few, and used a year range filter so that both multi-year figures and one real year's actual number can be viewed 

## Visualization

<video src="../visualizations/analysis-6.mp4" controls width="700"></video>

## Observations
- No single district shows a sustained one-directional trend across every year, growth and decline both bounce around from year to year rather than compounding steadily in one direction

## A technical note
This was the trickiest chart in the project. Two earlier attempts didn't work: an animated bar-chart-race (bars reordering live) turned out to require data in long format plus a `RANK()` table calculation that Tableau can't apply cleanly to wide-format data, and a full heatmap version got dominated by the same tiny-district outlier problem the axis-locking above solves more simply. The year filter range ended up being the version that actually shipped
