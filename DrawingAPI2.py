from DrawingAPI import DrawingAPI

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return "API2.circle at {0}:{1} - radius: {2}".format(x, y, radius)
