import xbmcaddon,os,requests,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin

def CATEGORIES():
   addDir3('Stupcat Egjeli 2019','https://pastebin.com/iW5n03EL',2,'https://shkoder.gjirafa.com/api/storage/gjvideo/images/serie/background/stupcat-egjeli.jpg','','')
   addDir3('Ekspertiza','https://pastebin.com/wvkkmsC1',3,'https://www.chip.de/ii/4/4/9/4/6/0/7/4/f408a47699a0a859.png','','')
   addDir2('SchengenVisa','https://pastebin.com/kKqRYa4N',4,'https://www.chip.de/ii/4/4/9/4/6/0/7/4/f408a47699a0a859.png','','')
   addDir3('Filma','https://pastebin.com/u7hVnKXR',5,'http://www.newscrane.com/wp-content/uploads/2018/01/Newscrane-movie-feature3.jpg','','')
   
def Ekspertiza():
   r = requests.get('https://pastebin.com/wvkkmsC1')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
	 
def Moviess():
   r = requests.get('https://pastebin.com/u7hVnKXR')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def SchengenVisa():
   r = requests.get('https://pastebin.com/kKqRYa4N')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')

def Stupcat_Egjeli_2019():
   r = requests.get('https://pastebin.com/iW5n03EL')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
	 
def addLink(name,url,image,urlType,fanart):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable','true')
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param       
#################################################################################################################

#                               NEED BELOW CHANGED

  
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
     
def addDir2(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
###############################################################################################################        

def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % viewType )
 


              
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        OPEN_URL(url)
elif mode==2:
        Stupcat_Egjeli_2019()
elif mode==3:
        Ekspertiza()
elif mode==4:
        SchengenVisa()
elif mode==5:
        Moviess()


        


xbmcplugin.endOfDirectory(int(sys.argv[1]))
