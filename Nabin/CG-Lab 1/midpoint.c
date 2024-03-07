#include <stdio.h>
#include <graphics.h>

void drawCircle(int radius) {
    int x = 0, y = radius;
    int p = 1 - radius;

    // Initialize graphics system
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);

    // Plot initial point
    putpixel(x, y, WHITE);

    while (x < y) {
        x++;
        if (p < 0)
            p += 2 * x + 1;
        else {
            y--;
            p += 2 * (x - y) + 1;
        }
        // Plot points in all octants
        putpixel(x, y, WHITE);
        putpixel(-x, y, WHITE);
        putpixel(x, -y, WHITE);
        putpixel(-x, -y, WHITE);
        putpixel(y, x, WHITE);
        putpixel(-y, x, WHITE);
        putpixel(y, -x, WHITE);
        putpixel(-y, -x, WHITE);
    }

    delay(5000); // Delay to display the circle
    closegraph(); // Close graphics system
}

int main() {
    int radius = 100; // Change the radius as needed
    drawCircle(radius);
    return 0;
}