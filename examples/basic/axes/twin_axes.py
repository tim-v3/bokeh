'''This example shows how to add a secondary y-axis to a figure and set a color
for the label values.

.. bokeh-example-metadata::
    :apis: bokeh.plotting.figure.add_layout, bokeh.plotting.figure.scatter, bokeh.models.LinearAxis
    :refs: :ref:`ug_basic_axes_twin`
    :keywords: add_layout, axis, axis_label, axis_label_text_color, scatter, extra_y_ranges, LinearAxis

'''
from numpy import arange, linspace, pi, sin

from bokeh.models import LinearAxis, LinearScale, Range1d
from bokeh.palettes import Sunset6
from bokeh.plotting import figure, show

x = arange(-2*pi, 2*pi, 0.2)
y = sin(x)
y2 = linspace(0, 100, len(x))

blue, red = Sunset6[2], Sunset6[5]

p = figure(x_range=(-2*pi, 2*pi), y_range=(-1, 1))
p.background_fill_color = "#fafafa"

p.scatter(x, y, line_color="black", fill_color=blue, size=12)
p.axis.axis_label = "light blue circles"
p.axis.axis_label_text_color = blue

p.extra_x_ranges['foo'] = Range1d(start=-2*pi, end=2*pi)
p.extra_x_scales['foo'] = LinearScale()
p.extra_y_ranges['foo'] = Range1d(0, 100)
p.extra_y_scales['foo'] = LinearScale()
p.scatter(x, y2, color=red, size=8, y_range_name="foo")

ax2 = LinearAxis(x_range_name="foo", y_range_name="foo", axis_label="red circles")
ax2.axis_label_text_color = red
p.add_layout(ax2, 'left')

ax3 = LinearAxis(x_range_name="foo", y_range_name="foo", axis_label="red circles")
ax3.axis_label_text_color = red
p.add_layout(ax3, 'below')

show(p)
