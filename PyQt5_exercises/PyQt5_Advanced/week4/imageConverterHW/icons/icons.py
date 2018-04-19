from PyQt5.QtGui import QIcon
import os
root = os.path.dirname(__file__)


icons = dict(
    notImage = os.path.join(root, 'notImage.png'),
    folder = os.path.join(root, 'folder.png'),
    image = os.path.join(root, 'image.png'),
    main = os.path.join(root, 'main.png')
)
