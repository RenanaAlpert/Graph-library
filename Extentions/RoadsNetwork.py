from Graph.MST import *
import pandas as pd


def minimum_cost(g, city):
    mst = prim(g, city)
    return mst


def dataFrame_to_graph(df):
    g = UndirectedGraph()
    for col in df.columns:
        for row in df.index:
            if df.loc[row, col]:
                g.add_edge(row, col, df.loc[row, col])
    return g


def cities_and_roads_cost():
    file_name = "cities.csv"
    # input("Enter the name of the file (need to be csv file) that contain the list of the cities "
    # "and the cost of roads between each two of them: ")
    df = pd.read_csv(file_name)
    name_cities = df.columns.values[0]
    df = df.set_axis(df[name_cities], axis=0).drop([name_cities], axis=1)
    return df


if __name__ == '__main__':
    map_cities = cities_and_roads_cost()
    print(map_cities)
    graph_roads = dataFrame_to_graph(map_cities)
    center_city = 'Jerusalem'  # input("Enter the city that is center: ")
    min_roads_network = minimum_cost(graph_roads, center_city)
    print(min_roads_network)
