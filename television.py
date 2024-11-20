
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
        '''
        Changes truth value of __status
        :param self: television object
        :return: void
        '''
        self.__status = not self.__status

    def mute(self):
        '''
        Changes truth value of __muted and swaps __previousVolume with __volume
        :param self: television object
        :return: void
        '''
        if self.__status == True:
            self.__muted = not self.__muted#switch
            self.__previousVolume, self.__volume = self.__volume, self.__previousVolume

    def channel_up(self):
        '''
        When on, channel number if max, then changes to zero, otherwise up by one
        :param self: television object
        :return: void
        '''
        if self.__status == True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        '''
        When on, changes channel number if min, then changes to max, otherwise down by one
        :param self: television object
        :return: void
        '''
        if self.__status == True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        '''
        When on, if muted call mute(), then if max, no change, otherwise add volume by one
        :param self: television object
        :return: void
        '''
        if self.__status == True:#if on
            if self.__muted == True:
                self.mute()

            if self.__volume == self.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self):
        '''
        When on, if muted call mute(), then if max, no change, otherwise add volume by one
        :param self: television object
        :return: void
        '''
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





    def __str__(self) -> str:
        '''
        Returns the state of the television object
        :param self: television object
        :return: Television status, channel, and volume
        '''
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'