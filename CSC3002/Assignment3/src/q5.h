#ifndef _q5_h
#define _q5_h

//#include "graph.h"
#include "graph.h"
#include <set>

//template <typename NodeType, typename ArcType>
//bool isBipartite(Graph<NodeType, ArcType> &g);

//template <typename NodeType, typename ArcType>
//void visitUsingDFS(NodeType *node, Set<NodeType *> & visited, Set<NodeType *> & partitionSet[2]);

template <typename NodeType, typename ArcType>
void visitUsingDFS(Graph<NodeType, ArcType> & g, bool & flag, NodeType * node,  const int partition, Set<NodeType *> & visited, Set<NodeType *> * partitionSet) {
    if (!flag) return ;
    if (partitionSet[partition].contains(node)) {
        flag = false;
    } else {
        if (visited.contains(node)) return;
        partitionSet[1-partition].add(node);
    }
    visited.add(node);
    for (NodeType *tempNode : g.getNeighbors(node)) {
        visitUsingDFS(g, flag, tempNode, 1-partition, visited, partitionSet);
    }
}




//template <NodeType, ArcType>
template <typename NodeType, typename ArcType>
bool isBipartite(Graph<NodeType, ArcType> &g) {
    Set<NodeType *> partitionSet[2];
    Set<NodeType *> visited;
    bool flag = true;
    visitUsingDFS(g, flag, *(g.getNodeSet().begin()), 1, visited, partitionSet);
    return flag;
}

void q5();



//template <typename NodeType, typename ArcType>
//void depthFirstSearch(NodeType *node) {
//    visitUsingDFS(1, 
//}

//template <NodeType, ArcType>


#endif
