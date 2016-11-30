import cv2
import numpy as np

import util
def get_mask():
    mask = util.img.black((100, 100))
        # the region
    util.img.circle(mask, (50, 50), 40, 1, -1)
    util.img.rectangle(mask, (60, 15), (90, 40), 0, -1)
    
    # hole 1    
    util.img.rectangle(mask, (30, 30), (50, 50), 0, -1)
    util.img.circle(mask, (30, 30), 10, 0, -1)
    
    return mask
    
def show_mask(m, path = None):
    m = m.copy()
    h, w = util.img.get_shape(m)
    for x in xrange(w):
        for y in xrange(h):
            if m[y][x] != 0:
                m[y][x] = 255
                
    util.img.imshow('Image', m)
    if path:
        util.img.imwrite(path, m)
    
m = get_mask()
show_mask(m, path = './Origin.png')
contours, _ = cv2.findContours(m.copy(), mode = cv2.RETR_CCOMP, method = cv2.CHAIN_APPROX_NONE)
vis_contours = util.img.black(m)
cv2.drawContours(vis_contours, contours, 0, 255, 1 ) # show all contours
show_mask(vis_contours, path = './Contours.png')

cnt_to_be_shown =  contours[1]
x,y,w,h = cv2.boundingRect(cnt_to_be_shown)
vis_bbox = util.img.black(m)
util.img.rectangle(vis_bbox,(x,y),(x+w,y+h), 255, 1)
show_mask(vis_bbox, path = './Bbox1.png')

vis_bbox = util.img.black(m)
rect = cv2.minAreaRect(cnt_to_be_shown)
box = cv2.cv.BoxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(vis_bbox,[box],0,(0,0,255),2)
show_mask(vis_bbox, path = './Bbox1.png')

