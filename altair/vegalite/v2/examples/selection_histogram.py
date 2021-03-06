"""
Selection Histogram
===================
This chart shows an example of using an interval selection to filter the
contents of an attached histogram, allowing the user to see the proportion
of items in each category within the selection.
"""
# category: interactive charts
import altair as alt
from vega_datasets import data

cars = data.cars.url

brush = alt.selection(type='interval')

points = alt.Chart().mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
).add_selection(
    brush
)

bars = alt.Chart().mark_bar().encode(
    y='Origin:N',
    color='Origin:N',
    x='count(Origin):Q'
).transform_filter(
    brush
)

alt.vconcat(points, bars, data=cars)
