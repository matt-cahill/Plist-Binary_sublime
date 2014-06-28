import sublime, sublime_plugin
import os
# import stat
import shutil

class ToggleBinaryCommand(sublime_plugin.TextCommand):
  
  def run(self, view, args=None):
    fname = self.view.file_name()
    if os.path.splitext(fname)[1].lower() != ".plist":
      sublime.error_message("%s: Not a *.plist file!" % PACKAGE_NAME)
      return

    if self.view.is_dirty():
      sublime.error_message("%s: Can't encode an unsaved file!" % PACKAGE_NAME)
      return

    print(self.view.substr(sublime.Region(0, 5)))

    if self.view.substr(sublime.Region(0, 5)) == "<?xml":
      if os.access(fname, os.W_OK):
        os.system("plutil -convert binary1 " + fname)
        self.view.set_syntax_file("Packages/plist/plist.tmLanguage")
      else:
        shutil.copyfile(fname, "/tmp/plistbinarytemp.plist")
        os.system("plutil -convert binary1 /tmp/plistbinarytemp.plist")
        # self.window.open_file("/tmp/plistbinarytemp.plist")
        self.view.set_syntax_file("Packages/plist/plist.tmLanguage")
    else:
      if os.access(fname, os.W_OK):
        os.system("plutil -convert xml1 " + fname)
        self.view.set_syntax_file("Packages/plist/plist.tmLanguage")
      else:
        shutil.copyfile(fname, "/tmp/plistbinarytemp.plist")
        os.system("plutil -convert xml1 /tmp/plistbinarytemp.plist")
        # self.window.open_file("/tmp/plistbinarytemp.plist")
        self.view.set_syntax_file("Packages/plist/plist.tmLanguage")

    self.view.run_command('revert');
    
