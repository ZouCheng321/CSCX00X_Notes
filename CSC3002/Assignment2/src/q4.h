#include <iostream>
#include <cstdlib>
#include <cmath>

void getCoefficients(double *a, double *b, double *c);
void solveQuadratic(double *a, double *b, double *c,
                    double *x1, double * x2);
void printRoots(double *x1, double *x2);
void error(std::string msg);
int q4();
