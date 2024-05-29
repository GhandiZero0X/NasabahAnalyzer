# ImageTree.py
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

def show_tree_image(clf, feature_names, class_names):
    plt.figure(figsize=(15,3))
    plot_tree(clf, filled=True, feature_names=feature_names, class_names=class_names)
    plt.show()
