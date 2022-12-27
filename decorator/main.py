class Image:
    def __init__(self, image) -> None:
        self.image = image

    def render_image(self):
        return self.image


class Sketch:
    def __init__(self, image_obj) -> None:
        self.wrapped_image_obj = image_obj

    def render_image(self):
        return f"<sketch>{self.wrapped_image_obj.render_image()}</sketch>"

class WaterColor:

    def __init__(self, image_obj) -> None:
        self.wrapped_image_obj = image_obj

    def render_image(self):
        return f"<watercolor>{self.wrapped_image_obj.render_image()}</watercolor>"


if __name__ == "__main__":

    image = Image("Some Image")
    print(image.render_image())

    image = Sketch(image)
    print(image.render_image())

    image = WaterColor(image)
    print(image.render_image())

"""
output:
    Some Image
    <sketch>Some Image</sketch>
    <watercolor><sketch>Some Image</sketch></watercolor>
"""