import argparse
import networkx as nx
import optmodel as opt
import json

def readGraph(graphFile):
    return nx.read_gml(graphFile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read filenames.')
    parser.add_argument('-g', '--graph', help='the graph file', default = "../../data/SanteFe.gml")
    parser.add_argument('-p', '--params', help='the parameters file', default = "../../params/paramsFile.json")
    args = parser.parse_args()
    paramsFile = args.params
    graph = readGraph(args.graph)
    paramsDict = json.loads(open(paramsFile).read())
    optModel = opt.OptimizationModel(graph, paramsFile, paramsDict)
    optModel.solve()
    optModel.writeResults('results.txt')