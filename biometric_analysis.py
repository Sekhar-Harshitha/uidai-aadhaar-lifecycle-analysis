import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

print("Script running from:", os.getcwd())

# ==============================
# GLOBAL STYLE
# ==============================
plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "#f8f9fa",
    "axes.edgecolor": "#dddddd",
    "axes.grid": True,
    "grid.color": "#e6e6e6",
    "grid.linestyle": "--",
    "grid.alpha": 0.6,
    "font.family": "Segoe UI",
    "font.size": 11
})

# ==============================
# CORRECT PATH (FIXED)
# ==============================
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BIOMETRIC_FOLDER = os.path.join(PROJECT_ROOT, "data", "biometric")

print("Looking for files in:", BIOMETRIC_FOLDER)

files = glob.glob(os.path.join(BIOMETRIC_FOLDER, "*.csv"))

print("Files found:", files)

if not files:
    raise FileNotFoundError("No CSV files found in data/biometric folder")

# ==============================
# LOAD ALL FILES
# ==============================
df_list = []
for f in files:
    print("Loading:", f)
    df_list.append(pd.read_csv(f))

df = pd.concat(df_list, ignore_index=True)
print("Total rows loaded:", len(df))

# ==============================
# CLEAN DATA
# ==============================
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
df['state'] = df['state'].astype(str).str.title().str.strip()

# ==============================
# CREATE TOTAL UPDATES
# ==============================
df['total_bio_updates'] = (
    df['bio_age_5_17'].fillna(0) +
    df['bio_age_17_'].fillna(0)
)

# ==============================
# AGGREGATE
# ==============================
state_bio = (
    df.groupby('state')['total_bio_updates']
    .sum()
    .sort_values(ascending=False)
)

top10 = state_bio.head(10)

# ==============================
# PLOT
# ==============================
fig, ax = plt.subplots(figsize=(11, 6))

colors = plt.cm.Purples(np.linspace(0.45, 0.9, len(top10)))
bars = ax.barh(top10.index, top10.values, color=colors)
ax.invert_yaxis()

for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(False)

for bar in bars:
    w = bar.get_width()
    ax.text(
        w * 0.98,
        bar.get_y() + bar.get_height() / 2,
        f"{int(w):,}",
        va="center",
        ha="right",
        color="white",
        fontsize=10,
        fontweight="bold"
    )

ax.set_xlabel("Total Biometric Updates")
ax.set_ylabel("State")

fig.text(0.5, 0.96, "Top 10 States by Biometric Updates",
         ha="center", va="center", fontsize=16, fontweight="bold")

fig.text(0.5, 0.92, "Combined UIDAI Biometric Files",
         ha="center", va="center", fontsize=11, color="gray")

plt.subplots_adjust(top=0.88)
plt.show()

print("\nBiometric analysis completed successfully")
