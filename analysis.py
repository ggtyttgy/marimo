# 23f2003790@ds.study.iitm.ac.in
import marimo as mo
import numpy as np

# Independent variable
x = np.linspace(0, 10, 200)

# --- Cell 1: interactive slider ---
slope = mo.ui.slider(0, 5, value=2, description="Slope")

# Return the slider so it appears
slope

# --- Cell 2: dependent variable using slope ---
y = slope.value * x + 5

# Dynamic Markdown output depending on slider state
mo.md(f"""
### Linear Model
**Equation:** y = {slope.value} * x + 5  

First value of y: {y[0]:.2f}  

{"🟢" * slope.value}
""")
