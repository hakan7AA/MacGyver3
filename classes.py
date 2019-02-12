import pygame
from pygame.locals import *

class MacGyver:
  def __init__(self):
    self.coord = Coordinates(None, None)
    self.sprite = pygame.image.load('ressource/MacGyver.png')

  def get_coord(self):
    return self.coord

  def set_coord(self, coord):
    self.coord = coord

  def get_sprite(self):
    return self.sprite

  def empty(self):
    self.sprite = pygame.image.load('ressource/exit.png')

class Exit:
  def __init__(self):
    self.coord = Coordinates(None, None)
    self.sprite = pygame.image.load('ressource/exit.png')

  def get_coord(self):
    return self.coord

  def set_coord(self, coord):
    self.coord = coord

  def get_sprite(self):
    return self.sprite

  def empty(self):
    self.sprite = pygame.image.load('ressource/MacGyver.png') 


class Coordinates:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y

class Square:
  def __init__(self, coord, is_wall):
    self.coord = coord
    self.is_wall = is_wall
    self.has_item = False
    self.item = Item(None, 'ressource/empty.png')

  def get_coord(self):
    return self.coord

  def get_is_wall(self):
    return self.is_wall

  def get_has_item(self):
    return self.has_item

  def set_has_item(self, state):
    self.has_item = state
  
  def get_item(self):
    return self.item

  def set_item(self, item):
    self.item = item  


class Item:
  def __init__(self, name, sprite):
    self.name = name # pour initialiser et montrer que dans item(none, etc) le none sera remplacer par le nom que j'ai initialiser et qui se trouve dans macgyver.py
    self.coord = Coordinates(None, None)
    self.sprite = pygame.image.load(sprite).convert_alpha() #pour dire affiche les sprite c a dire les item tous 

  def get_coord(self):
    return self.coord

  def get_sprite(self):
    return self.sprite 

  def set_coord(self, coord):
    self.coord = coord          
        
