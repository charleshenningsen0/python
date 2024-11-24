
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Initializes the Television object
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__previousVolume: int = self.__volume

    def power(self) -> None:
        '''
        Changes truth value of __status
        '''
        self.__status = not self.__status

    def mute(self) -> None:
        '''
        Changes truth value of __muted and swaps __previousVolume with __volume
        '''
        if self.__status == True:
            self.__muted = not self.__muted#switch
            self.__previousVolume, self.__volume = self.__volume, self.__previousVolume

    def channel_up(self) -> None:
        '''
        When on, channel number if max, then changes to zero, otherwise up by one
        '''
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        When on, changes channel number if min, then changes to max, otherwise down by one
        '''
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        When on, if muted call mute(), then if max, no change, otherwise add volume by one
        '''
        if self.__status == True:#if on
            if self.__muted == True:
                self.mute()

            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        When on, if muted call mute(), then if max, no change, otherwise add volume by one
        '''
        if self.__status == True:#if on
            if self.__muted == False:#if unmuted
                if self.__volume == Television.MIN_VOLUME:
                    self.__volume = Television.MIN_VOLUME
                else:
                    self.__volume -= 1
            else:#if muted
                self.mute()  # unmute
                if self.__volume == Television.MIN_VOLUME:
                    self.__volume = Television.MIN_VOLUME
                else:
                    self.__volume -= 1





    def __str__(self) -> str:
        '''
        Returns the state of the television object
        :return: Television status, channel, and volume as str
        '''
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'