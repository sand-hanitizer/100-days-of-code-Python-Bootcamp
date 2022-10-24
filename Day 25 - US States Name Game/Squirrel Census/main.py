import pandas as pd

data = pd.read_csv("census.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {"Colors": ["Gray","Red","Black"], "Count":[gray_count,red_count,black_count]}
dataset = pd.DataFrame(data_dict)
print(dataset)

dataset.to_csv("ColorData.csv")
