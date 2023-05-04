import os
import xml.etree.ElementTree as ET

# Set the path to the directory containing the XML files
xml_dir_path = "/home/faster_rcnn/tools/datasets/VOC2012/Annotations"

# Traverse each XML file in the directory
for xml_file_name in os.listdir(xml_dir_path):
    if xml_file_name.endswith(".xml"):
        # Parse the XML file
        xml_file_path = os.path.join(xml_dir_path, xml_file_name)
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Find the "filename" parameter
        filename_elem = root.find("filename")
        if filename_elem is not None:
            # Set the value of the "filename" parameter to the file name
            filename_elem.text = xml_file_name.replace(".xml", ".jpg")

        # Save the modified XML file
        tree.write(xml_file_path)

