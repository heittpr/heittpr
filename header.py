from manim import *

class header(Scene):
  def construct(self):
    heittpr = Text('heittpr')
    heitor = Text('heitor')
    heitor.set_y((heittpr.height-heitor.height)/2)
    heittpr.save_state()

    self.add(heittpr)
    self.wait(1.5)
    self.play(Transform(heittpr, heitor, run_time=1.5))
    self.wait(1.5)
    self.play(Restore(heittpr, run_time=1.5))
