import sublime_plugin
import os
from glob import iglob

class TraverseCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        if kwargs['start'] == "root":
            self.start_directory = "/"
        elif kwargs['start'] == "home":
            self.start_directory = os.path.expanduser("~")
        elif kwargs['start'] == "project":
            self.start_directory = self.window.folders()[0]
        self.traverse(self.start_directory)

    def traverse(self, directory):
        directory = os.path.abspath(directory)
        dirs_and_files = self.find_dirs_and_files(directory)
        if directory != self.start_directory:
            dirs_and_files = [".."] + dirs_and_files

        def on_done(index):
            if index >= 0:
                dir_or_file = os.path.join(directory, dirs_and_files[index])
                if os.path.isfile(dir_or_file):
                    self.window.open_file(dir_or_file)
                else:
                    self.traverse(dir_or_file)

        self.window.show_quick_panel(dirs_and_files, on_done)

    def find_dirs_and_files(self, directory):
        filepaths = [f for f in iglob(os.path.join(directory, '*'))]
        filepaths += [f for f in iglob(os.path.join(directory, '.*'))]
        dirs_and_files = [os.path.basename(f) + "/" for f in filepaths if os.path.isdir(f)]
        dirs_and_files += [os.path.basename(f) for f in filepaths if os.path.isfile(f)]
        return dirs_and_files
