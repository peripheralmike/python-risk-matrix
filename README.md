# Risk Matrix Visualization Tool

This Python script offers a straightforward method to visualize risk assessments by plotting risks on a 2D matrix according to their impact (severity) and probability (likelihood) of occurrence. Utilizing matplotlib for graphing, it creates an intuitive, color-coded severity level chart for easy interpretation of different risks.

## Key Features

- **Risk Mapping**: Plots risks on a matrix based on impact and probability.
- **Unique Icons**: Differentiates risks using unique icons for quick identification.
- **Severity Levels**: Applies color-coding to visually distinguish between low, medium, and high severity levels.

## Prerequisites

To run this script, ensure you have the following installed:
- Python 3.x
- matplotlib library

## Installation

First, verify that Python 3 and pip are installed on your system. Then, install matplotlib using pip with the following command:

```bash
pip install matplotlib
```
## How to Use
Execute the script with Python to view the risk matrix:

```bash
python risk_matrix_visualization.py
```
Upon running, the script will display a risk matrix with predefined risks. These can be tailored to your specific needs by modifying the risks and icons dictionaries within the script.

## Customization Guide
To adapt the script to your scenario:

Risks: Amend the risks dictionary to include your specific risks, adjusting their impact and probability values as necessary.
Icons: Alter the icons dictionary if you wish to represent risks with different symbols.
Matrix Titles and Labels: Customize the plot title and axis labels to better fit your context.

## Visualization Example

![Diagram](Firgure_2.png "Example")

License
This project is made available under the MIT License. Feel free to use, modify, and distribute as needed with attribution.





