from DrawingAPI import DrawingAPI

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return "API1.circle at {0}:{1} - radius: {2}".format(x, y, radius)
