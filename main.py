#!/usr/bin/env python
# -*- coding: utf-8 -*-

###Os nomes de variáveis abaixo não foram discutidos e consensuados###
####Sugestão de criar arquivo de nomes e abreviaturas padrão #####

import pygame

pygame.init()

import os

#ideal screen: 1024x768#

pygame.display.set_caption("Glamour - OcaStudios")
#### Define o favicon do jogo ###
pygame.display.set_icon(pygame.image.load(os.path.join(directory.interface,'favicon.png')).convert_alpha())

os_screen = pygame.display.Info() #pega a resolução em uso
resolution = (os_screen.current_w,os_screen.current_h) #cria uma tupla com os valores da resolução atual

possible_resolutions = pygame.display.list_modes()
resolition_size = possible_resolutions[0] #pega a maior resolução que a tela aceita

resolution = os_screen.current_w,os_screen.current_h

	import directory
	#### Main directories ####
	homedir		= os.path.expanduser('~')# para linux
	main_dir	= os.path.join('/','usr','share','games','glamour')
	data_dir	= os.path.join(main_dir,"data")
	personal	= os.path.join(homedir ,'.glamour')
	saves_dir	= os.path.join(personal, 'saves')
	cache		= os.path.join(personal, 'cache')
	image_cache = os.path.join(personal, 'cache', 'images')
	for i in (personal, saves_dir, cache, image_cache):
		try:
			os.listdir(i)
		except:
			os.mkdir(i)



def splash_image():
	"""This function is independent of the game.
	Runs the splash screen"""

	splash = pygame.image.load(os.path.join(directory.data,'splash.png')).convert(32)
	introdir = os.path.join(directory.data,'images', 'intro','quanti')
	splash =[pygame.image.load(os.path.join(introdir,i)).convert(32) for i in sorted(os.listdir(introdir))]
	splash_size = splash[0].get_size()
	print "Setting SDV_VIDEO_CENTERED to True"
	os.environ['SDL_VIDEO_CENTERED'] = '1' ##IMPORTANTE ## Centraliza a tela de splash# função SDL
	print "Creating Splash Screen"

	splash_surface = pygame.display.set_mode(splash_size, pygame.NOFRAME)
	print "Creating and Setting Favicon"



	print "Showing Splash Screen"
	tempclock = pygame.time.Clock()
	for i in splash:
		splash_surface.blit(i,(0,0))
		pygame.display.flip()
		tempclock.tick(40)


#### Translation function ####
import gettext
localization_support = gettext.translation('glamour', os.path.join(main_dir,'locale'))
t = localization_support.ugettext


#screen = pygame.display.set_mode((w,h),32)
screen = pygame.display.set_mode((w,h),pygame.FULLSCREEN , 32)

import sqlite3


class App():
	def __init__():
		blabla

class Interface():
	def __init__():
		blabla

class Game():
	def __init__():
		blabla

if __name__=="__main__":
	app = App()

	app.interface = Interface()
	app.game = Game()

	while True:
		events 	= get_events()

		app.interface.loop(events)

		app.game.loop(interface.results)

		app.clock.tick(fps)

		pygame.display.flip()

