"""All Utilities and Classes for Notes Graphical Display"""
import os
import pygame

from .gui.screen import Screen
from .gui.textbox import TextArea


class NotesScreen(Screen):
    """Class to open a notes screen"""

    def __init__(self):
        super().__init__()
        os.path.join("C:/Users/project2-waid/assets/media/notes/notes.txt")
        file = open("assets/media/notes/notes.txt", "r+")
        self._textarea = TextArea((0, 0), (self.screen_width, self.screen_height),
                                  always_selected=True, initial_value=file.read())
        print(file.read())


    def _draw(self, screen):
        self._textarea.draw(screen)

    def _handle_events(self, events):
        super()._handle_events(events)
        self._textarea.handle_events(events)

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.close()
