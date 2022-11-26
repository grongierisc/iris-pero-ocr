from grongier.pex import BusinessService

import os
import configparser
import cv2
import torch
from pero_ocr.document_ocr.layout import PageLayout
from pero_ocr.document_ocr.page_parser import PageParser

from msg import SaveFileRequest

class ServiceOCR(BusinessService):

    def get_adapter_type():
        """
        Name of the registred adaptor
        """
        return "Ens.InboundAdapter"

    def on_init(self):
        if not hasattr(self,'path_in'):
            self.path_in = '/irisdev/app/misc/in/'
        if not hasattr(self,'path_out'):
            self.path_out = '/irisdev/app/misc/out/'
        if not hasattr(self,'target'):
            self.target = 'SaveFileOperation'
        # Read config file.
        if not hasattr(self,'config_path'):
            self.config_path = '/irisdev/app/misc/config_file.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

        # Init the OCR pipeline.
        self.page_parser = PageParser(self.config, torch.device("cpu"),
                    config_path=os.path.dirname(self.config_path))

    def on_process_input(self, message_input):
        """
        For each image file *.jpg, *.png, *.tif, *.tiff, *.bmp in input directory
        Parse the image by the OCR pipeline
        Create a PageLayout object
        Create a SaveFileRequest with a filename and the PageLayout object
        """ 
        for file in os.listdir(self.path_in):
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".tif") or file.endswith(".tiff") or file.endswith(".bmp"):
                # Read the document page image.
                input_image_path = self.path_in + file
                image = cv2.imread(input_image_path, 1)

                # Init empty page content.
                # This object will be updated by the ocr pipeline. id can be any string and it is used to identify the page.
                page_layout = PageLayout(id=input_image_path,
                    page_size=(image.shape[0], image.shape[1]))

                # Process the image by the OCR pipeline
                page_layout = self.page_parser.process_page(image, page_layout)

                # Create a SaveFileRequest with a filename and the PageLayout object
                filename = file + '.xml'
                content = page_layout.to_pagexml_string()
                message_output = SaveFileRequest(filename=filename, content=content)
                self.send_request_sync(self.target,message_output)

                # Create a SaveFileRequest with a filename and the PageLayout object
                filename = file + '.alto.xml'
                content = page_layout.to_altoxml_string()
                message_output = SaveFileRequest(filename=filename, content=content)
                self.send_request_sync(self.target,message_output)
                
                # move file to out directory
                os.rename(input_image_path, self.path_out + file)

if __name__ == '__main__':
    bs = ServiceOCR()
    bs.on_init()
    bs.on_process_input(None)
    print("Done")