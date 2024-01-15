from Graph.Graph import DirectedGraph
from Graph.Flow import *
import pandas as pd


def create_flow_net(df):
    g = DirectedGraph()
    for col in df.columns:
        for row in df.index:
            if df.loc[row, col]:
                g.add_edge(row, col, df.loc[row, col])
    g.add_node('s')
    g.add_node('t')
    for col in df.columns:
        g.add_edge(col, 't', 1)
    for row in df.index:
        g.add_edge('s', row, 1)
    return g


def create_dataframe():
    file_name = "girls_boys.csv"
    df = pd.read_csv(file_name, header=None)
    df = df.rename(columns={x: 'b_' + str(x) for x in df.columns}, index={x: 'g_' + str(x) for x in df.index})
    return df


def matching(flow_net: DirectedGraph) -> set[tuple]:
    couples = set()
    for girl in flow_net.get_nodes(0):
        if girl == 's':
            continue
        for boy, weight in flow_net.get_adjacency_list(girl).items():
            if boy == 't':
                continue
            if weight['f'] == 1:
                couples.add((girl, boy))
    return couples


if __name__ == '__main__':
    df = create_dataframe()
    # print(df)
    flow_graph = create_flow_net(df)
    flow, flow_net = ford_fulkerson(flow_graph, 's', 't')
    print(flow)
    print(matching(flow_net))

