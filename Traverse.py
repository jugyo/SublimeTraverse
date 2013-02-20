import sublime_plugin
import os
from glob import iglob

class TraverseCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        if kwargs['start'] == "root":
            self.traverse("/")
        elif kwargs['start'] == "home":
            self.traverse(os.path.expanduser("~"))
        elif kwargs['start'] == "project":
            self.traverse(self.window.folders()[0])

    def traverse(self, directory):
        filepaths = [f for f in iglob(os.path.join(directory, '*'))]
        filepaths += [f for f in iglob(os.path.join(directory, '.*'))]
        dirs_and_files = [os.path.basename(f) + "/" for f in filepaths if os.path.isdir(f)]
        dirs_and_files += [os.path.basename(f) for f in filepaths if os.path.isfile(f)]
        if directory != "/":
            dirs_and_files = [".."] + dirs_and_files

        def on_done(index):
            if index >= 0:
                dir_or_file = os.path.join(directory, dirs_and_files[index])
                if os.path.isfile(dir_or_file):
                    self.window.open_file(dir_or_file)
                else:
                    self.traverse(dir_or_file)

        self.window.show_quick_panel(dirs_and_files, on_done)
