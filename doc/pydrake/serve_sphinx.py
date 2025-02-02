"""
Serves documentation for `pydrake`.
"""

from os.path import abspath, dirname, join

from drake.doc.pydrake.sphinx_base import preview_main

if __name__ == "__main__":
    gen_script = join(dirname(abspath(__file__)), "gen_sphinx")
    preview_main(gen_script=gen_script, default_port=8001)
