import joblib
from sklearn import tree
import graphviz

def create_tree_image():
    # Muat model dan LabelEncoders
    clf = joblib.load('model.pkl')
    le_prestasi = joblib.load('le_prestasi.pkl')
    le_jaminan = joblib.load('le_jaminan.pkl')
    le_pekerjaan = joblib.load('le_pekerjaan.pkl')
    le_kelas = joblib.load('le_kelas.pkl')

    # Nama fitur dan kelas
    feature_names = ['Prestasi', 'Jaminan', 'Pekerjaan']
    class_names = le_kelas.inverse_transform(range(len(le_kelas.classes_)))

    # Buat visualisasi tree
    dot_data = tree.export_graphviz(clf, out_file=None, 
                                    feature_names=feature_names,
                                    class_names=class_names,
                                    filled=True, rounded=True, 
                                    special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render("decision_tree")

if __name__ == '__main__':
    create_tree_image()
