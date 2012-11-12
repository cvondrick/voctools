import os
import xml.etree.ElementTree

def removesmallboxes(path, thresh):
    for anno in os.listdir("{0}/Annotations".format(path)):
        if anno.endswith(".swp") or anno.startswith("."):
            print "Skipping {0}".format(anno)
            continue
        print "Processing {0}".format(anno),
        file = "{0}/Annotations/{1}".format(path, anno)
        tree = xml.etree.ElementTree.parse("{0}/Annotations/{1}".format(path, anno))
        root = tree.getroot()

        count = 0
        kept = 0
        for obj in root.iter("object"):
            box = obj.find("bndbox")
            xmax = int(box.find("xmax").text)
            ymax = int(box.find("ymax").text)
            xmin = int(box.find("xmin").text)
            ymin = int(box.find("ymin").text)

            if xmax - xmin <= thresh or ymax - ymin <= thresh:
                root.remove(obj)
                count += 1
            else:
                kept += 1
        print "\ttremoved {0}\tkept {1}".format(count, kept)

        open(file,"w").write(xml.etree.ElementTree.tostring(root))

if __name__ == "__main__":
    import sys
    removesmallboxes(sys.argv[1], 2)
