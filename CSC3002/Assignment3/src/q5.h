#ifndef _q5_h
#define _q5_h

#include "graph.h"
//#include "graph.h"

template <typename NodeType, typename ArcType>
bool isBipartite(Graph<NodeType, ArcType> &g);

template <typename NodeType, typename ArcType>
void visitUsingDFS(NodeType *node, Set<NodeType *> & visited, Set<NodeType *> & partitionSet[2]);

void q5();


#endif
