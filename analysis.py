# 23f2003790@ds.study.iitm.ac.in

# %% [markdown]
# # Interactive Data Analysis Notebook
# 
# Demonstrates variable dependencies, interactive sliders, and dynamic Markdown updates.

# %% [code]
import numpy as np
import marimo as mo  # Marimo environment

# Dataset
x = np.linspace(0, 10, 200)  # independent variable
y = 2 * x + 5 + np.random.normal(0, 2, size=x.shape)  # dependent variable

# %% [code]
# Cell 1: Linear relationship slider
slope_slider = mo.ui.slider(0, 5, value=2, description="Slope")
intercept_slider = mo.ui.slider(-10, 10, value=5, description="Intercept")

def update_linear():
    y_new = slope_slider.value * x + intercept_slider.value
    mo.md(f"**Slope:** {slope_slider.value}, **Intercept:** {intercept_slider.value}\n\n"
          f"Sample y_new[0]: {y_new[0]:.2f} {'🟢'*int(slope_slider.value)}")

slope_slider.on_change(update_linear)
intercept_slider.on_change(update_linear)

update_linear()  # initial display

# %% [code]
# Cell 2: Quadratic dependency slider
quad_slider = mo.ui.slider(0, 2, value=1, step=0.05, description="Quad Slope")

def update_quadratic():
    z = quad_slider.value * x**2
    mo.md(f"**Quadratic z = slope * x^2**\nSample z[0]: {z[0]:.2f} {'🔵'*int(quad_slider.value*5)}")

quad_slider.on_change(update_quadratic)
update_quadratic()  # initial display
