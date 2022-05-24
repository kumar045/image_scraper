from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os

def check_color(image,color):
    def RGB2HEX(color):
        return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

    def get_colors(image, number_of_colors, show_chart):
        
        modified_image = cv2.resize(image, (300, 300), interpolation = cv2.INTER_AREA)
        modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
        
        clf = KMeans(n_clusters = number_of_colors)
        labels = clf.fit_predict(modified_image)
        
        counts = Counter(labels)
        # sort to ensure correct color percentage
        counts = dict(sorted(counts.items()))
        
        center_colors = clf.cluster_centers_
        # We get ordered colors by iterating through the keys
        ordered_colors = [center_colors[i] for i in counts.keys()]
        hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
        rgb_colors = [ordered_colors[i] for i in counts.keys()]

        if (show_chart):
            plt.figure(figsize = (8, 6))
            plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
        
        return rgb_colors  


    def match_image_by_color(image, color, threshold = 60, number_of_colors = 10): 
        
        image_colors = get_colors(image, number_of_colors, False)
        selected_color = rgb2lab(np.uint8(np.asarray([[color]])))

        select_image = False
        for i in range(number_of_colors):
            curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
            diff = deltaE_cie76(selected_color, curr_color)
            if (diff < threshold):
                select_image = True
        
        return select_image

    def show_selected_images(images, color, threshold, colors_to_match):

            selected = match_image_by_color(images,
                                            color,
                                            threshold,)
            return selected
           



    COLORS = {
        'black': [0, 0, 120],
        'blue': [0, 0, 128],
        'yellow': [255, 255, 0]
    }          

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    selected=show_selected_images(image,  COLORS[color], 60, 5)
    print(selected)
    return selected