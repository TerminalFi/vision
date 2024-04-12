import sublime
import sublime_plugin


class MiniHtmlTextCommandShim(sublime_plugin.TextCommand):
    def run(self, _, command: str, args: dict):
        self.view.run_command(command, args)


class MiniHtmlWindowCommandShim(sublime_plugin.WindowCommand):
    def run(self, command: str, args: dict):
        self.window.run_command(command, args)


class MiniHtmlApplicationCommandShim(sublime_plugin.ApplicationCommand):
    def run(self, _, command: str, args: dict):
        sublime.run_command(command, args)
