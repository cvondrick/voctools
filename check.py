import os
import xml.etree.ElementTree

def removesmallboxes(path, thresh):
    for anno in os.listdir("{0}/Annotations".format(path)):
        if anno.endswith(".swp") or anno.startswith("."):
            print "Skipping {0}".format(anno)
            continue
        file = "{0}/Annotations/{1}".format(path, anno)
        tree = xml.etree.ElementTree.parse(file)
        root = tree.getroot()

        count = 0
        kept = 0
        for obj in root.iter("object"):
            box = obj.find("bndbox")
            xmax = int(box.find("xmax").text)
            ymax = int(box.find("ymax").text)
            xmin = int(box.find("xmin").text)
            ymin = int(box.find("ymin").text)

            if xmin < 0 or xmax < 0 or ymin < 0 or ymax < 0:
                print "File: {0}".format(file)
                print "Box has has negative coordinates."
                return
            if xmax <= xmin or ymax <= ymin:
                print "File: {0}".format(file)
                print "Box mins are greater than or equal to the maxs."
                return

        open(file,"w").write(xml.etree.ElementTree.tostring(root))
    print "All OK."

if __name__ == "__main__":
    import sys
    removesmallboxes(sys.argv[1], 10)
