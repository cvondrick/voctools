import os
import xml.etree.ElementTree

def changefolder(path, to):
    for anno in os.listdir("{0}/Annotations".format(path)):
        if anno.endswith(".swp") or anno.startswith("."):
            print "Skipping {0}".format(anno)
            continue
        print "Processing {0}".format(anno)
        file = "{0}/Annotations/{1}".format(path, anno)
        tree = xml.etree.ElementTree.parse("{0}/Annotations/{1}".format(path, anno))
        root = tree.getroot()
        root.find("folder").text = to;
        open(file,"w").write(xml.etree.ElementTree.tostring(root))

if __name__ == "__main__":
    import sys
    changefolder(sys.argv[1], sys.argv[2])
