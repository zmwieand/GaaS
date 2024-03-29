import os
import subprocess

class Graphviz():
    """
    Class to wrap graphviz png generation.
    """

    def generate_png(dot_file):
        """
        Fuction to generate a png from an input graphviz dot file.

        Returns the output png filepath.
        Raises an GraphvizRenderException if there is a problem rendering the
        png.
        """
        png = dot_file.split('.')[0] + ".png"
        cmd = ["dot", "-Tpng", dot_file, "-o", png]
        proc = subprocess.Popen(cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

        returncode = proc.wait()
        if returncode != 0:
            os.remove(dot_file)
            raise GraphvizRenderException()

        return png

class GraphvizRenderException(Exception):
    pass
