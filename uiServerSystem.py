# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()
levelId = serverApi.GetLevelId()


class uiServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        # 监听ui脚本发布的服务端通讯事件
        self.ListenForEvent("firstuiScript", "firstuiClientSystem",
                            "ButtonClickEvent", self, self.onButtonClick)
        self.ListenForEvent("firstuiScript", "firstuiClientSystem",
                            "onButtonClickEvent", self, self.usedWeatherSwitch)
        self.ListenForEvent("firstuiScript", "firstuiClientSystem",
                            "ButtonSwitchEvent", self, self.useGameModeSwitch)

    # 设置当期时间

    def onButtonClick(self, args):
        passedTime = serverApi.GetEngineCompFactory().CreateTime(levelId).GetTime()
        day = passedTime / 24000
        if args["SetTime"] == 0:
            serverApi.GetEngineCompFactory().CreateTime(levelId).SetTime(day * 24000 + 65000)
        elif args["SetTime"] == 1:
            serverApi.GetEngineCompFactory().CreateTime(levelId).SetTime(day * 24000 + 10000)

    # 设置当前天气

    def usedWeatherSwitch(self, args):
        passedWeather = serverApi.GetEngineCompFactory().CreateWeather(levelId).IsRaining()
        if not passedWeather:
            serverApi.GetEngineCompFactory().CreateWeather(levelId).SetRaining(1, 1000)
        elif passedWeather:
            serverApi.GetEngineCompFactory().CreateWeather(levelId).SetRaining(0, 1000)

    # 设置用户模式

    def useGameModeSwitch(self, args):
        passedGameMode = serverApi.GetEngineCompFactory().CreateGame(levelId).GetGameType()
        if passedGameMode == 0:
            serverApi.GetEngineCompFactory().CreateGame(levelId).SetDefaultGameType(1)
        elif passedGameMode == 1:
            serverApi.GetEngineCompFactory().CreateGame(levelId).SetDefaultGameType(0)
        elif passedGameMode == 2:
            serverApi.GetEngineCompFactory().CreateGame(levelId).SetDefaultGameType(1)

    # 销毁函数

    def Destroy(self):
        self.UnListenForEvent("firstuiScript", "firstuiClientSystem",
                              "ButtonClickEvent", self, self.onButtonClick)
        self.UnListenForEvent("firstuiScript", "firstuiClientSystem",
                              "onButtonClickEvent", self, self.usedWeatherSwitch)
        self.UnListenForEvent("firstuiScript", "firstuiClientSystem",
                              "onButtonClickEvent", self, self.useGameModeSwitch)
