using namespace Foam;

pointField getVertices2D(scalar xMax,scalar xMin,scalar yMax,scalar yMin)
{
    // By setting Z thickness to 1, the influence of Z is
    // eliminated from cell volume calculations
    scalar zThick = 1; 

    scalar zOff = zThick/2; // Offset of Z from the 0 plane

    pointField points(4);
    points[0] = point(xMin,yMin, -zOff);
    points[1] = point(xMax,yMin, -zOff);
    points[2] = point(xMax,yMax, -zOff);
    points[3] = point(xMin,yMax, -zOff);

    // Duplicate z points
    label sz = points.size();
    points.setSize(2*sz);
    for (label i = 0; i < sz; i++)
    {
        const point& pt = points[i];
        points[i+sz] = point(pt.x(), pt.y(), -pt.z());
    }

    return points;
}
