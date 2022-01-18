import traceback
from datetime import datetime
from time import sleep
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder

from src.tool import Tool
from src.modbus.ModBusTCPSyncClient import ModBusTCPSyncClient


class Mnemonic2Postgres(Tool):

    def __init__(self):
        self.ip: str = None
        self.menus = {
            'configurar': self.config
        }

    def config(self):
        self.ip = self.setConfig('IP', value=self.ip)

    def run(self):
        while True:
            self.clearTerminal()
            print(
                """
 _ _ _                                  __  _ __                        
( / ) )                          o        )( /  )      _/_              
 / / / _ _   _  _ _ _   __ _ _  ,  _, .--'  /--'__ (   /  _,  _   _  (  
/ / (_/ / /_(/_/ / / /_(_)/ / /_(_(__(__   /   (_)/_)_(__(_)_/ (_(/_/_)_
                                                          /|            
                                                         (/             
"""
            )
            print('Configurações:\n\tIP={}'.format(
                self.ip
            ))
            print('\nInforme uma opção:')
            for index, menu in enumerate(self.menus.keys()):
                print('\t* {} - {}'.format(index, menu))
            print('* Ou qualquer outra coisa para sair')
            choosen = input('Opção: ')
            length = len(self.menus.keys())
            try:
                index = int(choosen)
                if index > -1 and index < length:
                    choosen = list(self.menus.keys())[index]
            except ValueError:
                pass
            if choosen in self.menus.keys():
                self.menus[choosen]()
            else:
                return
