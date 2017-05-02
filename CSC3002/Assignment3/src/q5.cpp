#include <string>
#include "graph.h"
#include "set.h"
#include "q5.h"

class IntNode;
class IntArc;


class IntNode {

public:
//   string getName() {
//      return name;
//   }

   void setCode(int tempCode) {
       code = tempCode;
   }

private:
   std::string name;
   Set<IntArc *> arcs;
   int code;
//   string airportCode;
   friend class Graph<IntNode, IntArc>;
};

class IntArc {

public:
   IntNode *getStart() {
      return start;
   }

   IntNode *getFinish() {
      return finish;
   }

//   int getDistance() {
//      return distance;
//   }

//   void setDistance(int miles) {
//      distance = miles;
//   }

private:
   IntNode *start;
   IntNode *finish;
//   int distance;
   friend class Graph<IntNode,IntArc>;
};

//Graph<IntNode, IntArc> testGraph;

void q5() {
    Graph<IntNode, IntArc> testGraph;
    IntNode * node1 = testGraph.addNode("node1");
    IntNode * node2 = testGraph.addNode("node2");
    IntNode * node3 = testGraph.addNode("node3");
    IntNode * node4 = testGraph.addNode("node4");
    node1->setCode(1);
    node2->setCode(2);
    node3->setCode(3);
    node4->setCode(4);
    testGraph.addArc(node1,node2);
    testGraph.addArc(node2,node1);
    testGraph.addArc(node1,node3);
    testGraph.addArc(node3,node1);
    testGraph.addArc(node4,node2);
    testGraph.addArc(node2,node4);
    testGraph.addArc(node4,node3);
    std::cout << "Is a bipartite a bipartite? " << isBipartite(testGraph) << std::endl;
    testGraph.addArc(node1,node4);
    std::cout << "Is a none-bipartite a bipartite? " << isBipartite(testGraph) << std::endl;

}
