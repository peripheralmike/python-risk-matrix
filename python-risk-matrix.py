import matplotlib.pyplot as plt

# Define risks with their impact and probability ratings
risks = {
    "Risk A": {"Impact": 5, "Probability": 4},
    "Risk B": {"Impact": 3, "Probability": 3},
    "Risk C": {"Impact": 5, "Probability": 3},
    "Risk D": {"Impact": 4, "Probability": 2},
    "Risk E": {"Impact": 3, "Probability": 2}
}

# Define unique icons for each risk
icons = {
    "Risk A": "X",  # Cross for high severity
    "Risk B": "o",  # Circle for medium severity
    "Risk C": "P",  # Plus for high severity
    "Risk D": "D",  # Diamond for medium severity
    "Risk E": "*"   # Star for medium severity
}

# Creating the risk matrix plot
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_xlabel('Probability')
ax.set_ylabel('Impact')
ax.set_title('Risk Matrix Visualization')

# Apply background colors for severity levels
ax.fill_between([0, 5], [0, 0], [2, 2], color='green', alpha=0.3, label='Low Severity')
ax.fill_between([0, 5], [2, 2], [4, 4], color='yellow', alpha=0.3, label='Medium Severity')
ax.fill_between([0, 5], [4, 4], [5, 5], color='red', alpha=0.3, label='High Severity')

# Plot each risk with a unique icon
for risk, values in risks.items():
    ax.scatter(values["Probability"], values["Impact"], label=risk, s=200, marker=icons[risk], edgecolors='k')

ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Risks")

plt.tight_layout()
plt.show()
