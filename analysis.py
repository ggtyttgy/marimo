# Author: 23f2003790@ds.study.iitm.ac.in

import marimo
import numpy as np
import matplotlib.pyplot as plt

# --- Cell 1: Generate synthetic data ---
# This cell defines the dataset (X, Y) for analysis.
X = np.linspace(0, 10, 100)
Y = 3 * X + np.random.normal(0, 2, size=X.shape)

# --- Cell 2: Slider widget for slope ---
# The value of 'slope' from this cell will modify subsequent analysis.
slope = marimo.slider(label="Regression Slope", min=0.0, max=6.0, step=0.1, value=3.0)

# --- Cell 3: Compute predictions based on slider ---
# This cell depends on 'X' (from Cell 1) and 'slope' (from Cell 2).
Y_pred = slope.value * X

# --- Cell 4: Visualize and document ---
# This cell displays the results and updates the markdown dynamically.
fig, ax = plt.subplots()
ax.scatter(X, Y, label="Observed Data")
ax.plot(X, Y_pred, color="red", label=f"Model (slope={slope.value})")
ax.legend()
plt.close(fig)

marimo.display(fig)

marimo.markdown(f"""
### Interactive Linear Relationship Demo

- **Current regression slope:** `{slope.value}`
- The red line shows the predicted relationship between X and Y based on the slope above.

*Move the slider to explore how the model fits the data!*

---
*Data and widgets are linked: Changing the slider updates the line and markdown above automatically.*
""")
