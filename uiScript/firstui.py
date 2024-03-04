# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class firstui(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        # 初始化当前时间
        self.SetTime = 0
        # 初始化当前天气
        self.SetWeather = False
        # 初始化当前游戏模式
        self.SetGameMode = 0

    # Create函数无需初始化，会在创建完毕UI后自动调用
    def Create(self):
        # 昼夜切换按钮路径
        self.GetBaseUIControl("/all_panel/panel_1/button_1").asButton().AddTouchEventParams()
        self.GetBaseUIControl("/all_panel/panel_1/button_1").asButton().SetButtonTouchDownCallback(self.Day_NightSwitch)
        # 天气切换按钮路径
        self.GetBaseUIControl("/all_panel/panel_2/button_2").asButton().AddTouchEventParams()
        self.GetBaseUIControl("/all_panel/panel_2/button_2").asButton().SetButtonTouchDownCallback(self.WeatherSwitch)
        # 模式切换按钮路径
        self.GetBaseUIControl("/all_panel/panel_3/button_3").asButton().AddTouchEventParams()
        self.GetBaseUIControl("/all_panel/panel_3/button_3").asButton().SetButtonTouchDownCallback(self.gameModeSwitch)

    # 用于判断按下按钮后的世界时间，并通知到服务端
    def Day_NightSwitch(self, args):
        if self.SetTime == 0:
            clientApi.GetSystem("firstuiScript", "firstuiClientSystem").NotifyToServer("ButtonClickEvent",
                                                                                       {"SetTime": 0})
            self.SetTime = 1
        elif self.SetTime == 1:
            clientApi.GetSystem("firstuiScript", "firstuiClientSystem").NotifyToServer("ButtonClickEvent",
                                                                                       {"SetTime": 1})
            self.SetTime = 0

    # 控制天气切换

    def WeatherSwitch(self, args):
        if self.SetWeather == False:
            clientApi.GetSystem("firstuiScript", "firstuiClientSystem").NotifyToServer("onButtonClickEvent",
                                                                                       {"SetWeather": False})
            self.SetWeather = True
        elif self.SetWeather == True:
            clientApi.GetSystem("firstuiScript", "firstuiClientSystem").NotifyToServer("onButtonClickEvent",
                                                                                       {"SetWeather": True})
            self.SetWeather = False

    # 控制游戏模式切换
    def gameModeSwitch(self, args):
        if self.SetGameMode == 0:
            clientApi.GetSystem("firstuiScript", "firstuiClientSystem").NotifyToServer("ButtonSwitchEvent",
                                                                                       {"SetTime": 0})
            self.SetGameMode = 1
        elif self.SetGameMode == 1:
            clientApi.GetSystem("firstuiScript", "firstuiClientSystem").NotifyToServer("ButtonSwitchEvent",
                                                                                       {"SetTime": 1})
            self.SetGameMode = 0
        elif self.SetGameMode == 2:
            clientApi.GetSystem("firstuiScript", "firstuiClientSystem").NotifyToServer("ButtonSwitchEvent",
                                                                                       {"SetTime": 2})
            self.SetGameMode = 1
