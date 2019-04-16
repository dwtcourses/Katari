
from Katari.sip import SipMessage


class SipMessage:
    def __init__(self, message):
        self.message = message
        self.info = SipMessage.parse(message)
        self.port = info.get("port")
        self.transport = info.get("transport")
        self.address = info.get("address")
        

    @staticmethod
    def parse(sip_message):
        """
        Takes in a sip message
        :param sip_message:
        :return: dict

        >>> a = parse("<sip:cal3254@192.234.1.12:5060;transport=udp>")
        >>> a.port == 5060
        true
        >>> a.address == "cal3254@192.234.1.12"
        true
        >>> a.transport == "udp"
        true
        """
        message = sip_message[5:-1]
        # cal3254@192.234.1.12:5060;transport=udp
        if sip_message[:5] != "<sip:":
            raise Exception("tis not a sip message? :(")
        loc, tp = message.split(";")
        transport = tp.split("=")[1]
        address, port = loc.split(":")
        return dict(address=address, port=port, transport=transport)
