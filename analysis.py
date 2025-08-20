# Email: 23f2003790@ds.study.iitm.ac.in

import marimo
import numpy as np
import matplotlib.pyplot as plt

# Cell 1: Load data and define variables
# This cell creates synthetic data and exposes X and Y for downstream cells.
X = np.linspace(0, 10, 100)
Y = 2 * X + np.random.normal(0, 2, size=X.shape)

# Cell 2: Interactive slider for slope
# The value of 'slope' is used by subsequent cells to update the regression line.
slope = marimo.slider(label="Adjust Slope", min=0.0, max=5.0, step=0.1, value=2.0)

# Cell 3: Compute predicted values based on the slider
# This cell depends on 'X' from Cell 1 and 'slope' from Cell 2.
Y_pred = slope.value * X

# Cell 4: Plot and show dynamic markdown output
# This cell visualizes the relationship and outputs markdown based on widget state.
fig, ax = plt.subplots()
ax.scatter(X, Y, label="Data")
ax.plot(X, Y_pred, color="red", label=f"Regression Line (slope={slope.value})")
ax.legend()
plt.close(fig)

marimo.display(fig)

marimo.markdown(f"""
**Current Regression Slope:** `{slope.value}`

The red line shows the predicted relationship between X and Y based on the slope chosen above.

*Move the slider to see how the regression line changes!*
""")

# Comments:
# - Cell 1 initializes data used by all other cells.
# - Cell 2 creates a slider widget that controls the slope of the regression line.
# - Cell 3 uses the slider's state to update predictions.
# - Cell 4 displays a plot and dynamic markdown, both of which depend on the current slider value.
