from sketchpy import canvas
obj = canvas.sketch_from_image('./img.jpg')
obj.draw(threshold=127)
