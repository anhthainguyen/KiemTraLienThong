from sys import argv
import networkx as nx
import numpy as np

script, option_arg, input_arg, output_arg = argv
def docTapTinMaTranKe(inputFile):
	with open(input_arg) as file:
	    list2d = [[int(digit) for digit in line.split()] for line in file]
	    if not list2d:
	    	return list2d
	    vertex_n = list2d[0][0]
	    list2d.pop(0)
	    B = np.array(list2d, dtype = np.int)
	    print('Ma tran ke:', B)
	    return B

#Tim thanh phan lien thong bang DFS
def ganNhanDFS(graph, vertexLabel, u, label):

	vertexLabel[u] = label
	for v in nx.all_neighbors(graph, u):
		print(v)
		if vertexLabel[v] == 0:
			ganNhanDFS(graph, vertexLabel, v, label)

def connectedComponentsDFS(graph):
	label = 0
	vertexLabel = np.zeros(len(graph))
	for i in range(len(graph)):
		if vertexLabel[i] == 0:
			label += 1
			ganNhanDFS(graph, vertexLabel, i, label)
	return vertexLabel

#Tim thanh phan lien thong bang BFS
def ganNhanBFS():
	pass

def connectedComponentsBFS():
	pass

def printArrayToFile(outputFile, array):
	for item in array:
		outputFile.write("%s " % item)
	outputFile.write('\n')

def sortBySize(val):
	return val.size

def putToOutput(outputFile, labeledVertex):
	connectComponentLabels = np.unique(labeledVertex)
	resultList = []
	for l in connectComponentLabels:
		resultList.append([index for index, value in enumerate(labeledVertex) if value == l])
	sortedResultList = sorted(resultList, key=lambda e: (len(e), e[0]))
	numOfConnectComponent = len(np.unique(labeledVertex))
	outputFile.write("%s\n" % numOfConnectComponent)
	for sArr in sortedResultList:
		printArrayToFile(outputFile, sArr)




maTranKe = docTapTinMaTranKe(input_arg)
if len(maTranKe) == 0:
	print('The input file is empty')
else:
	G = nx.from_numpy_matrix(maTranKe)

	nx.k_components(G)
	print(nx.k_components(G))
	print('Do thi nay lien thong?', nx.is_connected(G))

	if option_arg == 'd':
		print('Su dung DFS!!!')
		danhSachDaGanNhan = connectedComponentsDFS(G)
		output_file = open(output_arg, "wt")
		putToOutput(output_file, danhSachDaGanNhan)

	
 #Xu ly truong hop dung DFS
# print(list(nx.dfs_preorder_nodes(G, source=0)))
# print(list(nx.dfs_preorder_nodes(G, source=1)))
# print(list(nx.dfs_preorder_nodes(G, source=2)))
# print(list(nx.dfs_preorder_nodes(G, source=3)))
# print(list(nx.dfs_preorder_nodes(G, source=4)))
# print(list(nx.dfs_preorder_nodes(G, source=5)))
# print(list(nx.dfs_preorder_nodes(G, source=6)))

#  #xu ly truong hop dung BFS
# print("Dung BFS")
# print(list(nx.bfs_edges(G, source=0)))
# print(list(nx.bfs_edges(G, source=1)))
# print(list(nx.bfs_edges(G, source=2)))
# print(list(nx.bfs_edges(G, source=3)))
# print(list(nx.bfs_edges(G, source=4)))
# print(list(nx.bfs_edges(G, source=5)))
# print(list(nx.bfs_edges(G, source=6)))


