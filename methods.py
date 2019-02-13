"""Pygame, random and class file imoprtation."""
import random
import pygame
from pygame.locals import *
from classes import *


def random_coordinates():
    """Method to get random coordinates. Returns a Coordinates type object."""
    return Coordinates(random.randint(0, 14), random.randint(0, 14))


def generate_laby(player, exit):
    """
    Method to generate the laby.

    Transforms the .txt file into a list of lines, then each line into a list of characters.
    For each character it will generate a square, or set Macgyver/exit's position.
    """
    with open('macgyverlaby.txt') as laby:
        str_laby = ''.join(str(line) for line in laby)
        list_str = list(str_laby)
        laby = []
        x = 0
        y = 0

        for entry in list_str:
            # Sets square as a wall if the character is 'm'
            if entry == 'm':
                laby.append(Square(Coordinates(x, y), True))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

            elif entry == 'x':
                # Sets square as empty if the character is 'x'
                laby.append(Square(Coordinates(x, y), False))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

            elif entry == 'd':
                # Sets the inital position of the player if the character is a 'd'
                laby.append(Square(Coordinates(x, y), False))
                player.set_coord(Coordinates(x, y))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

            elif entry == 'a':
                # Sets the position of the exit if the character is a 'a'
                laby.append(Square(Coordinates(x, y), False))
                exit.set_coord(Coordinates(x, y))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

    return laby


def display_laby(laby, window, wall, background, exit, player):
    """Method to display the laby."""
    window.blit(background, (0, 0))
    window.blit(player.get_sprite(), (player.get_coord().get_x() * 30, player.get_coord().get_y() * 30))
    window.blit(exit.get_sprite(), (exit.get_coord().get_x() * 30, exit.get_coord().get_y() * 30))

    for square in laby:
        if square.get_is_wall() is True:
            window.blit(wall, (square.get_coord().get_x() * 30, square.get_coord().get_y() * 30))

        else:
            if square.get_has_item() is True:
                window.blit(square.get_item().get_sprite(), (square.get_coord().get_x() * 30, square.get_coord().get_y() * 30))
    pygame.display.flip()


def put_item_in_laby(laby, item, player, exit):
    """Method to put the items in the laby, at random positions."""
    for square in laby:
        if square.get_coord().get_x() == item.get_coord().get_x() and square.get_coord().get_y() == item.get_coord().get_y():
            if (item.get_coord().get_x() != exit.get_coord().get_x() and item.get_coord().get_y() != exit.get_coord().get_y()) and (item.get_coord().get_x() != player.get_coord().get_x() and item.get_coord().get_y() != player.get_coord().get_y()):
                if square.get_has_item() is True:
                    item.set_coord(random_coordinates())
                    put_item_in_laby(laby, item, player, exit)
                    break
                if square.get_is_wall() is True:
                    item.set_coord(random_coordinates())
                    put_item_in_laby(laby, item, player, exit)
                    break
                if square.get_is_wall() is False and square.get_has_item() is False: # si ya pas de mur ni d'item alors
                    square.set_has_item(True) #ajoute un item
                    square.set_item(item) # 
                    break
            else:
                item.set_coord(random_coordinates())
                put_item_in_laby(laby, item, player, exit)
                break

    return laby
                                



                    




                                         



