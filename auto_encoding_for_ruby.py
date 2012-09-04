# 
# Copyright (c) 2012 by Lifted Studios.  All Rights Reserved.
# 

import constants
import re
import sublime
import sublime_plugin

class AutoEncodingForRuby(sublime_plugin.EventListener):
  '''
  Automatically adds or removes an encoding declaration, if necessary, at the top of the file.
  '''

  def __init__(self):
    '''
    Initializes the plugin.
    '''
    self.settings = sublime.load_settings(constants.SETTINGS_FILE)

  def on_load(self, view):
    self.handle_encoding_declaration_on(view)

  def on_modified(self, view):
    self.handle_encoding_declaration_on(view)

  def handle_encoding_declaration_on(self, view):
    if self.is_ruby_file_on(view):
      try:
        self.decode_to_ascii_the_content_of(view)
      except UnicodeEncodeError:
        if not self.has_encoding_declaration_on_first_line_of(view):
          self.add_encoding_declaration_on_the_first_line_of(view)
      else:
        if self.has_encoding_declaration_on_first_line_of(view):
          self.remove_encoding_declaration_on_the_first_line_of(view)

  def is_ruby_file_on(self, view):
    return re.search("Ruby", view.settings().get("syntax"), re.IGNORECASE)

  def decode_to_ascii_the_content_of(self, view):
    file_content = view.substr(sublime.Region(0, view.size()))

    file_content.decode("ascii")

  def has_encoding_declaration_on_first_line_of(self, view):
    pattern = self.settings.get(constants.ENCODING_PATTERN)
    return re.match(pattern, self.first_line_from(view), re.IGNORECASE)

  def first_line_from(self, view):
    return view.substr(view.full_line(0))

  def add_encoding_declaration_on_the_first_line_of(self, view):
    edit = view.begin_edit()
    view.insert(edit, 0, self.settings.get(constants.SETTING_FORMAT) + "\n\n")
    view.end_edit(edit)

  def remove_encoding_declaration_on_the_first_line_of(self, view):
    edit = view.begin_edit()
    self.erase_first_line_of(view, edit)

    if self.has_only_whitespace_on_the_first_line_of(view):
      self.erase_first_line_of(view, edit)

    view.end_edit(edit)

  def erase_first_line_of(self, view, edit):
    view.erase(edit, view.full_line(0))

  def has_only_whitespace_on_the_first_line_of(self, view):
    return re.search("^\s*$", self.first_line_from(view))