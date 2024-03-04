# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name="firstuiScript", version="0.0.1")
class firstuiScript(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def firstuiScriptServerInit(self):
        serverApi.RegisterSystem('firstuiScript', 'uiServerSystem',
                                 'firstuiScript.uiServerSystem.uiServerSystem')

    @Mod.DestroyServer()
    def firstuiScriptServerDestroy(self):
        serverApi.RegisterSystem('firstuiScript', 'uiServerSystem',
                                 'firstuiScript.uiServerSystem.uiServerSystem')

    @Mod.InitClient()
    def firstuiScriptClientInit(self):
        clientApi.RegisterSystem('firstuiScript', 'firstuiClientSystem',
                                 'firstuiScript.firstuiClientSystem.firstuiClientSystem')

    @Mod.DestroyClient()
    def firstuiScriptClientDestroy(self):
        clientApi.RegisterSystem('firstuiScript', 'firstuiClientSystem',
                                 'firstuiScript.firstuiClientSystem.firstuiClientSystem')
