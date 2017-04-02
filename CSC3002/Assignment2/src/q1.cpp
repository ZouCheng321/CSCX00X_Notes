#include <iostream>
#include "gwindow.h"

void drawHFractal(GWindow &gw, double x, double y, double size, int order){
    const auto half = size/2;
    if(order!=0){
        gw.drawLine(x-half, y, x+half, y);
        gw.drawLine(x-half, y-half, x-half, y+half);
        gw.drawLine(x+half, y-half, x+half, y+half);
        if(order>0){
            drawHFractal(gw, x-half, y+half, size/2, order-1);
            drawHFractal(gw, x-half, y-half, size/2, order-1);
            drawHFractal(gw, x+half, y+half, size/2, order-1);
            drawHFractal(gw, x+half, y-half, size/2, order-1);
        }
    }


}
