#include <iostream>
#include <cstdlib>
#include <cmath>
#include "q4.h"


int q4() {
    double a;
    double b;
    double c;
    double r1;
    double r2;
    double *a_ptr = &a;
    double *b_ptr = &b;
    double *c_ptr = &c;
    double *r1_ptr = &r1;
    double *r2_ptr = &r2;
    getCoefficients(a_ptr, b_ptr, c_ptr);
    solveQuadratic(a_ptr, b_ptr, c_ptr, r1_ptr, r2_ptr);
    printRoots(r1_ptr, r2_ptr);
    return 0;
}

void getCoefficients(double *a, double *b, double *c) {
    std::cout << "Enter coefficients for the quadratic equation:" << std::endl;
    std::cout << "a: ";
    std::cin >> *a;
    std::cout << "b: ";
    std::cin >> *b;
    std::cout << "c: ";
    std::cin >> *c;
}

void solveQuadratic(double *a, double *b, double *c, double *x1, double *x2) {
    if (*a==0) error("The coefficient a must be non zero.");
    double disc = *b * *b - 4 * *a * *c;
    if (disc < 0) error("This equation has no real roots.");
    double sqrtDisc = sqrt(disc);
    *x1 = (-*b + sqrtDisc) / (2 * *a);
    *x2 = (-*b - sqrtDisc) / (2 * *a);
}

void printRoots(double *x1, double *x2) {
    if (*x1 == *x2) {
        std::cout << "The roots are " << *x1 << " and " << *x2 << std::endl;
    } else {
        std::cout << "The roots are " << *x1 << " and " << *x2 << std::endl;
    }
}

void error(std::string msg) {
    std::cerr << msg << std::endl;
    exit(EXIT_FAILURE);
}
