from grongier.pex import BusinessOperation

from msg import SaveFileRequest

import os

class SaveFile(BusinessOperation):
    """
    This method is called by the BusinessService when a message is received.
    """
    def on_init(self):
        """
        This method is called when the BusinessOperation is initialized.
        """
        if hasattr(self,'path'):
            os.chdir(self.path)
        

    def save_file(self, request: SaveFileRequest):
        """
        Create a new file with the content of the request
        """
        filename = request.filename
        content = request.content

        # Create a new file with the content of the request
        with open(filename, 'w',encoding='utf-8') as f:
            f.write(content)
