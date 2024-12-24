# -- Path setup
import os
import sys
sys.path.insert(0, os.path.abspath('../'))

# -- Project information
project = 'Fun Motion Detector'
copyright = '2024, Flavie Hebral'
author = 'Flavie Hebral'
release = '0.1.0'

# -- General configuration
extensions = [
    # Pour générer la documentation automatique
    'sphinx.ext.autodoc',
    # Pour supporter les docstrings au format Google ou NumPy
    'sphinx.ext.napoleon',
            ]

# Liste des chemins pour les templates, s'il y en a
templates_path = ['_templates']

# Liste des fichiers et dossiers à ignorer
exclude_patterns = []

# -- Options for HTML output

html_theme = 'alabaster'

# Si vous avez des fichiers statiques comme des CSS ou des images
html_static_path = ['_static']

# -- Autodoc configuration
autodoc_mock_imports = []

# -- Documentation à générer

# Documentation à partir de fichiers Python
autodoc_default_options = {
    # Inclut les membres (fonctions, classes) dans la documentation
    'members': True,
    'undoc-members': True,  # Inclut les membres non documentés
    'show-inheritance': True,  # Affiche les héritages dans les classes
}
