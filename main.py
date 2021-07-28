import plotly.express as px

india = px.data.gapminder().query("country=='India'")
print(india)

fig = px.bar(india, x='year', y='pop')
fig.show()