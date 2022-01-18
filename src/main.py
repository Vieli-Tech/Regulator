import traceback

from src.tool import Tool

from src.modbus import ModBus


class Main():

    def __init__(self):
        self.tool: Tool = None
        self.last_tool: Tool = None
        self.options = {
            'modbus': ModBus
        }

    def menu(self):
        print('Informe uma ferramenta:')
        for index, option in enumerate(self.options.keys()):
            print('\t* {} - {}'.format(index, option))
        if self.last_tool is not None:
            print('Última ferramenta: \n\t* last')
        choosen = input('Opção: ')
        length = len(self.options.keys())
        try:
            index = int(choosen)
            if index > -1 and index < length:
                choosen = list(self.options.keys())[index]
        except ValueError:
            pass
        if choosen in self.options.keys():
            self.tool = self.options[choosen]()
            self.last_tool = self.tool
            return True
        elif choosen == 'last':
            self.tool = self.last_tool
        else:
            print('Ferramenta não encontrada!')
            return False

    def run(self):
        while True:
            print(
                """
.#####...######...####...##..##..##.......####...######...####...#####..
.##..##..##......##......##..##..##......##..##....##....##..##..##..##.
.#####...####....##.###..##..##..##......######....##....##..##..#####..
.##..##..##......##..##..##..##..##......##..##....##....##..##..##..##.
.##..##..######...####....####...######..##..##....##.....####...##..##.
........................................................................
"""
            )
            if self.tool is None:
                self.menu()
            else:
                try:
                    self.tool.run()
                except Exception as e:
                    print('Erro na ferramenta {}:'.format(self.tool.__name__), e)
                    print(traceback.format_exc())
                finally:
                    self.tool = None


main = Main()
main.run()
