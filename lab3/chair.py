from stool import Stool


class Chair(Stool):
    def __init__(self, height, quality, heightChairBack):
        super().__init__(height, quality)
        self.heightChairBack = heightChairBack

    def wood_amount(self):
        return super().woodAmount() + 2 * self.height + 5

    def __str__(self):
        return f'Chair height is {self.height}, height of back seat is {self.heightChairBack} and quality is {self.quality}'