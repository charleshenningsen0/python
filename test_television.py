import pytest
from television import *

class Test:
    def setup_method(self):
        self.tele1 = Television()


    #done after each test
    def teardown_method(self):
        del self.tele1


    def test_init(self):
        assert self.tele1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tele1.power()
        assert self.tele1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tele1.power()
        assert self.tele1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        #on, up one, and muted
        self.tele1.power()
        self.tele1.volume_up()
        self.tele1.mute()
        assert self.tele1.__str__() == "Power = True, Channel = 0, Volume = 0"

        # On and unmuted
        self.tele1.mute()
        assert self.tele1.__str__() == "Power = True, Channel = 0, Volume = 1"

        # off and muted
        self.tele1.power()
        self.tele1.mute()
        assert self.tele1.__str__() == "Power = False, Channel = 0, Volume = 1"

        # off and unmuted
        self.tele1.mute()
        assert self.tele1.__str__() == "Power = False, Channel = 0, Volume = 1"


    def test_channel_up(self):
        self.tele1.channel_up()
        assert self.tele1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.tele1.power()
        self.tele1.channel_up()
        assert self.tele1.__str__() == "Power = True, Channel = 1, Volume = 0"

        for _ in range(self.tele1.MAX_CHANNEL): # 3
            self.tele1.channel_up()

        assert self.tele1.__str__() == "Power = True, Channel = 0, Volume = 0"



    def test_channel_down(self):
        self.tele1.channel_down()
        assert self.tele1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.tele1.power()
        self.tele1.channel_down()
        assert self.tele1.__str__() == f'Power = True, Channel = {self.tele1.MAX_CHANNEL}, Volume = 0'



    def test_volume_up(self):
        self.tele1.volume_up()
        assert self.tele1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.tele1.power()
        self.tele1.volume_up()
        assert self.tele1.__str__() == "Power = True, Channel = 0, Volume = 1"

        self.tele1.mute()
        self.tele1.volume_up()
        assert self.tele1.__str__() == "Power = True, Channel = 0, Volume = 2"

        for _ in range(self.tele1.MAX_VOLUME):
            self.tele1.volume_up()
        assert self.tele1.__str__() == f"Power = True, Channel = 0, Volume = {self.tele1.MAX_VOLUME}"

    def test_volume_down(self):
        self.tele1.volume_down()
        assert self.tele1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.tele1.power()
        for _ in range(self.tele1.MAX_VOLUME):
            self.tele1.volume_up()

        self.tele1.volume_down()
        assert self.tele1.__str__() == f"Power = True, Channel = 0, Volume = {self.tele1.MAX_VOLUME - 1}"

        self.tele1.mute()
        self.tele1.volume_down()
        assert self.tele1.__str__() == f"Power = True, Channel = 0, Volume = {self.tele1.MAX_VOLUME - 2}"



