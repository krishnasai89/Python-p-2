from sketchpy import canvas
obj = canvas.sketch_from_image('./img.png')
obj.draw(threshold=127)
