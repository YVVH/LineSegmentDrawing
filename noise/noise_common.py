class MixedNoise:
    def __init__(self, center, fig, text):
        self.center = center
        self.text = text
        self.fig = fig

    def draw(self, image, thickness):
        self.fig.draw(image, (0, 0, 0), thickness=thickness)
        img = self.text.draw(image, (0, 0, 0))

        return img
