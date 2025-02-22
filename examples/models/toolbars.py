''' This example shows multiple ways to place the toolbar and the x and y axes
with respect to the plot

.. bokeh-example-metadata::
    :apis: bokeh.layouts.column, bokeh.layouts.row, bokeh.plotting.figure, bokeh.plotting.show
    :refs: :ref:`ug_interaction_tools_toolbar`
    :keywords: tools, toolbar, axes, layout

'''
import numpy as np

from bokeh.layouts import column, row
from bokeh.plotting import figure, show

N = 1000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = np.array([(r, g, 150) for r, g in zip(50+2*x, 30+2*y)], dtype="uint8")

TOOLS="hover,crosshair,pan,reset,box_select"

def mkplot(toolbar, xaxis, yaxis):
    p = figure(width=300, height=300, tools=TOOLS, toolbar_location=toolbar, x_axis_location=xaxis, y_axis_location=yaxis)
    p.scatter(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)
    return p

p_lbl = mkplot(toolbar="left",  xaxis="below", yaxis="left")
p_lbr = mkplot(toolbar="left",  xaxis="below", yaxis="right")
p_rbl = mkplot(toolbar="right", xaxis="below", yaxis="left")
p_rbr = mkplot(toolbar="right", xaxis="below", yaxis="right")

p_lal = mkplot(toolbar="left",  xaxis="above", yaxis="left")
p_lar = mkplot(toolbar="left",  xaxis="above", yaxis="right")
p_ral = mkplot(toolbar="right", xaxis="above", yaxis="left")
p_rar = mkplot(toolbar="right", xaxis="above", yaxis="right")

p_abl = mkplot(toolbar="above", xaxis="below", yaxis="left")
p_aal = mkplot(toolbar="above", xaxis="above", yaxis="left")
p_bbl = mkplot(toolbar="below", xaxis="below", yaxis="left")
p_bal = mkplot(toolbar="below", xaxis="above", yaxis="left")

p_abr = mkplot(toolbar="above", xaxis="below", yaxis="right")
p_aar = mkplot(toolbar="above", xaxis="above", yaxis="right")
p_bbr = mkplot(toolbar="below", xaxis="below", yaxis="right")
p_bar = mkplot(toolbar="below", xaxis="above", yaxis="right")

layout = column(
    row(p_lbl, p_lbr, p_lal, p_lar),
    row(p_rbl, p_rbr, p_ral, p_rar),
    row(p_abl, p_aal, p_abr, p_aar),
    row(p_bbl, p_bal, p_bbr, p_bar),
)

show(layout)
