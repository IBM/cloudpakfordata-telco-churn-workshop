from yaml import load, dump, Loader
from os import path
import os
import shutil


import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

from PIL import Image
from resizeimage import resizeimage


FROM=r'./'
TO=r'./'
LAB_DEFINITIONS=r'./deploy/gitbook-mapping.yml'

data = load(open(LAB_DEFINITIONS, 'r'), Loader=Loader)
labs = data[0]['labs']


# First create the treeprocessor
class ImgExtractor(Treeprocessor):
    def run(self, doc):
        "Find all images and append to markdown.images. "
        self.markdown.images = []
        for image in doc.findall('.//img'):
            self.markdown.images.append(image.get('src'))

# Then tell markdown about it
class ImgExtExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        img_ext = ImgExtractor(md)
        md.treeprocessors.add('imgext', img_ext, '>inline')

def copy_resize_image(src, dst, w_max, h_max):
    with open(src, 'r+b') as f:
        with Image.open(f) as image:
            if image.height > image.width:
                contain = resizeimage.resize_height(image, h_max)
            else:
                contain = resizeimage.resize_width(image, w_max)
                
            contain.save(dst, image.format)

def process_lab(lab):
    assert(len(lab.keys())==1)
    
    name = list(lab.keys())[0]
    contents = lab[name]
    
    for content in contents:
        src = path.join(FROM, content['from'])
        dst = path.join(TO, content['to'])

        os.makedirs(path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)

        print(path.dirname(src))
        print(dst)

        md = markdown.Markdown(extensions=[ImgExtExtension()])
        html = md.convert(open(src,'r').read())
        # print(md.images)

        dst_img_path = path.abspath(path.join(path.dirname(dst), 'images'))
        os.makedirs(dst_img_path, exist_ok=True)
        
        with open(dst,'r') as file:
            filedata = file.read()
            for i in md.images:
                src_img = path.abspath(path.join(path.dirname(src), i))
                dst_img = path.abspath(path.join(dst_img_path, path.basename(src_img)))
                # shutil.copyfile(src_img, dst_img)
                copy_resize_image(src_img, dst_img, 640,640)

                print("Copied {}".format(dst_img))
                dst_rel_image = path.relpath(dst_img, path.dirname(dst))
                filedata = filedata.replace(i,dst_rel_image)
                print("updated {} to {}".format(i, dst_rel_image))
        with open(dst,'w') as file:
            file.write(filedata)







for lab in labs:
    process_lab(lab)