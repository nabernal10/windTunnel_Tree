import matplotlib.pyplot as plt

# Path to your data file
data_file = "postProcessing/volField_volAverage/0/volFieldValue.dat"

# Read and clean the data
with open(data_file, "r") as f:
    lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Remove parentheses and convert strings to floats
data = []
for line in lines:
    line = line.replace("(", "").replace(")", "")
    values = list(map(float, line.split()))
    data.append(values)

# Separate each column
time     = [row[0] for row in data]
Ux       = [row[1] for row in data]
Uy       = [row[2] for row in data]
Uz       = [row[3] for row in data]
k        = [row[4] for row in data]
epsilon  = [row[5] for row in data]
T        = [row[6] for row in data]
TLeaf    = [row[7] for row in data]
specHum  = [row[8] for row in data]
p        = [row[9] for row in data]

# Define line styles and colors
styles = {
    "Ux":       ("-", "#1f77b4"),
    "Uy":       ("--", "#ff7f0e"),
    "Uz":       (":", "#2ca02c"),
    "k":        ("-.", "#d62728"),
    "epsilon":  ("-", "#9467bd"),
    "T":        ("--", "#8c564b"),
    "TLeaf":    (":", "#e377c2"),
    "specHum":  ("-.", "#7f7f7f"),
    "p":        ("-", "#bcbd22")
}

# Plot
plt.figure(figsize=(10, 6))

# Variables to plot
plt.plot(time, Ux,       styles["Ux"][0], color=styles["Ux"][1], label="Ux")
plt.plot(time, Uy,       styles["Uy"][0], color=styles["Uy"][1], label="Uy")
plt.plot(time, Uz,       styles["Uz"][0], color=styles["Uz"][1], label="Uz")
plt.plot(time, k,        styles["k"][0], color=styles["k"][1], label="k")
plt.plot(time, epsilon,  styles["epsilon"][0], color=styles["epsilon"][1], label="epsilon")
plt.plot(time, T,        styles["T"][0], color=styles["T"][1], label="T")
plt.plot(time, TLeaf,    styles["TLeaf"][0], color=styles["TLeaf"][1], label="TLeaf")
plt.plot(time, specHum,  styles["specHum"][0], color=styles["specHum"][1], label="specHum")
plt.plot(time, p,        styles["p"][0], color=styles["p"][1], label="p")

# Styling
plt.xlabel("Time step", fontsize=12)
plt.ylabel("Volume-averaged value", fontsize=12)
plt.title("Selected volume-averaged fields over time", fontsize=14, fontweight="bold")
plt.yscale("log")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()