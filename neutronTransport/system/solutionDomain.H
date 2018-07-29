using namespace Foam;

scalar tau = constant::mathematical::twoPi;

scalar xMax = tau/2;
scalar xMin = 0;
scalar yMax = tau/2;
scalar yMin = 0;

pointField getVertices(scalar xMax,scalar xMin,scalar yMax,scalar yMin)
{

    pointField points(4);
    points[0]  = point(xMin,yMin, -0.1);
    points[1]  = point(xMax,yMin, -0.1);
    points[2]  = point(xMax,yMax, -0.1);
    points[3]  = point(xMin,yMax, -0.1);

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
