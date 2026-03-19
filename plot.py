import pandas as pd

url = "https://storage.googleapis.com/covid19-open-data/v3/epidemiology.csv"
df = pd.read_csv(url)
df_us = df[df["location_key"] == "US"]
df_us = df_us[["date", "new_confirmed"]]
df_us = df_us.sort_values("date")

df_us = df_us.dropna()
df_us["new_confirmed"] = df_us["new_confirmed"].clip(lower=0)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,4))
plt.plot(pd.to_datetime(df_us["date"]), df_us["new_confirmed"])
plt.title("Daily COVID Cases (US)")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.savefig("time_series.png", dpi=300, bbox_inches="tight")
plt.show()

# diffrencing
df_us["diff"] = df_us["new_confirmed"].diff()
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(df_us["diff"].dropna())
plt.savefig("acf.png", dpi=300, bbox_inches="tight")
plt.show()

plot_pacf(df_us["diff"].dropna())
plt.savefig("pacf.png", dpi=300, bbox_inches="tight")
plt.show()