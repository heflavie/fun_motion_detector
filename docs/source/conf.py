# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../'))  # Ajoute le dossier racine de votre projet

# -- Project information -----------------------------------------------------
project = 'Fun Motion Detector'
copyright = '2024, Flavie Hebral'
author = 'Flavie Hebral'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # Pour générer la documentation automatique
    'sphinx.ext.napoleon',  # Pour supporter les docstrings au format Google ou NumPy
]

# Liste des chemins pour les templates, s'il y en a
templates_path = ['_templates']

# Liste des fichiers et dossiers à ignorer
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'

# Si vous avez des fichiers statiques comme des CSS ou des images
html_static_path = ['_static']

# -- Autodoc configuration --------------------------------------------------
# Ajoutez motion_detector.py et test_motion_detection.py dans le chemin d'importation
autodoc_mock_imports = []  # Si vous avez des dépendances manquantes, vous pouvez les ajouter ici

# -- Documentation à générer -------------------------------------------------
# C'est ici que vous allez mentionner les fichiers sources comme index.rst
# Vous pouvez maintenant ajouter les modules et leurs docstrings via Sphinx

# Documentation à partir de fichiers Python
autodoc_default_options = {
    'members': True,  # Inclut les membres (fonctions, classes) dans la documentation
    'undoc-members': True,  # Inclut les membres non documentés
    'show-inheritance': True,  # Affiche les héritages dans les classes
}

# -- Paths to the Python modules ------------------------------------------
# Si votre fichier motion_detector.py est dans le dossier racine, vous avez déjà fait la bonne chose avec sys.path.insert
# Si vous avez des fichiers Python dans un sous-dossier, ajustez le chemin en conséquence.

