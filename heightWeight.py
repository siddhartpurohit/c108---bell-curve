import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv("data.csv")
#fig = ff.create_distplot([df["Height"].tolist() ],["HeightOfStudents"],show_hist = False )
fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["WeightOfStudents"],show_hist = False)
fig.show()
