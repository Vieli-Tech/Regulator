import os

class Tool():

    @staticmethod
    def clearTerminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def setConfig(self, title: str, transform: callable = str, value = None, options=None):
        valid = False
        informed = None
        while not valid:
            if options is not None:
                print('Por favor informe uma opção para ', title)
                for option in options:
                    print('\t* ', option)
            informed = input('{} [{}]:'.format(title, value))
            if informed == '' and value is None:
                print('Por favor, informe um valor')
            elif informed != '' and options is None:
                try:
                    informed = transform(informed)
                    valid = True
                except Exception as e:
                    print('O valor informado não é valido', e)
            elif informed != '' and options is not None:
                if informed in options:
                    valid = True
                else:
                    print('Informe uma opção válida!')
            else:
                valid = True
        return informed

    def run(self):
        """Runs the tool"""
        pass
