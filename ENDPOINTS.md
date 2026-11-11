# Divoom TimesFrame Local REST API Endpoints

Base URL: `http://<DEVICE_IP>:9000/divoom_api`

All calls are HTTP GET with a JSON body. The body always includes `"Command": "<CommandName>"`.

## Command Summary

| Command | Purpose | Request class | Request params | Response class |
|---|---|---|---|---|
| `Channel/Add5LcdHistory` | Add5Lcd History | `_unknown_` | — | `_unknown_` |
| `Channel/AddEqData` | Add Eq Data | `com.divoom.Divoom.http.request.channel.ChannelAddEqDataRequest` | `AuthorHeadId`, `AuthorId`, `AuthorNickName`, `FileId`, `ImageName` | `_unknown_` |
| `Channel/AddHistory` | Add History | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelAddHistoryRequest` | — | `_unknown_` |
| `Channel/AddIndependence` | Add Independence | `com.divoom.Divoom.http.request.channel.wifi.WIfiChannelAddIndependenceRequest` | — | `com.divoom.Divoom.http.response.channel.wifi.WIfiChannelAddIndependenceResponse` |
| `Channel/CleanCustom` | Clean Custom | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelCleanCustomRequest` | `CustomPageIndex` | `_unknown_` |
| `Channel/ClockCommentLike` | Clock Comment Like | `_unknown_` | — | `_unknown_` |
| `Channel/CoverPixelClock` | Cover Pixel Clock | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelCoverPixelClockRequest` | `CoverPixelFileId` | `_unknown_` |
| `Channel/CustomChange` | Custom Change | `_unknown_` | — | `_unknown_` |
| `Channel/DelHistory` | Del History | `_unknown_` | — | `_unknown_` |
| `Channel/DelIndependence` | Del Independence | `com.divoom.Divoom.http.request.channel.wifi.WIfiChannelDelIndependenceRequest` | — | `_unknown_` |
| `Channel/DeleteCustom` | Delete Custom | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelDeleteCustomRequest` | `CustomId`, `CustomPageIndex` | `_unknown_` |
| `Channel/DeleteEq` | Delete Eq | `_unknown_` | — | `_unknown_` |
| `Channel/DeletePixelClock` | Delete Pixel Clock | `_unknown_` | — | `_unknown_` |
| `Channel/DeviceGetMyClock` | Device Get My Clock | `com.divoom.Divoom.http.request.myCLock.DeviceGetMyClockRequest` | `ClockList` | `_unknown_` |
| `Channel/EqDataChange` | Eq Data Change | `_unknown_` | — | `_unknown_` |
| `Channel/ExitNightPreview` | Exit Night Preview | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelExitNightPreviewRequest` | — | `_unknown_` |
| `Channel/Get5LcdClockList` | Read Lcd Clock List | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGet5LcdClockListV2Request` | `Flag` | `com.divoom.Divoom.http.response.channel.wifi.WifiGet5LcdClockListResponse` |
| `Channel/Get5LcdClockListV2` | Read Lcd Clock List V2 | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGet5LcdClockListV2Request` | `Flag` | `_unknown_` |
| `Channel/Get5LcdInfo` | Read Lcd Info | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGet5LcdInfoV2Response` |
| `Channel/Get5LcdInfoV2` | Read Lcd Info V2 | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGet5LcdInfoV2Response` |
| `Channel/GetAlbumTime` | Read Album Time | `_unknown_` | — | `_unknown_` |
| `Channel/GetAll` | Read All | `com.divoom.Divoom.http.request.channel.ChannelGetAllRequest` | — | `com.divoom.Divoom.http.response.channel.ChannelGetAllResponse` |
| `Channel/GetAllCustomTime` | Read All Custom Time | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetAllCustomTimeResponse` |
| `Channel/GetAmbientLight` | Read Ambient Light | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetAmbientLightResponse` |
| `Channel/GetClockCommentList` | Read Clock Comment List | `_unknown_` | — | `_unknown_` |
| `Channel/GetClockComponentDisplay` | Read Clock Component Display | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetClockComponentDisplayRequest` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockComponentDisplayResponse` |
| `Channel/GetClockConfig` | Read Clock Config | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetClockConfigRequest` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockConfigResponse` |
| `Channel/GetClockFont` | Read Clock Font | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockFontResponse` |
| `Channel/GetClockInfo` | Read Clock Info | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetClockInfoRequest` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockInfoResponse` |
| `Channel/GetClockList` | Read Clock List | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetClockListRequest` | `CountryISOCode`, `Flag`, `Version` | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockListResponse` |
| `Channel/GetClockPlayPlanCycle` | Read Clock Play Plan Cycle | `_unknown_` | — | `_unknown_` |
| `Channel/GetClockPlayPlanDate` | Read Clock Play Plan Date | `_unknown_` | — | `_unknown_` |
| `Channel/GetClockStyle` | Read Clock Style | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetClockStyleRequest` | `CountryISOCode`, `EndNum`, `StartNum` | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockStyleResponse` |
| `Channel/GetConfig` | Read Config | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetConfigRequest` | — | `com.divoom.Divoom.http.response.danmaku.DanmakuGetConfigResponse` |
| `Channel/GetCustomGalleryTime` | Read Custom Gallery Time | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetCustomGalleryTimeRequest` | `CustomId` | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetCustomGalleryTimeResponse` |
| `Channel/GetCustomList` | Read Custom List | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetCustomListRequest` | `CustomPageIndex` | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetCustomListResponse` |
| `Channel/GetCustomPageIndex` | Read Custom Page Index | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetCustomPageIndexResponse` |
| `Channel/GetElementStyleList` | Read Element Style List | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetElementStyleListRequest` | `CountryISOCode`, `EndNum`, `StartNum`, `ItemType` | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetElementStyleListResponse` |
| `Channel/GetEqDataList` | Read Eq Data List | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetEqDataListResponse` |
| `Channel/GetEqPosition` | Read Eq Position | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetEqPositionResponse` |
| `Channel/GetEqTime` | Read Eq Time | `_unknown_` | — | `_unknown_` |
| `Channel/GetIndependenceConfig` | Read Independence Config | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetIndependenceConfigRequest` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetIndependenceConfigResponse` |
| `Channel/GetIndex` | Read Index | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetIndexResponse` |
| `Channel/GetNightView` | Read Night View | `_unknown_` | — | `com.divoom.Divoom.http.response.system.WifiChannelGetNightViewResponse` |
| `Channel/GetNotifyList` | Read Notify List | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetNotifyListResponse` |
| `Channel/GetOnOff` | Read On Off | `_unknown_` | — | `com.divoom.Divoom.http.response.system.WifiChannelGetOnOffResponse` |
| `Channel/GetOnOffScreen` | Read On Off Screen | `com.divoom.Divoom.http.request.channel.wifi.ChannelOnOffScreenRequest` | `OnOff` | `com.divoom.Divoom.http.response.system.WifiChannelGetOnOffScreenResponse` |
| `Channel/GetOneCustom` | Read One Custom | `com.divoom.Divoom.http.request.channel.ChannelGetOneCustomRequest` | `CustomId`, `CustomPageIndex` | `com.divoom.Divoom.http.response.channel.ChannelGetOneCustomResponse` |
| `Channel/GetRGBInfo` | Read RGBInfo | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetRGBInfoResponse` |
| `Channel/GetSongInfo` | Read Song Info | `com.divoom.Divoom.http.request.channel.ChannelGetSongInfoRequest` | — | `com.divoom.Divoom.http.response.channel.ChannelGetSongInfoResponse` |
| `Channel/GetStartupChannel` | Read Startup Channel | `_unknown_` | — | `_unknown_` |
| `Channel/GetSubClockList` | Read Sub Clock List | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetSubClockListRequest` | `CountryISOCode`, `EndNum`, `StartNum`, `ClockType` | `_unknown_` |
| `Channel/GetSubscribe` | Read Subscribe | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetSubscribeRequest` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetSubscribeResponse` |
| `Channel/GetSubscribeGalleryTime` | Read Subscribe Gallery Time | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetSubscribeGalleryTimeResponse` |
| `Channel/GetSubscribeTime` | Read Subscribe Time | `_unknown_` | — | `_unknown_` |
| `Channel/ItemSearch` | Item Search | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelItemSearchRequest` | `EndNum`, `ItemFlag`, `ItemId`, `Key`, `StartNum` | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelItemSearchResponse` |
| `Channel/LikeClock` | Like Clock | `com.divoom.Divoom.http.request.myCLock.MyClockLikeClockRequest` | `LikeFlag` | `_unknown_` |
| `Channel/LoginThird` | Login Third | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelLoginThirdRequest` | `LogInfo`, `Type` | `_unknown_` |
| `Channel/My5LcdClockAdd` | My5Lcd Clock Add | `com.divoom.Divoom.http.request.channel.wifi.My5LcdClockAddRequest` | — | `_unknown_` |
| `Channel/My5LcdClockGetList` | My5Lcd Clock Get List | `com.divoom.Divoom.http.request.channel.wifi.My5LcdClockGetListRequest` | `CountryISOCode`, `EndNum`, `StartNum`, `Flag` | `com.divoom.Divoom.http.response.channel.wifi.My5LcdClockGetListResponse` |
| `Channel/My5LcdClockInsertPosition` | My5Lcd Clock Insert Position | `com.divoom.Divoom.http.request.channel.wifi.My5LcdClockInsertPositionRequest` | `NewPositionClockId` | `_unknown_` |
| `Channel/My5LcdClockRemove` | My5Lcd Clock Remove | `com.divoom.Divoom.http.request.channel.wifi.My5LcdClockRemoveRequest` | — | `_unknown_` |
| `Channel/MyClockAdd` | My Clock Add | `com.divoom.Divoom.http.request.myCLock.MyClockAddRecentRequest` | — | `_unknown_` |
| `Channel/MyClockAddRecent` | My Clock Add Recent | `com.divoom.Divoom.http.request.myCLock.MyClockAddRecentRequest` | — | `_unknown_` |
| `Channel/MyClockBatchRemove` | My Clock Batch Remove | `com.divoom.Divoom.http.request.channel.wifi.MyClockBatchRemoveRequest` | `ClockList` | `_unknown_` |
| `Channel/MyClockGetFavoriteList` | My Clock Get Favorite List | `_unknown_` | — | `_unknown_` |
| `Channel/MyClockGetList` | My Clock Get List | `com.divoom.Divoom.http.request.myCLock.MyClockGetListRequest` | `CountryISOCode`, `EndNum`, `StartNum`, `Flag` | `_unknown_` |
| `Channel/MyClockGetRecentList` | My Clock Get Recent List | `_unknown_` | — | `_unknown_` |
| `Channel/MyClockInsertPosition` | My Clock Insert Position | `com.divoom.Divoom.http.request.myCLock.MyClockInsertPositionRequest` | `NewPositionClockId` | `_unknown_` |
| `Channel/MyClockRemove` | My Clock Remove | `com.divoom.Divoom.http.request.myCLock.MyClockRemoveRequest` | — | `_unknown_` |
| `Channel/MyClockSetFavorite` | My Clock Set Favorite | `_unknown_` | — | `_unknown_` |
| `Channel/NewPixelClock` | New Pixel Clock | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelNewPixelClockRequest` | `ClockType` | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelNewPixelClockResponse` |
| `Channel/OnOffScreen` | On Off Screen | `com.divoom.Divoom.http.request.channel.wifi.ChannelOnOffScreenRequest` | `OnOff` | `com.divoom.Divoom.http.response.system.WifiChannelGetOnOffScreenResponse` |
| `Channel/RenamePixelClock` | Rename Pixel Clock | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelRenamePixelClockRequest` | `ClockName` | `_unknown_` |
| `Channel/ReportClockComment` | Report Clock Comment | `_unknown_` | — | `_unknown_` |
| `Channel/ResetClock` | Reset Clock | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelResetClockRequest` | — | `_unknown_` |
| `Channel/Set5LcdChannelType` | Configure Lcd Channel Type | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSet5LcdChannelTypeRequest` | `ChannelType` | `_unknown_` |
| `Channel/Set5LcdWholeClockId` | Configure Lcd Whole Clock Id | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSet5LcdWholeClockIdRequest` | — | `_unknown_` |
| `Channel/SetAlbumTime` | Configure Album Time | `_unknown_` | — | `_unknown_` |
| `Channel/SetAllCustomTime` | Configure All Custom Time | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetAllCustomTimeRequest` | `TimeList` | `_unknown_` |
| `Channel/SetAmbientLight` | Configure Ambient Light | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetAmbientLightRequest` | `Brightness`, `Color`, `ColorCycle`, `EqOnOff`, `SelectEffect` | `_unknown_` |
| `Channel/SetBrightness` | Configure Brightness | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetBrightnessRequest` | `Brightness` | `com.divoom.Divoom.http.response.system.SysSetBrightnessResponse` |
| `Channel/SetClockConfig` | Configure Clock Config | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetClockConfigRequest` | `ItemList`, `ItemList2` | `_unknown_` |
| `Channel/SetClockConfigSpecial` | Configure Clock Config Special | `_unknown_` | — | `_unknown_` |
| `Channel/SetClockPlayPlanCycle` | Configure Clock Play Plan Cycle | `com.divoom.Divoom.http.request.myCLock.SetClockPlayPlanCycleRequest` | `CycleRuleList` | `_unknown_` |
| `Channel/SetClockPlayPlanDate` | Configure Clock Play Plan Date | `com.divoom.Divoom.http.request.myCLock.SetClockPlayPlanDateRequest` | `DateRuleList` | `_unknown_` |
| `Channel/SetClockSelectId` | Configure Clock Select Id | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetClockSelectIdRequest` | — | `_unknown_` |
| `Channel/SetClockStyle` | Configure Clock Style | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetClockStyleRequest` | `StyleId` | `_unknown_` |
| `Channel/SetConfig` | Configure Config | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetConfigRequest` | `ChannelIndex`, `ClockTime`, `GalleryShowTimeFlag`, `GalleryTime`, `LcdStartupArray`, `LcdStartupChannel`, `RotationFlag`, `SingleGalleyTime`, `StartUpClockId`, `StartUpClockImageFileId`, `StartUpClockOnOff` | `_unknown_` |
| `Channel/SetCustom` | Configure Custom | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetCustomRequest` | `AuthorHeadId`, `AuthorId`, `AuthorNickName`, `CustomId`, `CustomPageIndex`, `FileId`, `GalleryId`, `ImageName`, `SoundFileId` | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelSetCustomResponse` |
| `Channel/SetCustomGalleryTime` | Configure Custom Gallery Time | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetCustomGalleryTimeRequest` | `CustomId`, `GalleryShowTimeFlag`, `SingleGalleyTime`, `SoundOnOff` | `_unknown_` |
| `Channel/SetCustomId` | Configure Custom Id | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetCustomIdRequest` | `CustomId` | `_unknown_` |
| `Channel/SetCustomPageIndex` | Configure Custom Page Index | `com.divoom.Divoom.http.request.channel.wifi.WifiSetCustomPageIndexRequest` | `CustomPageIndex` | `_unknown_` |
| `Channel/SetEqPosition` | Configure Eq Position | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetEqPositionRequest` | `EqPosition` | `_unknown_` |
| `Channel/SetEqTime` | Configure Eq Time | `_unknown_` | — | `_unknown_` |
| `Channel/SetIndependenceConfig` | Configure Independence Config | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetIndependenceConfigRequest` | `EndTime`, `IsEnable`, `StartTime`, `VoiceEnable`, `WeekArray` | `_unknown_` |
| `Channel/SetIndependenceName` | Configure Independence Name | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetIndependenceNameRequest` | `IndependenceName` | `_unknown_` |
| `Channel/SetIndex` | Configure Index | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetIndexRequest` | `SelectIndex` | `_unknown_` |
| `Channel/SetNightPreview` | Configure Night Preview | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetNightPreviewRequest` | `Brightness` | `_unknown_` |
| `Channel/SetNightView` | Configure Night View | `com.divoom.Divoom.http.request.system.WifiChannelSetNightViewRequest` | `Brightness`, `EndTime`, `OnOff`, `StartTime` | `_unknown_` |
| `Channel/SetNotifyList` | Configure Notify List | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetNotifyListRequest` | `NotifyList` | `_unknown_` |
| `Channel/SetOnOff` | Configure On Off | `com.divoom.Divoom.http.request.system.WifiChannelSetOnOffRequest` | `EndTime`, `OnOff`, `StartTime` | `_unknown_` |
| `Channel/SetProduceTime` | Configure Produce Time | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetProduceTimeRequest` | `ProduceTime` | `_unknown_` |
| `Channel/SetRGBInfo` | Configure RGBInfo | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetRGBInfoRequest` | `Brightness`, `Color`, `ColorCycle`, `KeyOnOff`, `LightList`, `OnOff`, `SelectLightIndex` | `_unknown_` |
| `Channel/SetStartupChannel` | Configure Startup Channel | `_unknown_` | — | `_unknown_` |
| `Channel/SetSubscribe` | Configure Subscribe | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetSubscribeRequest` | `AlbumId`, `AlbumName`, `AuthorType`, `PlayId`, `PlayName`, `SubscribeType`, `UserList` | `_unknown_` |
| `Channel/SetSubscribeGalleryTime` | Configure Subscribe Gallery Time | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetSubscribeGalleryTimeRequest` | `GalleryShowTimeFlag`, `SingleGalleyTime` | `_unknown_` |
| `Channel/SetSubscribeTime` | Configure Subscribe Time | `_unknown_` | — | `_unknown_` |
| `Channel/Store5LcdClockGetClassify` | Store5Lcd Clock Get Classify | `com.divoom.Divoom.http.request.channel.wifi.Store5LcdClockGetClassifyRequest` | `CountryISOCode`, `EndNum`, `StartNum` | `com.divoom.Divoom.http.response.channel.wifi.Store5LcdClockGetClassifyResponse` |
| `Channel/Store5LcdClockGetList` | Store5Lcd Clock Get List | `com.divoom.Divoom.http.request.channel.wifi.Store5LcdClockGetListRequest` | `CountryISOCode`, `EndNum`, `StartNum`, `ClassifyId`, `Flag` | `com.divoom.Divoom.http.response.channel.wifi.Store5LcdClockGetListResponse` |
| `Channel/StoreClockGetClassify` | Store Clock Get Classify | `_unknown_` | — | `_unknown_` |
| `Channel/StoreClockGetList` | Store Clock Get List | `com.divoom.Divoom.http.request.myCLock.MyClockStoreClockGetListRequest` | `CountryISOCode`, `EndNum`, `StartNum`, `ClassifyId`, `Flag` | `_unknown_` |
| `Channel/StoreGetBanner` | Store Get Banner | `com.divoom.Divoom.http.request.myCLock.MyClockStoreGetBannerRequest` | `CountryISOCode`, `EndNum`, `StartNum` | `_unknown_` |
| `Channel/StoreGetForumBannerList` | Store Get Forum Banner List | `_unknown_` | — | `_unknown_` |
| `Channel/StoreGetTopicBannerList` | Store Get Topic Banner List | `_unknown_` | — | `_unknown_` |
| `Channel/StoreGetTopicList` | Store Get Topic List | `_unknown_` | — | `_unknown_` |
| `Channel/StoreMyWorkshopClockList` | Store My Workshop Clock List | `_unknown_` | — | `_unknown_` |
| `Channel/StoreNew20` | Store New20 | `_unknown_` | — | `_unknown_` |
| `Channel/StoreTop20` | Store Top20 | `com.divoom.Divoom.http.request.myCLock.MyClockStoreTop20Request` | `CountryISOCode`, `EndNum`, `StartNum`, `Flag` | `_unknown_` |
| `Channel/StoreTopicClockGetList` | Store Topic Clock Get List | `com.divoom.Divoom.http.request.myCLock.MyClockStoreTopicClockGetListRequest` | `CountryISOCode`, `EndNum`, `StartNum`, `Flag`, `TopicId` | `_unknown_` |
| `Channel/UploadClockConfig` | Upload Clock Config | `com.divoom.Divoom.http.request.channel.wifi.WifiChannelUploadClockConfigRequest` | `Explain`, `ItemList`, `Name` | `_unknown_` |
| `Danmaku/GetBlueConfig` | Read Blue Config | `_unknown_` | — | `com.divoom.Divoom.http.response.danmaku.DanmakuGetBlueConfigResponse` |
| `Danmaku/GetConfig` | Read Config | `_unknown_` | — | `com.divoom.Divoom.http.response.danmaku.DanmakuGetConfigResponse` |
| `Danmaku/RandomFace` | Random Face | `_unknown_` | — | `_unknown_` |
| `Danmaku/SendBlueText` | Send Blue Text | `_unknown_` | — | `_unknown_` |
| `Danmaku/SendFace` | Send Face | `_unknown_` | — | `_unknown_` |
| `Danmaku/SendText` | Send Text | `_unknown_` | — | `_unknown_` |
| `Danmaku/SetBlueConfig` | Configure Blue Config | `_unknown_` | — | `_unknown_` |
| `Danmaku/SetConfig` | Configure Config | `_unknown_` | — | `_unknown_` |
| `Device/AppRestartMqtt` | App Restart Mqtt | `_unknown_` | — | `_unknown_` |
| `Device/BindUser` | Bind User | `_unknown_` | — | `_unknown_` |
| `Device/BlueNoLanguage` | Blue No Language | `com.divoom.Divoom.http.request.device.DeviceBlueNoLanguageRequest` | — | `com.divoom.Divoom.http.response.device.DeviceBlueNoLanguageResponse` |
| `Device/CloseClockTimer` | Close Clock Timer | `com.divoom.Divoom.http.request.device.DeviceCloseClockTimerRequest` | — | `_unknown_` |
| `Device/Connect` | Connect | `_unknown_` | — | `com.divoom.Divoom.http.response.device.DeviceDisconnectMqttResponse` |
| `Device/ConnectApp` | Connect App | `_unknown_` | — | `_unknown_` |
| `Device/DeleteResetAll` | Delete Reset All | `_unknown_` | — | `_unknown_` |
| `Device/DeleteShareCodeV2` | Delete Share Code V2 | `_unknown_` | — | `_unknown_` |
| `Device/DeleteUserV2` | Delete User V2 | `_unknown_` | — | `_unknown_` |
| `Device/Disconnect` | Disconnect | `_unknown_` | — | `com.divoom.Divoom.http.response.device.DeviceDisconnectMqttResponse` |
| `Device/DisconnectMqtt` | Disconnect Mqtt | `_unknown_` | — | `com.divoom.Divoom.http.response.device.DeviceDisconnectMqttResponse` |
| `Device/ExitDevice` | Exit Device | `_unknown_` | — | `_unknown_` |
| `Device/GetClassifyFontList` | Read Classify Font List | `_unknown_` | — | `_unknown_` |
| `Device/GetClockInfo` | Read Clock Info | `_unknown_` | — | `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockInfoResponse` |
| `Device/GetDelayPowerOff` | Read Delay Power Off | `com.divoom.Divoom.http.request.device.DeviceGetDelayPowerOffRequest` | — | `com.divoom.Divoom.http.response.device.DeviceGetDelayPowerOffResponse` |
| `Device/GetDispClassify` | Read Disp Classify | `_unknown_` | — | `_unknown_` |
| `Device/GetDispItemList` | Read Disp Item List | `_unknown_` | — | `_unknown_` |
| `Device/GetFileVersion` | Read File Version | `com.divoom.Divoom.http.request.device.DeviceGetFileVersionRequest` | `FileType` | `com.divoom.Divoom.http.response.device.DeviceGetFileVersionResponse` |
| `Device/GetFontClassify` | Read Font Classify | `_unknown_` | — | `_unknown_` |
| `Device/GetList` | Read List | `_unknown_` | — | `com.divoom.Divoom.http.response.device.DeviceGetListResponse` |
| `Device/GetListV2` | Read List V2 | `_unknown_` | — | `_unknown_` |
| `Device/GetNewBind` | Read New Bind | `_unknown_` | — | `com.divoom.Divoom.http.response.device.DeviceGetNewBindResponse` |
| `Device/GetNoBanFlag` | Read No Ban Flag | `com.divoom.Divoom.http.request.device.DeviceGetNoBanFlagRequest` | `NoBan` | `com.divoom.Divoom.http.response.device.DeviceGetNoBanFlagResponse` |
| `Device/GetNoMasterListV2` | Read No Master List V2 | `_unknown_` | — | `_unknown_` |
| `Device/GetShareCodeV2` | Read Share Code V2 | `_unknown_` | — | `_unknown_` |
| `Device/GetSomeFontInfo` | Read Some Font Info | `_unknown_` | — | `_unknown_` |
| `Device/GetStorageStatus` | Read Storage Status | `_unknown_` | — | `com.divoom.Divoom.http.response.device.DeviceGetStorageStatusResponse` |
| `Device/GetUpdateFileList` | Read Update File List | `com.divoom.Divoom.http.request.device.DeviceGetUpdateFileListRequest` | `HardwareList`, `IsTest` | `com.divoom.Divoom.http.response.device.DeviceGetUpdateFileListResponse` |
| `Device/GetUpdateInfo` | Read Update Info | `com.divoom.Divoom.http.request.device.DeviceGetUpdateInfoRequest` | `TestFlag` | `com.divoom.Divoom.http.response.device.DeviceGetUpdateInfoResponse` |
| `Device/GetUserDialList` | Read User Dial List | `_unknown_` | — | `_unknown_` |
| `Device/GiftMode` | Gift Mode | `com.divoom.Divoom.http.request.device.GiftModeRequest` | `GiftMode` | `_unknown_` |
| `Device/Hearbeat` | Hearbeat | `_unknown_` | — | `_unknown_` |
| `Device/InputShareCodeV2` | Input Share Code V2 | `_unknown_` | — | `_unknown_` |
| `Device/NotifyUpdate` | Notify Update | `_unknown_` | — | `_unknown_` |
| `Device/ResetAll` | Reset All | `_unknown_` | — | `_unknown_` |
| `Device/SetDelayPowerOff` | Configure Delay Power Off | `com.divoom.Divoom.http.request.device.DeviceSetDelayPowerOffRequest` | `DelayPowerOff` | `com.divoom.Divoom.http.response.device.DeviceSetDelayPowerOffResponse` |
| `Device/SetDeviceVersion` | Configure Device Version | `com.divoom.Divoom.http.request.device.DeviceSetDeviceVersionRequest` | `DeviceVersion` | `_unknown_` |
| `Device/SetLog` | Configure Log | `com.divoom.Divoom.http.request.device.DeviceSetLogRequest` | `Flag` | `com.divoom.Divoom.http.response.system.SysSetLogoResponse` |
| `Device/SetName` | Configure Name | `com.divoom.Divoom.http.request.device.DeviceSetNameRequest` | `DeviceName` | `_unknown_` |
| `Device/SetPlace` | Configure Place | `com.divoom.Divoom.http.request.device.DeviceSetPlaceRequest` | `DevicePlace` | `_unknown_` |
| `Device/SetUTC` | Configure UTC | `com.divoom.Divoom.http.request.device.DeviceSetUtcRequest` | `Time`, `Utc` | `_unknown_` |
| `Device/Unbind` | Unbind | `com.divoom.Divoom.http.request.device.DeviceUnbindRequest` | `TAG`, `UnBindDeviceId` | `_unknown_` |
| `Device/WiFiGetLanguageFlag` | Wi Fi Get Language Flag | `com.divoom.Divoom.http.request.device.DeviceWiFiGetLanguageFlagRequest` | — | `com.divoom.Divoom.http.response.device.DeviceWiFiGetLanguageFlagResponse` |

## Details

### `Channel/Add5LcdHistory`

- **Purpose:** Add5Lcd History
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/AddEqData`

- **Purpose:** Add Eq Data
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.ChannelAddEqDataRequest`

**Request parameters (non-inherited):**
- `AuthorHeadId` (`java.lang.String`)
- `AuthorId` (`int`)
- `AuthorNickName` (`java.lang.String`)
- `FileId` (`java.lang.String`)
- `ImageName` (`java.lang.String`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/AddHistory`

- **Purpose:** Add History
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelAddHistoryRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/AddIndependence`

- **Purpose:** Add Independence
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WIfiChannelAddIndependenceRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WIfiChannelAddIndependenceResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `LcdIndependence` (`int`)

### `Channel/CleanCustom`

- **Purpose:** Clean Custom
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelCleanCustomRequest`

**Request parameters (non-inherited):**
- `CustomPageIndex` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/ClockCommentLike`

- **Purpose:** Clock Comment Like
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/CoverPixelClock`

- **Purpose:** Cover Pixel Clock
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelCoverPixelClockRequest`

**Request parameters (non-inherited):**
- `CoverPixelFileId` (`java.lang.String`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/CustomChange`

- **Purpose:** Custom Change
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/DelHistory`

- **Purpose:** Del History
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/DelIndependence`

- **Purpose:** Del Independence
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WIfiChannelDelIndependenceRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*

### `Channel/DeleteCustom`

- **Purpose:** Delete Custom
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelDeleteCustomRequest`

**Request parameters (non-inherited):**
- `CustomId` (`int`)
- `CustomPageIndex` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/DeleteEq`

- **Purpose:** Delete Eq
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/DeletePixelClock`

- **Purpose:** Delete Pixel Clock
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/DeviceGetMyClock`

- **Purpose:** Device Get My Clock
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.DeviceGetMyClockRequest`

**Request parameters (non-inherited):**
- `ClockList` (`java.util.List`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/EqDataChange`

- **Purpose:** Eq Data Change
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/ExitNightPreview`

- **Purpose:** Exit Night Preview
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelExitNightPreviewRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/Get5LcdClockList`

- **Purpose:** Read Lcd Clock List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGet5LcdClockListV2Request`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiGet5LcdClockListResponse`

**Request parameters (non-inherited):**
- `Flag` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `GroupList` (`java.util.List`)

### `Channel/Get5LcdClockListV2`

- **Purpose:** Read Lcd Clock List V2
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGet5LcdClockListV2Request`

**Request parameters (non-inherited):**
- `Flag` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/Get5LcdInfo`

- **Purpose:** Read Lcd Info
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGet5LcdInfoV2Response`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `ChannelType` (`int`)
- `ClockId` (`int`)
- `LcdIndependence` (`int`)
- `LcdIndependenceList` (`java.util.List`)

### `Channel/Get5LcdInfoV2`

- **Purpose:** Read Lcd Info V2
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGet5LcdInfoV2Response`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `ChannelType` (`int`)
- `ClockId` (`int`)
- `LcdIndependence` (`int`)
- `LcdIndependenceList` (`java.util.List`)

### `Channel/GetAlbumTime`

- **Purpose:** Read Album Time
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/GetAll`

- **Purpose:** Read All
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.ChannelGetAllRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.ChannelGetAllResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `SceneList` (`java.util.List`)

### `Channel/GetAllCustomTime`

- **Purpose:** Read All Custom Time
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetAllCustomTimeResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `TimeList` (`java.util.List`)

### `Channel/GetAmbientLight`

- **Purpose:** Read Ambient Light
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetAmbientLightResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `Brightness` (`int`)
- `ColorCycle` (`int`)
- `EqOnOff` (`int`)
- `SelectEffect` (`int`)
- `color` (`java.lang.String`)

### `Channel/GetClockCommentList`

- **Purpose:** Read Clock Comment List
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/GetClockComponentDisplay`

- **Purpose:** Read Clock Component Display
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetClockComponentDisplayRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockComponentDisplayResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `Height` (`int`)
- `PreviewImageId` (`java.lang.String`)
- `RegionList` (`java.util.List`)
- `Width` (`int`)

### `Channel/GetClockConfig`

- **Purpose:** Read Clock Config
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetClockConfigRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockConfigResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `AlbumShapePicId` (`java.lang.String`)
- `AuthorUserId` (`int`)
- `ClockExPlain` (`java.lang.String`)
- `ClockExPlainPicId` (`java.lang.String`)
- `CommentCnt` (`int`)
- `FavoriteCnt` (`int`)
- `HeadId` (`java.lang.String`)
- `IsFavorite` (`int`)
- `IsMyLike` (`int`)
- `ItemList` (`java.util.List`)
- `ItemList2` (`java.util.List`)
- `Level` (`int`)
- `LikeCnt` (`int`)
- `NickName` (`java.lang.String`)

### `Channel/GetClockFont`

- **Purpose:** Read Clock Font
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockFontResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `FontId` (`int`)
- `FontList` (`java.util.List`)

### `Channel/GetClockInfo`

- **Purpose:** Read Clock Info
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetClockInfoRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockInfoResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `Brightness` (`int`)
- `ClockId` (`int`)
- `LcdIndex` (`int`)
- `ProduceTime` (`int`)

### `Channel/GetClockList`

- **Purpose:** Read Clock List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetClockListRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockListResponse`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `Flag` (`int`)
- `Version` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `HistoryFlag` (`int`)
- `GroupList` (`java.util.List`)

### `Channel/GetClockPlayPlanCycle`

- **Purpose:** Read Clock Play Plan Cycle
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/GetClockPlayPlanDate`

- **Purpose:** Read Clock Play Plan Date
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/GetClockStyle`

- **Purpose:** Read Clock Style
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetClockStyleRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockStyleResponse`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `CurStyleId` (`int`)
- `CurStylePixelImageId` (`java.lang.String`)
- `StyleList` (`java.util.List`)

### `Channel/GetConfig`

- **Purpose:** Read Config
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetConfigRequest`
- **Response class:** `com.divoom.Divoom.http.response.danmaku.DanmakuGetConfigResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `DisplayArea` (`int`)
- `Speed` (`int`)

### `Channel/GetCustomGalleryTime`

- **Purpose:** Read Custom Gallery Time
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetCustomGalleryTimeRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetCustomGalleryTimeResponse`

**Request parameters (non-inherited):**
- `CustomId` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `GalleryShowTimeFlag` (`int`)
- `SingleGalleyTime` (`int`)
- `SoundOnOff` (`int`)

### `Channel/GetCustomList`

- **Purpose:** Read Custom List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetCustomListRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetCustomListResponse`

**Request parameters (non-inherited):**
- `CustomPageIndex` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `CustomList` (`java.util.List`)

### `Channel/GetCustomPageIndex`

- **Purpose:** Read Custom Page Index
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetCustomPageIndexResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `CustomPageIndex` (`int`)

### `Channel/GetElementStyleList`

- **Purpose:** Read Element Style List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetElementStyleListRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetElementStyleListResponse`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)
- `ItemType` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `GroupList` (`java.util.List`)

### `Channel/GetEqDataList`

- **Purpose:** Read Eq Data List
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetEqDataListResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `EqDataList` (`java.util.List`)

### `Channel/GetEqPosition`

- **Purpose:** Read Eq Position
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetEqPositionResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `EqPosition` (`int`)

### `Channel/GetEqTime`

- **Purpose:** Read Eq Time
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/GetIndependenceConfig`

- **Purpose:** Read Independence Config
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetIndependenceConfigRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetIndependenceConfigResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `EndTime` (`int`)
- `IsEnable` (`int`)
- `StartTime` (`int`)
- `VoiceEnable` (`int`)
- `WeekArray` (`java.util.List`)

### `Channel/GetIndex`

- **Purpose:** Read Index
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetIndexResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `SelectIndex` (`int`)

### `Channel/GetNightView`

- **Purpose:** Read Night View
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.system.WifiChannelGetNightViewResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `Brightness` (`int`)
- `EndTime` (`int`)
- `OnOff` (`int`)
- `StartTime` (`int`)

### `Channel/GetNotifyList`

- **Purpose:** Read Notify List
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetNotifyListResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `NotifyList` (`java.util.List`)

### `Channel/GetOnOff`

- **Purpose:** Read On Off
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.system.WifiChannelGetOnOffResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `EndTime` (`int`)
- `OnOff` (`int`)
- `StartTime` (`int`)

### `Channel/GetOnOffScreen`

- **Purpose:** Read On Off Screen
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.ChannelOnOffScreenRequest`
- **Response class:** `com.divoom.Divoom.http.response.system.WifiChannelGetOnOffScreenResponse`

**Request parameters (non-inherited):**
- `OnOff` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `OnOff` (`int`)

### `Channel/GetOneCustom`

- **Purpose:** Read One Custom
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.ChannelGetOneCustomRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.ChannelGetOneCustomResponse`

**Request parameters (non-inherited):**
- `CustomId` (`int`)
- `CustomPageIndex` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `CustomId` (`int`)
- `CustomPageIndex` (`int`)
- `FileId` (`java.lang.String`)

### `Channel/GetRGBInfo`

- **Purpose:** Read RGBInfo
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetRGBInfoResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `brightness` (`int`)
- `color` (`java.lang.String`)
- `colorCycle` (`int`)
- `keyOnOff` (`int`)
- `lightList` (`java.util.List`)
- `onOff` (`int`)
- `selectLightIndex` (`int`)

### `Channel/GetSongInfo`

- **Purpose:** Read Song Info
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.ChannelGetSongInfoRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.ChannelGetSongInfoResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `songInfo` (`java.lang.String`)

### `Channel/GetStartupChannel`

- **Purpose:** Read Startup Channel
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/GetSubClockList`

- **Purpose:** Read Sub Clock List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetSubClockListRequest`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)
- `ClockType` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

### `Channel/GetSubscribe`

- **Purpose:** Read Subscribe
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelGetSubscribeRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetSubscribeResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `AlbumId` (`int`)
- `AlbumName` (`java.lang.String`)
- `AuthorType` (`int`)
- `PlayId` (`int`)
- `PlayName` (`java.lang.String`)
- `SubscribeType` (`int`)
- `UserList` (`java.util.List`)

### `Channel/GetSubscribeGalleryTime`

- **Purpose:** Read Subscribe Gallery Time
- **Category:** Channel
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetSubscribeGalleryTimeResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `GalleryShowTimeFlag` (`int`)
- `SingleGalleyTime` (`int`)

### `Channel/GetSubscribeTime`

- **Purpose:** Read Subscribe Time
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/ItemSearch`

- **Purpose:** Item Search
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelItemSearchRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelItemSearchResponse`

**Request parameters (non-inherited):**
- `EndNum` (`int`)
- `ItemFlag` (`java.lang.String`)
- `ItemId` (`java.lang.String`)
- `Key` (`java.lang.String`)
- `StartNum` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `SearchList` (`java.util.List`)

### `Channel/LikeClock`

- **Purpose:** Like Clock
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.MyClockLikeClockRequest`

**Request parameters (non-inherited):**
- `LikeFlag` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/LoginThird`

- **Purpose:** Login Third
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelLoginThirdRequest`

**Request parameters (non-inherited):**
- `LogInfo` (`java.util.List`)
- `Type` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/My5LcdClockAdd`

- **Purpose:** My5Lcd Clock Add
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.My5LcdClockAddRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/My5LcdClockGetList`

- **Purpose:** My5Lcd Clock Get List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.My5LcdClockGetListRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.My5LcdClockGetListResponse`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)
- `Flag` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `ClockList` (`java.util.List`)

### `Channel/My5LcdClockInsertPosition`

- **Purpose:** My5Lcd Clock Insert Position
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.My5LcdClockInsertPositionRequest`

**Request parameters (non-inherited):**
- `NewPositionClockId` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/My5LcdClockRemove`

- **Purpose:** My5Lcd Clock Remove
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.My5LcdClockRemoveRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/MyClockAdd`

- **Purpose:** My Clock Add
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.MyClockAddRecentRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/MyClockAddRecent`

- **Purpose:** My Clock Add Recent
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.MyClockAddRecentRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/MyClockBatchRemove`

- **Purpose:** My Clock Batch Remove
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.MyClockBatchRemoveRequest`

**Request parameters (non-inherited):**
- `ClockList` (`java.util.List`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/MyClockGetFavoriteList`

- **Purpose:** My Clock Get Favorite List
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/MyClockGetList`

- **Purpose:** My Clock Get List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.MyClockGetListRequest`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)
- `Flag` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

### `Channel/MyClockGetRecentList`

- **Purpose:** My Clock Get Recent List
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/MyClockInsertPosition`

- **Purpose:** My Clock Insert Position
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.MyClockInsertPositionRequest`

**Request parameters (non-inherited):**
- `NewPositionClockId` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/MyClockRemove`

- **Purpose:** My Clock Remove
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.MyClockRemoveRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/MyClockSetFavorite`

- **Purpose:** My Clock Set Favorite
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/NewPixelClock`

- **Purpose:** New Pixel Clock
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelNewPixelClockRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelNewPixelClockResponse`

**Request parameters (non-inherited):**
- `ClockType` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `ClockId` (`int`)
- `ClockName` (`java.lang.String`)
- `ClockType` (`int`)
- `ImagePixelId` (`java.lang.String`)

### `Channel/OnOffScreen`

- **Purpose:** On Off Screen
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.ChannelOnOffScreenRequest`
- **Response class:** `com.divoom.Divoom.http.response.system.WifiChannelGetOnOffScreenResponse`

**Request parameters (non-inherited):**
- `OnOff` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `OnOff` (`int`)

### `Channel/RenamePixelClock`

- **Purpose:** Rename Pixel Clock
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelRenamePixelClockRequest`

**Request parameters (non-inherited):**
- `ClockName` (`java.lang.String`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/ReportClockComment`

- **Purpose:** Report Clock Comment
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/ResetClock`

- **Purpose:** Reset Clock
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelResetClockRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/Set5LcdChannelType`

- **Purpose:** Configure Lcd Channel Type
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSet5LcdChannelTypeRequest`

**Request parameters (non-inherited):**
- `ChannelType` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*

### `Channel/Set5LcdWholeClockId`

- **Purpose:** Configure Lcd Whole Clock Id
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSet5LcdWholeClockIdRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/SetAlbumTime`

- **Purpose:** Configure Album Time
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/SetAllCustomTime`

- **Purpose:** Configure All Custom Time
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetAllCustomTimeRequest`

**Request parameters (non-inherited):**
- `TimeList` (`java.util.List`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/SetAmbientLight`

- **Purpose:** Configure Ambient Light
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetAmbientLightRequest`

**Request parameters (non-inherited):**
- `Brightness` (`int`)
- `Color` (`java.lang.String`)
- `ColorCycle` (`int`)
- `EqOnOff` (`int`)
- `SelectEffect` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/SetBrightness`

- **Purpose:** Configure Brightness
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetBrightnessRequest`
- **Response class:** `com.divoom.Divoom.http.response.system.SysSetBrightnessResponse`

**Request parameters (non-inherited):**
- `Brightness` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `Brightness` (`int`)
- `SetUserId` (`int`)

### `Channel/SetClockConfig`

- **Purpose:** Configure Clock Config
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetClockConfigRequest`

**Request parameters (non-inherited):**
- `ItemList` (`java.util.List`)
- `ItemList2` (`java.util.List`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/SetClockConfigSpecial`

- **Purpose:** Configure Clock Config Special
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/SetClockPlayPlanCycle`

- **Purpose:** Configure Clock Play Plan Cycle
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.SetClockPlayPlanCycleRequest`

**Request parameters (non-inherited):**
- `CycleRuleList` (`java.util.List`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/SetClockPlayPlanDate`

- **Purpose:** Configure Clock Play Plan Date
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.SetClockPlayPlanDateRequest`

**Request parameters (non-inherited):**
- `DateRuleList` (`java.util.List`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/SetClockSelectId`

- **Purpose:** Configure Clock Select Id
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetClockSelectIdRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/SetClockStyle`

- **Purpose:** Configure Clock Style
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetClockStyleRequest`

**Request parameters (non-inherited):**
- `StyleId` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Channel/SetConfig`

- **Purpose:** Configure Config
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetConfigRequest`

**Request parameters (non-inherited):**
- `ChannelIndex` (`int`)
- `ClockTime` (`int`)
- `GalleryShowTimeFlag` (`int`)
- `GalleryTime` (`int`)
- `LcdStartupArray` (`java.util.List`)
- `LcdStartupChannel` (`int`)
- `RotationFlag` (`int`)
- `SingleGalleyTime` (`int`)
- `StartUpClockId` (`int`)
- `StartUpClockImageFileId` (`java.lang.String`)
- `StartUpClockOnOff` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/SetCustom`

- **Purpose:** Configure Custom
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetCustomRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelSetCustomResponse`

**Request parameters (non-inherited):**
- `AuthorHeadId` (`java.lang.String`)
- `AuthorId` (`int`)
- `AuthorNickName` (`java.lang.String`)
- `CustomId` (`int`)
- `CustomPageIndex` (`int`)
- `FileId` (`java.lang.String`)
- `GalleryId` (`int`)
- `ImageName` (`java.lang.String`)
- `SoundFileId` (`java.lang.String`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `CustomId` (`int`)

### `Channel/SetCustomGalleryTime`

- **Purpose:** Configure Custom Gallery Time
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetCustomGalleryTimeRequest`

**Request parameters (non-inherited):**
- `CustomId` (`int`)
- `GalleryShowTimeFlag` (`int`)
- `SingleGalleyTime` (`int`)
- `SoundOnOff` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/SetCustomId`

- **Purpose:** Configure Custom Id
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetCustomIdRequest`

**Request parameters (non-inherited):**
- `CustomId` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/SetCustomPageIndex`

- **Purpose:** Configure Custom Page Index
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiSetCustomPageIndexRequest`

**Request parameters (non-inherited):**
- `CustomPageIndex` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/SetEqPosition`

- **Purpose:** Configure Eq Position
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetEqPositionRequest`

**Request parameters (non-inherited):**
- `EqPosition` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/SetEqTime`

- **Purpose:** Configure Eq Time
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/SetIndependenceConfig`

- **Purpose:** Configure Independence Config
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetIndependenceConfigRequest`

**Request parameters (non-inherited):**
- `EndTime` (`int`)
- `IsEnable` (`int`)
- `StartTime` (`int`)
- `VoiceEnable` (`int`)
- `WeekArray` (`java.util.List`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*

### `Channel/SetIndependenceName`

- **Purpose:** Configure Independence Name
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetIndependenceNameRequest`

**Request parameters (non-inherited):**
- `IndependenceName` (`java.lang.String`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*

### `Channel/SetIndex`

- **Purpose:** Configure Index
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetIndexRequest`

**Request parameters (non-inherited):**
- `SelectIndex` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/SetNightPreview`

- **Purpose:** Configure Night Preview
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetNightPreviewRequest`

**Request parameters (non-inherited):**
- `Brightness` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/SetNightView`

- **Purpose:** Configure Night View
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.system.WifiChannelSetNightViewRequest`

**Request parameters (non-inherited):**
- `Brightness` (`int`)
- `EndTime` (`int`)
- `OnOff` (`int`)
- `StartTime` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/SetNotifyList`

- **Purpose:** Configure Notify List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetNotifyListRequest`

**Request parameters (non-inherited):**
- `NotifyList` (`java.util.List`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/SetOnOff`

- **Purpose:** Configure On Off
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.system.WifiChannelSetOnOffRequest`

**Request parameters (non-inherited):**
- `EndTime` (`int`)
- `OnOff` (`int`)
- `StartTime` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/SetProduceTime`

- **Purpose:** Configure Produce Time
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetProduceTimeRequest`

**Request parameters (non-inherited):**
- `ProduceTime` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/SetRGBInfo`

- **Purpose:** Configure RGBInfo
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetRGBInfoRequest`

**Request parameters (non-inherited):**
- `Brightness` (`int`)
- `Color` (`java.lang.String`)
- `ColorCycle` (`int`)
- `KeyOnOff` (`int`)
- `LightList` (`java.util.List`)
- `OnOff` (`int`)
- `SelectLightIndex` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Channel/SetStartupChannel`

- **Purpose:** Configure Startup Channel
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/SetSubscribe`

- **Purpose:** Configure Subscribe
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetSubscribeRequest`

**Request parameters (non-inherited):**
- `AlbumId` (`int`)
- `AlbumName` (`java.lang.String`)
- `AuthorType` (`int`)
- `PlayId` (`int`)
- `PlayName` (`java.lang.String`)
- `SubscribeType` (`int`)
- `UserList` (`java.util.List`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/SetSubscribeGalleryTime`

- **Purpose:** Configure Subscribe Gallery Time
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelSetSubscribeGalleryTimeRequest`

**Request parameters (non-inherited):**
- `GalleryShowTimeFlag` (`int`)
- `SingleGalleyTime` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*

### `Channel/SetSubscribeTime`

- **Purpose:** Configure Subscribe Time
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/Store5LcdClockGetClassify`

- **Purpose:** Store5Lcd Clock Get Classify
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.Store5LcdClockGetClassifyRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.Store5LcdClockGetClassifyResponse`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `ClassifyList` (`java.util.List`)

### `Channel/Store5LcdClockGetList`

- **Purpose:** Store5Lcd Clock Get List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.Store5LcdClockGetListRequest`
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.Store5LcdClockGetListResponse`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)
- `ClassifyId` (`int`)
- `Flag` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `ClockList` (`java.util.List`)

### `Channel/StoreClockGetClassify`

- **Purpose:** Store Clock Get Classify
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/StoreClockGetList`

- **Purpose:** Store Clock Get List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.MyClockStoreClockGetListRequest`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)
- `ClassifyId` (`int`)
- `Flag` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

### `Channel/StoreGetBanner`

- **Purpose:** Store Get Banner
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.MyClockStoreGetBannerRequest`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

### `Channel/StoreGetForumBannerList`

- **Purpose:** Store Get Forum Banner List
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/StoreGetTopicBannerList`

- **Purpose:** Store Get Topic Banner List
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/StoreGetTopicList`

- **Purpose:** Store Get Topic List
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/StoreMyWorkshopClockList`

- **Purpose:** Store My Workshop Clock List
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/StoreNew20`

- **Purpose:** Store New20
- **Category:** Channel

**Request parameters (non-inherited):**
_none / empty payload_

### `Channel/StoreTop20`

- **Purpose:** Store Top20
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.MyClockStoreTop20Request`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)
- `Flag` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

### `Channel/StoreTopicClockGetList`

- **Purpose:** Store Topic Clock Get List
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.myCLock.MyClockStoreTopicClockGetListRequest`

**Request parameters (non-inherited):**
- `CountryISOCode` (`java.lang.String`)
- `EndNum` (`int`)
- `StartNum` (`int`)
- `Flag` (`int`)
- `TopicId` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

### `Channel/UploadClockConfig`

- **Purpose:** Upload Clock Config
- **Category:** Channel
- **Request class:** `com.divoom.Divoom.http.request.channel.wifi.WifiChannelUploadClockConfigRequest`

**Request parameters (non-inherited):**
- `Explain` (`java.lang.String`)
- `ItemList` (`java.util.List`)
- `Name` (`java.lang.String`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*
- `LcdIndependence` (`int`) *(inherited)*
- `LcdIndex` (`int`) *(inherited)*
- `PageIndex` (`int`) *(inherited)*
- `ParentClockId` (`int`) *(inherited)*
- `ParentItemId` (`java.lang.String`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Danmaku/GetBlueConfig`

- **Purpose:** Read Blue Config
- **Category:** Danmaku
- **Response class:** `com.divoom.Divoom.http.response.danmaku.DanmakuGetBlueConfigResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `Background` (`int`)
- `Color` (`java.lang.String`)
- `Speed` (`int`)
- `TextSize` (`int`)

### `Danmaku/GetConfig`

- **Purpose:** Read Config
- **Category:** Danmaku
- **Response class:** `com.divoom.Divoom.http.response.danmaku.DanmakuGetConfigResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `DisplayArea` (`int`)
- `Speed` (`int`)

### `Danmaku/RandomFace`

- **Purpose:** Random Face
- **Category:** Danmaku

**Request parameters (non-inherited):**
_none / empty payload_

### `Danmaku/SendBlueText`

- **Purpose:** Send Blue Text
- **Category:** Danmaku

**Request parameters (non-inherited):**
_none / empty payload_

### `Danmaku/SendFace`

- **Purpose:** Send Face
- **Category:** Danmaku

**Request parameters (non-inherited):**
_none / empty payload_

### `Danmaku/SendText`

- **Purpose:** Send Text
- **Category:** Danmaku

**Request parameters (non-inherited):**
_none / empty payload_

### `Danmaku/SetBlueConfig`

- **Purpose:** Configure Blue Config
- **Category:** Danmaku

**Request parameters (non-inherited):**
_none / empty payload_

### `Danmaku/SetConfig`

- **Purpose:** Configure Config
- **Category:** Danmaku

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/AppRestartMqtt`

- **Purpose:** App Restart Mqtt
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/BindUser`

- **Purpose:** Bind User
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/BlueNoLanguage`

- **Purpose:** Blue No Language
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceBlueNoLanguageRequest`
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceBlueNoLanguageResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)

### `Device/CloseClockTimer`

- **Purpose:** Close Clock Timer
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceCloseClockTimerRequest`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `ClockId` (`int`) *(inherited)*

### `Device/Connect`

- **Purpose:** Connect
- **Category:** Device
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceDisconnectMqttResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `Online` (`int`)

### `Device/ConnectApp`

- **Purpose:** Connect App
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/DeleteResetAll`

- **Purpose:** Delete Reset All
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/DeleteShareCodeV2`

- **Purpose:** Delete Share Code V2
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/DeleteUserV2`

- **Purpose:** Delete User V2
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/Disconnect`

- **Purpose:** Disconnect
- **Category:** Device
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceDisconnectMqttResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `Online` (`int`)

### `Device/DisconnectMqtt`

- **Purpose:** Disconnect Mqtt
- **Category:** Device
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceDisconnectMqttResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `Online` (`int`)

### `Device/ExitDevice`

- **Purpose:** Exit Device
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/GetClassifyFontList`

- **Purpose:** Read Classify Font List
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/GetClockInfo`

- **Purpose:** Read Clock Info
- **Category:** Device
- **Response class:** `com.divoom.Divoom.http.response.channel.wifi.WifiChannelGetClockInfoResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `Brightness` (`int`)
- `ClockId` (`int`)
- `LcdIndex` (`int`)
- `ProduceTime` (`int`)

### `Device/GetDelayPowerOff`

- **Purpose:** Read Delay Power Off
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceGetDelayPowerOffRequest`
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceGetDelayPowerOffResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `DelayPowerOff` (`int`)

### `Device/GetDispClassify`

- **Purpose:** Read Disp Classify
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/GetDispItemList`

- **Purpose:** Read Disp Item List
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/GetFileVersion`

- **Purpose:** Read File Version
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceGetFileVersionRequest`
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceGetFileVersionResponse`

**Request parameters (non-inherited):**
- `FileType` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `FileId` (`java.lang.String`)
- `FileType` (`int`)
- `Version` (`int`)

### `Device/GetFontClassify`

- **Purpose:** Read Font Classify
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/GetList`

- **Purpose:** Read List
- **Category:** Device
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceGetListResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `DeviceList` (`java.util.List`)
- `MasterFlag` (`int`)
- `UserPublicIP` (`java.lang.String`)

### `Device/GetListV2`

- **Purpose:** Read List V2
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/GetNewBind`

- **Purpose:** Read New Bind
- **Category:** Device
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceGetNewBindResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `NewBindFlag` (`int`)

### `Device/GetNoBanFlag`

- **Purpose:** Read No Ban Flag
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceGetNoBanFlagRequest`
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceGetNoBanFlagResponse`

**Request parameters (non-inherited):**
- `NoBan` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `NoBan` (`int`)

### `Device/GetNoMasterListV2`

- **Purpose:** Read No Master List V2
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/GetShareCodeV2`

- **Purpose:** Read Share Code V2
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/GetSomeFontInfo`

- **Purpose:** Read Some Font Info
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/GetStorageStatus`

- **Purpose:** Read Storage Status
- **Category:** Device
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceGetStorageStatusResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Response fields:**
- `Command` (`java.lang.String`)
- `DeviceId` (`long`)
- `ReturnCode` (`int`)
- `ReturnMessage` (`java.lang.String`)
- `androidCacheTime` (`long`)
- `Full` (`int`)

### `Device/GetUpdateFileList`

- **Purpose:** Read Update File List
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceGetUpdateFileListRequest`
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceGetUpdateFileListResponse`

**Request parameters (non-inherited):**
- `HardwareList` (`java.util.List`)
- `IsTest` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `VersionList` (`java.util.List`)

### `Device/GetUpdateInfo`

- **Purpose:** Read Update Info
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceGetUpdateInfoRequest`
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceGetUpdateInfoResponse`

**Request parameters (non-inherited):**
- `TestFlag` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*
- `Language` (`java.lang.String`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `CanUpdate` (`int`)
- `Version` (`java.lang.String`)

### `Device/GetUserDialList`

- **Purpose:** Read User Dial List
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/GiftMode`

- **Purpose:** Gift Mode
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.GiftModeRequest`

**Request parameters (non-inherited):**
- `GiftMode` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Device/Hearbeat`

- **Purpose:** Hearbeat
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/InputShareCodeV2`

- **Purpose:** Input Share Code V2
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/NotifyUpdate`

- **Purpose:** Notify Update
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/ResetAll`

- **Purpose:** Reset All
- **Category:** Device

**Request parameters (non-inherited):**
_none / empty payload_

### `Device/SetDelayPowerOff`

- **Purpose:** Configure Delay Power Off
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceSetDelayPowerOffRequest`
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceSetDelayPowerOffResponse`

**Request parameters (non-inherited):**
- `DelayPowerOff` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)

### `Device/SetDeviceVersion`

- **Purpose:** Configure Device Version
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceSetDeviceVersionRequest`

**Request parameters (non-inherited):**
- `DeviceVersion` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Device/SetLog`

- **Purpose:** Configure Log
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceSetLogRequest`
- **Response class:** `com.divoom.Divoom.http.response.system.SysSetLogoResponse`

**Request parameters (non-inherited):**
- `Flag` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)

### `Device/SetName`

- **Purpose:** Configure Name
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceSetNameRequest`

**Request parameters (non-inherited):**
- `DeviceName` (`java.lang.String`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Device/SetPlace`

- **Purpose:** Configure Place
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceSetPlaceRequest`

**Request parameters (non-inherited):**
- `DevicePlace` (`int`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Device/SetUTC`

- **Purpose:** Configure UTC
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceSetUtcRequest`

**Request parameters (non-inherited):**
- `Time` (`java.lang.String`)
- `Utc` (`long`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Device/Unbind`

- **Purpose:** Unbind
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceUnbindRequest`

**Request parameters (non-inherited):**
- `TAG` (`java.lang.String`)
- `UnBindDeviceId` (`long`)

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

### `Device/WiFiGetLanguageFlag`

- **Purpose:** Wi Fi Get Language Flag
- **Category:** Device
- **Request class:** `com.divoom.Divoom.http.request.device.DeviceWiFiGetLanguageFlagRequest`
- **Response class:** `com.divoom.Divoom.http.response.device.DeviceWiFiGetLanguageFlagResponse`

**Request parameters (non-inherited):**
_none / empty payload_

**Inherited/common request parameters:**
- `Command` (`java.lang.String`) *(inherited)*
- `DeviceId` (`long`) *(inherited)*
- `DevicePassword` (`java.lang.Integer`) *(inherited)*
- `LocalToken` (`java.lang.Integer`) *(inherited)*

**Response fields:**
- `androidCacheTime` (`long`)
- `ProhibitionLanguage` (`int`)
