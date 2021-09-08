import traceback
from datetime import datetime
from time import sleep
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder

from src.tool import Tool
from src.modbus.ModBusTCPSyncClient import ModBusTCPSyncClient


class ModBus(Tool):

    def __init__(self):
        self.ip: str = None
        self.port: int = None
        self.register: int = None
        self.type: str = None
        self.types = [
            'coil',
            'float32'
        ]
        self.order: str = None
        self.orders = [
            'big-little',
            'big-big',
            'little-big'
        ]
        self.menus = {
            'ler': self.read,
            'gravar': self.write,
            'configurar': self.config
        }

    def config(self):
        self.ip = self.setConfig('IP', value=self.ip)
        self.port = self.setConfig('Porta', transform=int, value=self.port)
        self.register = self.setConfig(
            'Registrador', transform=int, value=self.register)
        self.type = self.setConfig(
            'Tipo do Registrador', value=self.type, options=self.types)
        self.order = self.setConfig(
            'Ordem dos Bytes', value=self.order, options=self.orders)

    def read(self):
        try:
            value = None
            connection = ModBusTCPSyncClient(self.ip, self.port)
            byteorder = None
            wordorder = None
            if connection.is_socket_open():
                if self.order == 'big-little':
                    byteorder = Endian.Big
                    wordorder = Endian.Little
                elif self.order == 'big-big':
                    byteorder = Endian.Big
                    wordorder = Endian.Big
                else:
                    byteorder = Endian.Little
                    wordorder = Endian.Big
                if self.type == 'coil':
                    value = connection.read_coils(
                        self.register, unit=1).bits[0]
                elif self.type == 'float32':
                    BinaryPayloadDecoder.fromRegisters(
                        connection.read_holding_registers(
                            self.register, 2, unit=1
                        ).registers,
                        byteorder=byteorder, wordorder=wordorder
                    ).decode_32bit_float()
                print('Lido valor: ', value)
            else:
                print('Não foi possível se conectar para realizar a leitura')
        except Exception as e:
            print('Erro: ', e)
            print(traceback.format_exc())
        finally:
            input('Pressione Enter para continuar')

    def write(self):
        try:
            value = input('Informe um valor a ser gravado: ')
            if self.type == 'coil':
                value = int(value)
            else:
                value = float(value)
            connection = ModBusTCPSyncClient(self.ip, self.port)
            byteorder = None
            wordorder = None
            if connection.is_socket_open():
                if self.order == 'big-little':
                    byteorder = Endian.Big
                    wordorder = Endian.Little
                elif self.order == 'big-big':
                    byteorder = Endian.Big
                    wordorder = Endian.Big
                else:
                    byteorder = Endian.Little
                    wordorder = Endian.Big
                if self.type == 'coil':
                    connection.write_coil(self.register, value, unit=1)
                elif self.type == 'float32':
                    builder = BinaryPayloadBuilder(byteorder=byteorder, wordorder=wordorder)
                    builder.add_32bit_float(value)
                    connection.write_registers(self.register, builder.to_registers(), unit=1)
                print('Valor gravado!')
            else:
                print('Não foi possível se conectar para realizar a leitura')
        except Exception as e:
            print('Erro: ', e)
            print(traceback.format_exc())
        finally:
            input('Pressione Enter para continuar')

    def run(self):
        while True:
            self.clearTerminal()
            print(
                """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▀▄░█▀▄▄▀█░▄▀██░▄▄▀█░██░█░▄▄
██░█░█░█░██░█░█░██░▄▄▀█░██░█▄▄▀
██░███░██▄▄██▄▄███░▀▀░██▄▄▄█▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""
            )
            print('Configurações:\n\tIP={}\n\tPorta={}\n\tRegistrador={}\n\tTipo={}\n\tOrdem={}'.format(
                self.ip,
                self.port,
                self.register,
                self.type,
                self.order
            ))
            print('\nInforme uma opção:')
            for menu in self.menus.keys():
                print('\t* ', menu)
            print('* Ou qualquer outra coisa para sair')
            choosen = input('Opção: ')
            if choosen in self.menus.keys():
                self.menus[choosen]()
            else:
                return

