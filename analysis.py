# 23f2003790@ds.study.iitm.ac.in

# %% [markdown]
# # Interactive Data Analysis Notebook
# 
# This notebook demonstrates variable dependencies, interactive widgets, and dynamic markdown updates.
# All code cells are documented with comments for data flow.

# %% [code]
import numpy as np
from ipywidgets import FloatSlider, interact
from IPython.display import display, Markdown

# Dataset setup
x = np.linspace(0, 10, 200)  # independent variable
y = 2 * x + 5 + np.random.normal(0, 2, size=x.shape)  # dependent variable
# y depends on x and some random noise

# %% [markdown]
# ## Cell 1: Linear relationship
# y depends on x and some random noise.
# This cell sets up the base data.

# %% [code]
def update_linear(slope=2.0, intercept=5.0):
    """
    Update linear dependent variable y_new and display dynamic markdown
    """
    y_new = slope * x + intercept  # dependent variable
    md = f"**Slope:** {slope:.1f}, **Intercept:** {intercept:.1f}\n\n"
    md += f"Sample prediction y_new[0]: {y_new[0]:.2f}"
    display(Markdown(md))

# Interactive sliders for linear relationship
interact(update_linear,
         slope=FloatSlider(min=0, max=5, step=0.1, value=2.0, description='Slope'),
         intercept=FloatSlider(min=-10, max=10, step=0.5, value=5.0, description='Intercept'));

# %% [markdown]
# ## Cell 2: Quadratic dependency
# Demonstrates another dependent variable that relies on the first slider’s slope.

# %% [code]
def update_quadratic(slope=2.0):
    """
    Quadratic dependent variable: z = slope * x^2
    """
    z = slope * x**2
    md = f"**Quadratic dependency z = slope * x^2**\n"
    md += f"Sample z[0]: {z[0]:.2f}"
    display(Markdown(md))

# Interactive slider for quadratic dependency
interact(update_quadratic,
         slope=FloatSlider(min=0, max=2, step=0.05, value=1.0, description='Slope'));
