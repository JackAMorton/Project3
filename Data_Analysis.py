import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_excel (r"C:\Users\Jack Morton\Documents\WorldBank Data.xlsx",sheet_name = "Collated Data")

df.rename(columns = {
    "Tax Revenue (% of GDP)":"Tax_Revenue",
    "Use of IMF credit (DOD, current US$)" : "IMF_Credit",
    "GDP per capita (current US$)": "Per_Capita"
},
inplace = True)


IMF_country = df.groupby("Country").IMF_Credit.sum()
IMF_country_top = df.groupby("Country").IMF_Credit.sum().sort_values(ascending= False).head()
# print("The top five countries are:""\n","\n",IMF_country_top)
#print("\n","Countries by IMF credit used","\n","\n", (IMF_country.sort_values(ascending=False)))

IMF_year = (df.groupby("Year").IMF_Credit.sum())
# print("\n","Years with highest used of IMF Credit","\n","\n",(IMF_year.sort_values(ascending=False)))

# print(df.groupby("Country").IMF_Credit.sum())

Capita_Country = df.groupby("Country").Per_Capita.sum()
# print("\n","Countries by Per Capita Income","\n","\n",(Capita_Country.sort_values(ascending=False)))

year_x = list(range(2000,2019))

# ax = plt.subplot()
# plt.plot(
#     year_x,
#     IMF_year,
#     color = "Red")
# ax.set_xticks(year_x)
# plt.xlabel("Year")
# plt.ylabel("IMF Credit used in Billions $")
# plt.title("IMF Credit used by year")
# plt.show()

country_list = df.Country.unique()
ax = plt.subplot()
plt.barh(
    country_list,
    IMF_country,
    color = "Red")
plt.ylabel("Country")
plt.xlabel("IMF Credit Used in Billions $")
plt.title("IMF Credit used by Country")
plt.show()
