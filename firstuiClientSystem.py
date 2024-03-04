# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
levelId = clientApi.GetLevelId()


class firstuiClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
                            'UiInitFinished', self, self.ui_init)

    # 注册并创建ui
    def ui_init(self, args):
        clientApi.RegisterUI("firstui", "first_ui", "firstuiScript.uiScript.firstui.firstui",
                             "first_ui.main")
        clientApi.CreateUI("firstui", "first_ui", {"isHud": 1})

    def Destroy(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
                              'UiInitFinished', self, self.ui_init)
