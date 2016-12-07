import sublime
import sublime_plugin

import sys, os

class ToggleFoldCommand(sublime_plugin.TextCommand):

  DEBUG = False

  def p(self, msg):
    if self.DEBUG:
      print(msg)

  def run(self, edit):

    sel = self.view.sel()

    if len(sel) == 1:
      region = sel[0]
      is_fold = self.view.fold(region)

      if is_fold == False:
        self.view.unfold(region)
      self.p(is_fold)

