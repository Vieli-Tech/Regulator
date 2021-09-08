from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ConnectionException
from time import sleep


class ModBusTCPSyncClient(ModbusTcpClient):

    def execute(self, request=None):
        """
        :param request: The request to process
        :returns: The result of the request execution
        """
        if not self.connect():
            raise ConnectionException(
                "Failed to connect[%s]" % (self.__str__()))
        res = self.transaction.execute(request)
        sleep(0.01)
        return res
