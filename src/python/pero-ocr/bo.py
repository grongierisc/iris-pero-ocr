from grongier.pex import BusinessOperation

import os

class SaveFile(BusinessOperation):
    def on_init(self):
        if hasattr(self,'path'):
            os.chdir(self.path)
        

    def save_file(self, request):
        """
        Write the content of the request in a file
        """
        filename = request.filename
        content = request.content

        with open(filename, "w") as outfile:
            outfile.write(content)