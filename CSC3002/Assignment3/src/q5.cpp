#include "graph.h"
#include "set.h"
#include "q5.h"



//template <NodeType, ArcType>
template <typename NodeType, typename ArcType>
bool isBipartite(Graph<NodeType, ArcType> &g) {
    Set<NodeType *> partitionSet[2];
    Set<NodeType *> visited;
    bool flag = true;
    visitUsingDFS(flag, g.getNodeSet(), 1, visited, partitionSet);
    return flag;

//void depthFirstSearch(Node *node) {
//    Set<Node *>
}

//template <NodeType, ArcType>
template <typename NodeType, typename ArcType>
void visitUsingDFS(bool &flag, NodeType *node, const int partition, Set<NodeType *> & visited, Set<NodeType *> & partitionSet[2]) {
    if (!flag || visited.contains(node)) return ;
    if (partitionSet[partition].contains(node)) {
        flag = false;
    } else {
        partitionSet[1-partition].add(node);
    }
    visited.add(node);
    for (ArcType *arc : node->arcs) {
        visitUsingDFS(flag, arc->finish, 1-partition, visited, partitionSet);
    }
}

void q5() {
    Graph<int, int> testGraph;
    testGraph.addNode(1);
    testGraph.addNode(2);
    testGraph.addNode(3);
    testGraph.addNode(4);
    testGraph.addNode(5);
    testGraph.addNode(6);
    testGraph.addNode(7);
    testGraph.addNode(8);
    testGraph.addNode(9);
    testGraph.addArc(1,2);
    testGraph.addArc(2,1);
    testGraph.addArc(1,3);
    testGraph.addArc(3,1);
    testGraph.addArc(4,2);
    testGraph.addArc(2,4);
    testGraph.addArc(4,3);
    std::cout << "Is a bipartite a bipartite? " << isBipartite(testGraph) << std::endl;
    testGraph.addArc(1,4);
    std::cout << "Is a none-bipartite a bipartite? " << isBipartite(testGraph) << std::endl;

}
