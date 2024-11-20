
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__previousVolume = self.__volume

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status == True:
            self.__muted = not self.__muted#switch
            self.__previousVolume, self.__volume = self.__volume, self.__previousVolume

    def channel_up(self):
        if self.__status == True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status == True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status == True:#if on
            if self.__muted == True:
                self.mute()

            if self.__volume == self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self):
        #maybe always need to -=1
        #Go line by line, maybe test, see where we are going wrong here
        if self.__status == True:#if on
            if self.__muted == False:#if unmuted
                if self.__volume == self.MIN_VOLUME:
                    self.__volume = self.MIN_VOLUME
                else:
                    self.__volume -= 1
            else:#if muted
                self.mute()  # unmute
                if self.__volume == self.MIN_VOLUME:
                    self.__volume = self.MIN_VOLUME
                else:
                    self.__volume -= 1





    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'