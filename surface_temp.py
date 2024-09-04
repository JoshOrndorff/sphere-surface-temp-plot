# inspired by https://plotly.com/python/3d-surface-plots/

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# The original example used a ring cyclide. We just need a simple sphere.
# https://math.stackexchange.com/questions/150937/derive-parametric-equations-for-sphere
import numpy as np
u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
x = (np.cos(u) * np.sin(v))
y = (np.sin(u) * np.sin(v))
z = np.cos(v)

# TODO, is making subplots necessary? Does it really matter for this one off figure?
fig = make_subplots(rows=1, cols=1,
                    specs=[[{'is_3d': True}]],
                    # subplot_titles=['Color corresponds to z'],
                    )

fig.add_trace(go.Surface(x=x, y=y, z=z, surfacecolor=10 * x * y * y * z), 1, 1)
fig.update_layout(title_text="$T = 10xy^2z$")
fig.show()