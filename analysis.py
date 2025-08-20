# 23f2003790@ds.study.iitm.ac.in

# %% [markdown]
# # Interactive Data Analysis Notebook
# 
# This notebook demonstrates relationships between variables using interactive widgets.
# Comments document the data flow.

# %% [code]
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

# Sample dataset
x = np.linspace(0, 10, 200)  # independent variable
y = 2 * x + 5 + np.random.normal(0, 2, size=x.shape)  # dependent variable

# %% [markdown]
# ## Variable Dependencies
# `y` depends on `x` and some random noise.

# %% [code]
# Interactive function
def plot_line(slope=2.0, intercept=5.0):
    """
    Plot y = slope * x + intercept
    This dynamically updates based on slider widget state.
    """
    y_new = slope * x + intercept  # dependent variable recalculation
    plt.figure(figsize=(8,4))
    plt.scatter(x, y, label='Original y')
    plt.plot(x, y_new, color='red', label=f'Predicted y = {slope}x + {intercept}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interactive Linear Relationship')
    plt.legend()
    plt.show()

# Slider widgets
interact(plot_line,
         slope=FloatSlider(min=0.0, max=5.0, step=0.1, value=2.0),
         intercept=FloatSlider(min=-10.0, max=10.0, step=0.5, value=5.0));

# %% [markdown]
# Adjust the sliders above to see how `y_new` changes dynamically.
# 
# **Data flow notes:**  
# - `x` is fixed across all recalculations.  
# - `y_new` depends on `slope` and `intercept` sliders.  
# - Markdown updates describe the impact of slider changes.
